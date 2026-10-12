#!/usr/bin/env python3
"""Check copy against Claude's official terminology and writing style.

Usage:
  python3 lint.py --locale zh-Hans FILE [FILE ...]
  echo "你可以在Claude Code里打开聊天" | python3 lint.py --locale zh-Hans -
  python3 lint.py --locale en-US README.md                  # English: style checks only
  python3 lint.py --locale zh-Hans --json locales/zh.json   # i18n JSON: checks each string value

Findings are candidates to review in context: many variants are also ordinary words.
No third-party dependencies.
"""
import argparse
import json
import re
import sys
from pathlib import Path

GLOSSARY = Path(__file__).resolve().parent.parent / "data" / "glossary.json"
# A variant used at least GENERIC_MIN times elsewhere in official copy, and GENERIC_RATIO times
# more than in the term's own context, is treated as a generic word and reported as low confidence
GENERIC_MIN = 10
GENERIC_RATIO = 3
HAN = r"一-鿿"
# Locales without word spacing match variants as substrings; the rest match case-insensitively
# at the start of a word, so stems such as "сесси" cover every inflection
CJK = {"zh-Hans", "zh-Hant", "ja-JP", "ko-KR"}
WORD_START = r"(?<![\w\u0900-\u097F])"


# Names that contain glossary words but are never translated
PROTECTED = {"Agent Skills", "Agent Skill"}


def pattern(words, locale):
    alt = "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))
    return re.compile(f"(?:{alt})" if locale in CJK else f"{WORD_START}(?:{alt})", 0 if locale in CJK else re.I)
LATIN = r"A-Za-z0-9"


def recommended_forms(rec):
    """Split “无痕模式（incognito chat → 无痕对话）” into ['无痕模式', '无痕对话']."""
    if not rec:
        return []
    head, _, tail = rec.partition("（")
    forms = [p.strip() for p in head.split(" / ") if p.strip()]
    forms += [m.strip() for m in re.findall(r"→\s*([^；）]+)", tail)]
    return forms


def load_rules(locale):
    terms = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    fold = (lambda x: x) if locale in CJK else str.lower
    allowed = set()
    for t in terms:
        allowed.update(recommended_forms(t["recommended"].get(locale)))
    allowed |= PROTECTED
    allowed_folded = {fold(a) for a in allowed}
    rules = []
    for t in terms:
        forms = recommended_forms(t["recommended"].get(locale))
        if not forms:
            continue
        bad = [v for v in t["variants"].get(locale, [])
               if fold(v) not in allowed_folded and not any(fold(v) in fold(f) for f in forms)]
        if bad:
            elsewhere = t.get("official_elsewhere", {}).get(locale, {})
            rules.append({"term": t, "forms": forms, "elsewhere": elsewhere,
                          "bad": [(v, pattern([v], locale)) for v in sorted(bad, key=len, reverse=True)]})
    # Mask every recommended form first so substrings of them aren't flagged
    mask = pattern(allowed, locale) if allowed else None
    return rules, mask


