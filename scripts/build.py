#!/usr/bin/env python3
"""Build the glossary, string table, style stats and prompt snippets from the
official i18n files under sources/.

Usage: python3 scripts/build.py
No third-party dependencies.
"""
import csv
import importlib.util
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
DATA = ROOT / "data"
DIST = ROOT / "dist"
TERMS = json.loads((ROOT / "glossary" / "terms.json").read_text(encoding="utf-8"))
LOCALES = TERMS["locales"]
LOCALE_NAMES = {"zh-Hans": "简体中文", "zh-Hant": "繁體中文", "ja-JP": "日本語", "ko-KR": "한국어",
                "de-DE": "Deutsch", "fr-FR": "Français", "es-ES": "Español", "pt-BR": "Português (Brasil)",
                "it-IT": "Italiano", "ru": "Русский", "hi-IN": "हिन्दी"}
# Locales without word spacing: variants are matched as plain substrings.
# Everywhere else a variant matches case-insensitively at the start of a word, so stems cover inflections.
CJK = {"zh-Hans", "zh-Hant", "ja-JP", "ko-KR"}
WORD_START = r"(?<![\w\u0900-\u097F])"
# claude.ai once named Simplified Chinese zh-CN; normalize aliases to canonical locales
ALIASES = {"zh-CN": "zh-Hans", "zh-TW": "zh-Hant", "ja": "ja-JP", "ko": "ko-KR", "en": "en-US"}
EXAMPLES_PER_TERM = 4
LABELS = {"desktop": "Claude Desktop", "web": "claude.ai", "web-dynamic": "claude.ai dynamic strings"}
SKILL = ROOT / "skills" / "claude-i18n-style"
SKILL_EXAMPLES = 2


def load_corpus(directory):
    """Read <locale>.json files in a directory and return {locale: {key: text}}."""
    out = {}
    for f in sorted(directory.glob("*.json")):
        locale = ALIASES.get(f.stem, f.stem)
        out[locale] = json.loads(f.read_text(encoding="utf-8"))
    return out


def load_sources():
    """Return [(source_name, {locale: {key: text}})] for sources that include en-US."""
    corpora = []
    for name, path in [
        ("desktop", SOURCES / "desktop"),
        ("web", SOURCES / "web"),
        ("web-dynamic", SOURCES / "web" / "dynamic"),
    ]:
        if path.is_dir():
            corpus = load_corpus(path)
            if "en-US" in corpus:
                corpora.append((name, corpus))
    return corpora


def variant_pattern(v, locale):
    return re.compile(re.escape(v) if locale in CJK else WORD_START + re.escape(v), 0 if locale in CJK else re.I)


def count_variants(text, variants, locale):
    """Count variants longest first so a short variant isn't also counted inside a longer one."""
    counts = Counter()
    for v in sorted(variants, key=len, reverse=True):
        text, n = variant_pattern(v, locale).subn("\0", text)
        if n:
            counts[v] += n
    return counts


def analyze_terms(corpora):
    results = []
    for term in TERMS["terms"]:
        pattern = re.compile(term["match"], re.I)
        stats = {loc: Counter() for loc in LOCALES}
        missing = Counter()
        examples = []
        total = 0
        for source, corpus in corpora:
            en = corpus["en-US"]
            for key, text in en.items():
                if not pattern.search(text):
                    continue
                total += 1
                row = {"source": source, "key": key, "en-US": text}
                for loc in LOCALES:
                    tr = corpus.get(loc, {}).get(key)
                    row[loc] = tr
                    if tr is None:
                        # Only count as untranslated when the source ships this locale at all
                        if loc in corpus:
                            missing[loc] += 1
                    else:
                        stats[loc].update(count_variants(tr, term["variants"].get(loc, []), loc))
                examples.append(row)
        # Prefer the shortest examples: closest to the bare term
        examples.sort(key=lambda r: (sum(r[l] is None for l in LOCALES), len(r["en-US"])))
        results.append({
            **{k: term[k] for k in ("id", "category", "en", "note")},
            "recommended": {loc: term["recommended"].get(loc) for loc in LOCALES},
            "occurrences": total,
            "observed": {loc: dict(stats[loc].most_common()) for loc in LOCALES},
            "untranslated": dict(missing),
            "examples": examples[:EXAMPLES_PER_TERM],
        })
    return results


