---
name: claude-i18n-style
description: Write, translate and review product copy with the terminology and voice of Claude's official copy, in English, Simplified and Traditional Chinese, Japanese, Korean, German, French, Spanish, Brazilian Portuguese, Italian, Russian and Hindi. Use when writing or localizing UI strings, i18n JSON files, docs, release notes or help content for an AI product; when translating terms such as session, chat, agent, skill, artifact, plan or usage; or when the user asks to match Claude's wording or check copy for terminology and style issues. Unofficial; not affiliated with Anthropic.
---

# Claude copy terminology and style

> Unofficial skill, not affiliated with Anthropic.

Two parts: writing conventions for each language, and recommended translations of 80 core terms. Each rule lists how often official Claude copy uses it. This skill covers terminology and house style only; grammar and general translation quality are assumed.

## Files

| File | Contents | When to read |
|---|---|---|
| [style.md](references/style.md) | Writing conventions per language | Every time; read the section for the target language |
| `references/terms.<locale>.md`, e.g. [terms.zh-Hans.md](references/terms.zh-Hans.md) | Recommended translations, official counts, examples | When writing or translating non-English copy |
| [glossary.json](data/glossary.json) | Machine-readable glossary | For programmatic use |
| [lint.py](scripts/lint.py) | Terminology and style checks | Before delivering, or when reviewing existing copy |

Locales: `en-US`, `zh-Hans`, `zh-Hant`, `ja-JP`, `ko-KR`, `de-DE`, `fr-FR`, `es-ES`, `pt-BR`, `it-IT`, `ru`, `hi-IN`.

## Writing English

1. Read the English section of [style.md](references/style.md). Key rules:
   - Sentence case for buttons, titles and menus: `New chat`
   - Capitalize product names such as Claude Code and Cowork; lowercase feature names such as project, skill and artifact mid-sentence
   - Address the user as you; use contractions; no apologies or exclamation marks
   - Errors: `Couldn’t <verb> <object>. Try again.`
   - Curly `’` and `“”`, ellipsis `…`, spaced em dash ` — `
2. Run `python3 scripts/lint.py --locale en-US <file>` before delivering.

## Writing or translating other languages

1. Read `references/terms.<locale>.md` and the matching section of [style.md](references/style.md).
2. Use the recommended translation for every listed term. Keep product names such as Claude Code, Cowork and MCP in English.
3. For terms not in the glossary, follow the style of related terms and the target language’s common usage. Never invent translations for product names.
4. Run lint before delivering.

## Reviewing

```bash
python3 scripts/lint.py --locale zh-Hans path/to/file.md
python3 scripts/lint.py --locale de-DE locales/de.json
echo "text" | python3 scripts/lint.py --locale fr-FR -
```

`.json` files are checked value by value. Options: `--json` for machine-readable output, `--no-style` for terminology only, `--all` to include low-confidence hits. Code blocks and inline code are skipped.

Lint reports possible issues. Judge each in context:

- Words official copy also uses widely in other senses are low confidence and hidden by default.
- Words with two common meanings are still reported, with a prompt to confirm the meaning.
- If the word refers to the term’s concept, change it to the recommended translation.
- If it is ordinary usage, keep it and tell the user why.
- If the term note says the translation depends on context, follow the note.

When reporting to the user, list what changed, the official counts behind each change, and what was kept on purpose.

## Data coverage

- Every language draws on about 35,000 official strings from Claude Desktop and claude.ai.
- When a term has no recommendation for a locale, shown as “—”, don’t claim an official translation exists.
- Where official copy is inconsistent, the term note gives the split and the recommendation follows the majority.
- Data versions are in the header of each `references/terms.<locale>.md`.