STYLE_RULES = {
    "zh-Hans": [
        (r"你(?!们)", "Address the user as 您, not 你 (8889 : 1)"),
        (rf"[{HAN}][{LATIN}]|[{LATIN}][{HAN}]", "Put a space between Han characters and Latin letters or digits (20449 : 2)"),
        (rf'[{HAN}]"|"[{HAN}]', "Use Chinese curly quotes “”"),
        (r"\.\.\.", "Use the ellipsis character …"),
        (rf"[{HAN}][,:;?!]", "Use fullwidth punctuation after Han characters: ，：；？！"),
    ],
    "zh-Hant": [
        (r"你(?!們)", "Address the user as 您, not 你 (9088 : 2)"),
        (rf"[{HAN}][{LATIN}]|[{LATIN}][{HAN}]", "Put a space between Han characters and Latin letters or digits (18572 : 0)"),
        (r"[“”]", "Use corner brackets 「」 for quotes"),
        (rf'[{HAN}]"|"[{HAN}]', "Use corner brackets 「」 for quotes"),
        (r"\.\.\.", "Use the ellipsis character …"),
        (rf"[{HAN}][,:;?!]", "Use fullwidth punctuation after Han characters"),
    ],
    "ja-JP": [
        (r"(だ|である)。?$", "Use the polite です・ます form (10980 : 1)"),
        (r"\.\.\.", "Use the ellipsis character …"),
        (r'[぀-ヿ一-鿿]"', "Use 「」 for quotes"),
    ],
    "ko-KR": [
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "de-DE": [
        (r"(?<![.!?:] )(?<!^)(?<!„)\bSie\b", "Address the user as du (10779 : 432)"),
        (r"(?<!\S)[“\"](?=\w)", "Use German quotes „…“"),
        (r"\bFehler beim\b", "Write errors as “… konnte nicht …” (1953 : 115)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "fr-FR": [
        (r"\b[Tt]u\b", "Address the user as vous (10687 : 103)"),
        (r"[“\"](?=\w)", "Use French quotes « … » (647 : 76)"),
        (r"\w[?!;:](?=\s|$)", "Put a narrow no-break space before ? ! ; : (2679 : 6)"),
        (r"\w'\w", "Use the curly apostrophe ’ (13662 : 3619)"),
        (r"\bÉchec (de|du|des|lors)\b", "Write errors as “Impossible de …” (1238 : 522)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "es-ES": [
        (r"\b[Uu]sted(es)?\b", "Address the user as tú (6832 : 8)"),
        (r"^[^¿\n]*\?", "Open questions with ¿ (850 : 15)"),
        (r"\bError al\b", "Write errors as “No se pudo …” (1109 : 356)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "pt-BR": [
        (r"\b[Tt]u\b|\b[Tt]eu\b|\b[Tt]ua\b", "Address the user as você (3091 : 0)"),
        (r"\bFalha ao\b", "Write errors as “Não foi possível …” (1726 : 603)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "it-IT": [
        (r"\bLei\b", "Address the user as tu (5616 : 0)"),
        (r"\w'\w", "Use the curly apostrophe ’ (5316 : 1572)"),
        (r"\b[Pp]er favore\b", "Avoid “per favore” (7 uses)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "ru": [
        (r"\b[Тт]ы\b|\b[Тт]в(ой|оя|оё|ое|ои|оего|оей|оих)\b", "Address the user as вы (4121 : 59)"),
        (r"[“\"„](?=\w)", "Use guillemets «…» (1750 : 4)"),
        (r"\bОшибка\b", "Write errors as “Не удалось …” (2557 : 73)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "hi-IN": [
        (r"तुम", "Address the user as आप (7825 : 7)"),
        (r"[ऀ-ॿ]\.(?=\s|$)", "End sentences with । (22213 : 308)"),
        (r"\.\.\.", "Use the ellipsis character …"),
    ],
    "en-US": [
        (r"(?<=[a-z,] )(?<!Agent )(Projects?|Skills?|Artifacts?|Connectors?|Plugins?|Sessions?)\b",
         "Feature names are lowercase mid-sentence (project 668 : 11)"),
        (r"\b(cannot|[Dd]o not|does not|is not|are not|you are)\b", "Use contractions: can’t, don’t, isn’t (1723 : 292)"),
        (r"\b(Failed to|Unable to|Could not)\b", "Write errors as “Couldn’t …” (1834 : 693)"),
        (r"\b[Pp]lease try again", "Write “Try again.” without please (1770 : 41)"),
        (r"\b(Sorry|sorry|Oops)\b", "Don’t apologize in UI copy"),
        (r"\w!(?=\s|$)", "Avoid exclamation marks"),
        (r"\b[Ll]og (in|out)\b", "Use sign in / sign out (330 : 18)"),
        (r"\w'\w", "Use the curly apostrophe ’ (8117 : 148)"),
        (r'"[^"]+"', "Use curly quotes “” (547 : 30)"),
        (r"\.\.\.", "Use the ellipsis character … (U+2026)"),
        (r" - ", "Use a spaced em dash — (791 : 10)"),
    ],
}

# For the Title Case check: words that are capitalized anyway and don't indicate Title Case
SMALL_WORDS = {"a", "an", "the", "and", "or", "to", "of", "in", "on", "for", "with", "by", "at", "from", "as", "is"}
PROPER = {"Claude", "Code", "Cowork", "Remote", "Control", "Desktop", "MCP", "API", "Opus", "Sonnet", "Haiku",
          "Chrome", "Mac", "Windows", "Google", "GitHub", "Slack", "Anthropic", "I"}


def title_case(line):
    """Return True for a short title or button written in Title Case. Official copy uses sentence case, 8994 : 750."""
    text = re.sub(r"^\s*(#+|[-*]|\d+\.)\s+", "", line).strip()
    words = text.split()
    if not 2 <= len(words) <= 6 or not re.fullmatch(r"[A-Za-z][A-Za-z ’'-]*", text):
        return False
    rest = [w for w in words[1:] if w.lower() not in SMALL_WORDS]
    return bool(rest) and all(w[0].isupper() for w in rest) and any(w not in PROPER for w in rest)


def note_applies(note, locale):
    """Show a term note unless it only talks about other locales."""
    codes = re.findall(r"\b(?:zh-Hans|zh-Hant|ja-JP|ko-KR|de-DE|fr-FR|es-ES|pt-BR|it-IT|ru|hi-IN)\b", note or "")
    return bool(note) and (not codes or locale in codes)


def strip_code(line):
    """Blank out `inline code` and URLs with spaces, keeping column numbers."""
    return re.sub(r"`[^`]*`|https?://\S+?(?=[)\s]|$)", lambda m: " " * len(m.group()), line)


def lint_text(text, locale, rules, mask, where="", style=True):
    issues = []
    in_fence = False
    for lineno, raw in enumerate(text.splitlines(), 1):
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = strip_code(raw)
        # Treat {placeholders} as Latin words: they take spaces like words and their names aren't terms
        line = re.sub(r"\{\w+\}", lambda m: "X" * len(m.group()), line)
        masked = mask.sub(lambda m: "\0" * len(m.group()), line) if mask else line
        for r in rules:
            for v, vp in r["bad"]:
                for m in vp.finditer(masked):
                    t = r["term"]
                    n = r["elsewhere"].get(v, 0)
                    generic = n >= GENERIC_MIN and n >= GENERIC_RATIO * t["observed"].get(locale, {}).get(v, 0)
                    forms = " / ".join(r["forms"])
                    msg = f"Official translation of {t['en']}: “{forms}”" + (f". {t['note'].rstrip('.')}" if note_applies(t["note"], locale) else "")
                    if generic:
                        msg += f". Official copy also uses “{v}” {n} times elsewhere, likely a generic word"
                    elif n >= GENERIC_MIN:
                        msg += f". Official copy also uses “{v}” {n} times elsewhere; check this refers to {t['en']}"
                    issues.append({
                        "where": where, "line": lineno, "col": m.start() + 1, "kind": "term",
                        "confidence": "low" if generic else "high",
                        "found": m.group(), "variant": v, "suggest": " / ".join(r["forms"]), "term": t["en"], "message": msg,
                        "context": raw.strip(),
                    })
                masked = vp.sub(lambda m: "\0" * len(m.group()), masked)
        if style and locale == "en-US" and title_case(line):
            issues.append({"where": where, "line": lineno, "col": 1, "kind": "style", "confidence": "high",
                           "found": line.strip(), "message": "Use sentence case for titles and buttons (8994 : 750)",
                           "context": raw.strip()})
        for pattern, msg in STYLE_RULES.get(locale, []) if style else []:
            for m in re.finditer(pattern, line, re.M):
                issues.append({"where": where, "line": lineno, "col": m.start() + 1, "kind": "style", "confidence": "high",
                               "found": m.group(), "message": msg, "context": raw.strip()})
    return issues


def iter_json_strings(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from iter_json_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from iter_json_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    locales = ["en-US", *json.loads(GLOSSARY.read_text(encoding="utf-8"))[0]["recommended"]]
    ap.add_argument("--locale", required=True, choices=locales)
    ap.add_argument("--json", action="store_true", help="print results as JSON")
    ap.add_argument("--no-style", action="store_true", help="check terms only, skip style rules")
    ap.add_argument("--all", action="store_true", help="also list low-confidence hits on words official copy commonly uses elsewhere")
    ap.add_argument("files", nargs="+", help="files to check; - reads stdin; .json files are checked value by value")
    args = ap.parse_args()

    rules, mask = load_rules(args.locale)
    issues = []
    for f in args.files:
        if f == "-":
            issues += lint_text(sys.stdin.read(), args.locale, rules, mask, "<stdin>", not args.no_style)
            continue
        content = Path(f).read_text(encoding="utf-8")
        if f.endswith(".json"):
            for key, value in iter_json_strings(json.loads(content)):
                issues += lint_text(value, args.locale, rules, mask, f"{f}#{key}", not args.no_style)
        else:
            issues += lint_text(content, args.locale, rules, mask, f, not args.no_style)

    low = [i for i in issues if i["confidence"] == "low"]
    shown = issues if args.all else [i for i in issues if i["confidence"] == "high"]
    if args.json:
        print(json.dumps(shown, ensure_ascii=False, indent=2))
    else:
        for i in shown:
            loc = f"{i['where']} (col {i['col']})" if "#" in i["where"] else f"{i['where']}:{i['line']}:{i['col']}"
            tag = i["kind"] if i["confidence"] == "high" else "term?"
            print(f"[{tag}] {loc}  「{i['found']}」 {i['message']}\n    {i['context']}")
        terms = sum(i["kind"] == "term" for i in shown)
        print(f"\n{len(shown)} possible issues: {terms} terminology, {len(shown) - terms} style. Review terminology hits in context.")
        if low and not args.all:
            print(f"{len(low)} more low-confidence terminology hits; use --all to show them.")
    sys.exit(1 if shown else 0)


if __name__ == "__main__":
    main()