HAN = r"\u4e00-\u9fff"
LATIN = r"A-Za-z0-9"


def style_stats(corpora):
    """Collect per-locale style stats: forms of address, quotes, ellipses, CJK-Latin spacing, etc."""
    texts = {loc: [] for loc in LOCALES}
    for _, corpus in corpora:
        for loc in LOCALES:
            texts[loc].extend(corpus.get(loc, {}).values())
    out = {}
    for loc in ("zh-Hans", "zh-Hant"):
        joined = "\n".join(texts[loc])
        spaced = len(re.findall(rf"[{HAN}] [{LATIN}]|[{LATIN}] [{HAN}]", joined))
        tight = len(re.findall(rf"[{HAN}][{LATIN}]|[{LATIN}][{HAN}]", joined))
        out[loc] = {
            "strings": len(texts[loc]),
            "您": joined.count("您"),
            "你": joined.count("你") - joined.count("你们"),
            "“”": joined.count("“"),
            "「」": joined.count("「"),
            "ASCII quotes": len(re.findall(rf'[{HAN}]"|"[{HAN}]', joined)) // 2,
            "…": joined.count("…"),
            "...": joined.count("..."),
            "CJK-Latin spaced": spaced,
            "CJK-Latin unspaced": tight,
            "请": joined.count("请") + joined.count("請"),
            "fullwidth comma ，": joined.count("，"),
            "ASCII comma after Han": len(re.findall(rf"[{HAN}],", joined)),
        }
    ja = "\n".join(texts["ja-JP"])
    out["ja-JP"] = {
        "strings": len(texts["ja-JP"]),
        "です/ます endings": len(re.findall(r"(です|ます|ました|ません)[。]?$", ja, re.M)),
        "だ/である endings": len(re.findall(r"(だ|である)[。]?$", ja, re.M)),
        "「」": ja.count("「"),
        "…": ja.count("…"),
        "フォルダ": len(re.findall(r"フォルダ(?!ー)", ja)),
        "フォルダー": ja.count("フォルダー"),
    }
    en_texts = [t for _, corpus in corpora for t in corpus["en-US"].values()]
    en = "\n".join(en_texts)
    small = {"a", "an", "the", "and", "or", "to", "of", "in", "on", "for", "with", "by", "at", "from", "as", "is"}
    title = sentence = 0
    for t in en_texts:
        words = t.split()
        if not 2 <= len(words) <= 5 or not re.fullmatch(r"[A-Za-z][A-Za-z ’'-]*", t):
            continue
        caps = [w[0].isupper() for w in words[1:] if w.lower() not in small]
        title += bool(caps) and all(caps)
        sentence += bool(caps) and not any(caps)
    out["en-US"] = {
        "strings": len(en_texts),
        "sentence case, short strings": sentence,
        "Title Case, short strings": title,
        "…": en.count("…"),
        "...": len(re.findall(r"\.\.\.", en)),
        "’": en.count("’"),
        "' within words": len(re.findall(r"\w'\w", en)),
        "“”": en.count("“"),
        "\"": en.count('"'),
        "—": en.count("—"),
        "' - '": en.count(" - "),
        "contractions": len(re.findall(r"\b(can|isn|don|Don|you)['’](t|re)\b", en)),
        "full forms": len(re.findall(r"\b(cannot|is not|[Dd]o not|you are)\b", en)),
        "you": len(re.findall(r"\b[Yy]ou\b", en)),
        "we": len(re.findall(r"\b[Ww]e\b", en)),
        "Oxford comma": len(re.findall(r"\w+, \w+, and \w", en)),
        "no Oxford comma": len(re.findall(r"\w+, \w+ and \w", en)),
        "sign in": len(re.findall(r"\b[Ss]ign in\b", en)),
        "log in": len(re.findall(r"\b[Ll]og in\b", en)),
        "Couldn’t …": len(re.findall(r"\b[Cc]ouldn['’]t\b", en)),
        "Failed to …": en.count("Failed to"),
        "Unable to / Could not …": en.count("Unable to") + en.count("Could not"),
        "Try again": len(re.findall(r"\b[Tt]ry again", en)),
        "Please try again": en.count("Please try again"),
        "Sorry / Oops": len(re.findall(r"\b(Sorry|sorry|Oops)\b", en)),
        "!": en.count("!"),
    }
    ko = "\n".join(texts["ko-KR"])
    out["ko-KR"] = {
        "strings": len(texts["ko-KR"]),
        "합니다/습니다 style": len(re.findall(r"(합니다|습니다|십시오)[.]?", ko)),
        "~요 endings": len(re.findall(r"(해요|세요|어요|아요)[.]?$", ko, re.M)),
        "…": ko.count("…"),
    }
    for loc, checks in STYLE_CHECKS.items():
        joined = "\n".join(texts[loc])
        out[loc] = {"strings": len(texts[loc]),
                    **{name: len(re.findall(p, joined, re.M)) for name, p in checks}}
    return out


# Regex counts behind the per-locale rules in STYLE.md
STYLE_CHECKS = {
    "de-DE": [("du", r"\b[Dd](u|ich|ir|ein\w*)\b"), ("Sie", r"(?<![.!?] )(?<!^)\bSie\b"),
              ("„“", r"„"), ("»«", r"»"), ("…", r"…"), ("...", r"\.\.\."),
              ("konnte nicht", r"konnte\w* nicht"), ("Fehler beim", r"Fehler beim"), ("Bitte", r"\b[Bb]itte\b")],
    "fr-FR": [("vous", r"\b[Vv]ous\b|\b[Vv]otre\b|\b[Vv]os\b"), ("tu", r"\b[Tt]u\b|\b[Tt]on\b|\b[Tt]es\b"),
              ("« »", r"«"), ("“”", r"“"), ("espace avant ? ! : ;", r"[ \u00a0\u202f][?!:;]"), ("sans espace", r"\w[?!;]"),
              ("’", r"’"), ("'", r"\w'\w"), ("…", r"…"), ("...", r"\.\.\."),
              ("Impossible de", r"Impossible de"), ("Échec", r"Échec"), ("Réessayez", r"Réessayez"), ("Veuillez", r"Veuillez")],
    "es-ES": [("tú", r"\b[Tt]us?\b|\b[Pp]uedes\b|\b[Tt]ienes\b"), ("usted", r"\b[Uu]sted\b"),
              ("“”", r"“"), ("« »", r"«"), ("¿", r"¿"), ("? sin ¿", r"^[^¿\n]*\?"), ("…", r"…"), ("...", r"\.\.\."),
              ("No se pudo", r"No se pud"), ("Error al", r"Error al"),
              ("Inténtalo de nuevo", r"[Ii]nténtalo de nuevo"), ("Vuelve a intentarlo", r"[Vv]uelve a intentarlo")],
    "pt-BR": [("você", r"\b[Vv]ocê\b"), ("tu", r"\b[Tt]u\b|\b[Tt]eu\b|\b[Tt]ua\b"), ("“”", r"“"), ('"', r'"'),
              ("…", r"…"), ("...", r"\.\.\."), ("Não foi possível", r"Não foi possível"), ("Falha ao", r"Falha ao"),
              ("Tente novamente", r"[Tt]ente novamente"), ("Por favor", r"[Pp]or favor")],
    "it-IT": [("tu", r"\b[Tt]u[oa]i?\b|\b[Pp]uoi\b"), ("Lei", r"\bLei\b"), ("“”", r"“"), ("« »", r"«"),
              ("’", r"’"), ("'", r"\w'\w"), ("…", r"…"), ("...", r"\.\.\."),
              ("Impossibile", r"Impossibile"), ("Errore durante", r"Errore durante"), ("Riprova", r"Riprova"), ("Per favore", r"[Pp]er favore")],
    "ru": [("вы", r"\b[Вв]ы\b|\b[Вв]аш"), ("ты", r"\b[Тт]ы\b|\b[Тт]во"), ("«»", r"«"), ("„“", r"„"), ("“”", r"“"),
           ("…", r"…"), ("...", r"\.\.\."), ("—", r"—"), ("Не удалось", r"Не удалось"), ("Ошибка", r"Ошибка"),
           ("Пожалуйста", r"[Пп]ожалуйста")],
    "hi-IN": [("आप", r"आप"), ("तुम", r"तुम"), ("।", r"।"), (". sentence end", r"[\u0900-\u097F]\.(\s|$)"), ("“”", r"“"),
              ('"', r'"'), ("…", r"…"), ("...", r"\.\.\."), ("कृपया", r"कृपया")],
}


def write_strings_tsv(corpora):
    DATA.mkdir(exist_ok=True)
    cols = ["source", "key", "en-US", *LOCALES]
    with open(DATA / "strings.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        for source, corpus in corpora:
            for key, en in sorted(corpus["en-US"].items()):
                w.writerow([source, key, *(
                    (corpus.get(loc, {}).get(key) or "").replace("\n", "\\n")
                    for loc in ["en-US", *LOCALES]
                )])


def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def fmt_observed(observed):
    return ", ".join(f"{v} ×{n}" for v, n in observed.items()) or "—"


def write_glossary_md(results, versions):
    lines = [
        "# Claude Glossary",
        "",
        "<!-- Generated by scripts/build.py. Do not edit; change glossary/terms.json instead. -->",
        f"Sources: {versions}",
        "",
        "## Quick reference",
        "",
        "| English | " + " | ".join(LOCALE_NAMES[l] for l in LOCALES) + " | Notes |",
        "|---|" + "---|" * len(LOCALES) + "---|",
    ]
    for r in results:
        lines.append(
            f"| **{md_escape(r['en'])}** | "
            + " | ".join(md_escape(r["recommended"][l]) or "—" for l in LOCALES)
            + f" | {md_escape(r['note'])} |"
        )
    lines += ["", "## Term details", "",
              "“Official usage” counts each candidate translation in official strings whose English source contains the term. "
              "“Untranslated” counts those strings with no official translation. “—” means no official data.", ""]
    current_cat = None
    for r in results:
        if r["category"] != current_cat:
            current_cat = r["category"]
            lines += [f"### {current_cat}", ""]
        lines += [f"#### {r['en']}  `{r['id']}`", ""]
        if r["note"]:
            lines += [r["note"], ""]
        lines += [f"Matches {r['occurrences']} official strings.", "",
                  "| Language | Recommended | Official usage | Untranslated |", "|---|---|---|---|"]
        for l in LOCALES:
            if not r["recommended"][l] and not r["observed"][l]:
                continue
            lines.append(f"| {LOCALE_NAMES[l]} | {md_escape(r['recommended'][l]) or '—'} | "
                         f"{md_escape(fmt_observed(r['observed'][l]))} | {r['untranslated'].get(l, 0)} |")
        if r["examples"]:
            lines += ["", "<details><summary>Official examples</summary>", "",
                      "| en-US | " + " | ".join(LOCALES) + " |", "|---|" + "---|" * len(LOCALES)]
            for ex in r["examples"]:
                lines.append(f"| {md_escape(ex['en-US'])} | "
                             + " | ".join(md_escape(ex[l]) if ex[l] is not None else "*untranslated*" for l in LOCALES)
                             + " |")
            lines += ["", "</details>"]
        lines.append("")
    (ROOT / "GLOSSARY.md").write_text("\n".join(lines), encoding="utf-8")


def write_prompts(results):
    """Write a per-locale terminology snippet to paste into a system prompt."""
    DIST.mkdir(exist_ok=True)
    for l in LOCALES:
        lines = [
            f"<!-- Generated by scripts/build.py: Claude {l} terminology -->",
            f"In {l} UI copy and responses, translate these terms exactly as listed:",
            "",
        ]
        for r in results:
            if not r["recommended"][l]:
                continue
            note = f". {r['note']}" if r["note"] else ""
            lines.append(f"- {r['en']} → {r['recommended'][l]}{note}")
        (DIST / f"prompt.{l}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_skill(results, versions, corpora):
    """Generate references/ and data/ under skills/ and package dist/claude-i18n-style.zip.

    SKILL.md and scripts/ are maintained by hand; references/ and data/ are regenerated.
    Full official strings such as strings.tsv are never packaged.
    """
    variants = {t["id"]: t["variants"] for t in TERMS["terms"]}
    (SKILL / "data").mkdir(parents=True, exist_ok=True)
    glossary = SKILL / "data" / "glossary.json"
    entries = [{**{k: r[k] for k in ("id", "category", "en", "recommended", "note", "observed")},
                "variants": variants[r["id"]], "official_elsewhere": {}} for r in results]
    glossary.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Run lint over the official translations: count uses of each variant where the English
    # source is not the term. Stored as official_elsewhere so lint can downgrade generic words.
    spec = importlib.util.spec_from_file_location("skill_lint", SKILL / "scripts" / "lint.py")
    lint = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lint)
    by_en = {e["en"]: e for e in entries}
    patterns = {t["en"]: re.compile(t["match"], re.I) for t in TERMS["terms"]}
    for l in LOCALES:
        rules, mask = lint.load_rules(l)
        hits = Counter()
        for _, corpus in corpora:
            en = corpus["en-US"]
            for key, text in corpus.get(l, {}).items():
                for issue in lint.lint_text(text, l, rules, mask, style=False):
                    if not patterns[issue["term"]].search(en.get(key, "")):
                        hits[(issue["term"], issue["variant"])] += 1
        for (en, found), n in hits.items():
            by_en[en]["official_elsewhere"].setdefault(l, {})[found] = n
    glossary.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    refs = SKILL / "references"
    refs.mkdir(exist_ok=True)
    for l in LOCALES:
        lines = [
            f"# {LOCALE_NAMES[l]} ({l}) terms",
            "",
            f"Sources: {versions}. “Official count” is how often each translation appears in official {l} strings whose English source contains the term.",
            "",
            "| English | Recommended | Notes | Official count | Official examples |",
            "|---|---|---|---|---|",
        ]
        for r in results:
            examples = [f"{md_escape(ex['en-US'])} → {md_escape(ex[l])}"
                        for ex in r["examples"] if ex[l]][:SKILL_EXAMPLES]
            lines.append(f"| {md_escape(r['en'])} | {md_escape(r['recommended'][l]) or '—'} | {md_escape(r['note'])} | "
                         f"{md_escape(fmt_observed(r['observed'][l]))} | {'<br>'.join(examples)} |")
        (refs / f"terms.{l}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    style = (ROOT / "STYLE.md").read_text(encoding="utf-8")
    style = re.sub(r"\[`?([^\]]+?)`?\]\([^)]+\)", r"\1", style).replace("GLOSSARY.md", "references/terms.<locale>.md").replace(" Raw numbers: data/style-stats.json.", "")
    (refs / "style.md").write_text(style, encoding="utf-8")

    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(DIST / f"{SKILL.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts and f.name != ".DS_Store":
                z.write(f, f.relative_to(SKILL.parent))


def main():
    corpora = load_sources()
    if not corpora:
        raise SystemExit("No data under sources/. Run scripts/extract_desktop.py first.")
    versions = []
    for name, corpus in corpora:
        vf = SOURCES / ("desktop" if name == "desktop" else "web") / "VERSION"
        tag = vf.read_text().strip() if vf.exists() else "unknown"
        versions.append(f"{LABELS[name]} {tag}, {len(corpus['en-US'])} English strings")
    versions = "; ".join(versions)

    results = analyze_terms(corpora)
    stats = style_stats(corpora)
    DATA.mkdir(exist_ok=True)
    (DATA / "glossary.json").write_text(json.dumps(
        [{k: r[k] for k in ("id", "category", "en", "recommended", "note", "occurrences", "observed", "untranslated")}
         for r in results], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA / "style-stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_strings_tsv(corpora)
    write_glossary_md(results, versions)
    write_prompts(results)
    write_skill(results, versions, corpora)
    print(f"Sources: {versions}")
    print(f"{len(results)} terms -> GLOSSARY.md, data/glossary.json, dist/prompt.*.md, skills/")


if __name__ == "__main__":
    main()
