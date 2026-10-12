# claude.ai strings

claude.ai has about 34,000 strings per language. Download them into this directory by hand.

## Download

The site is behind Cloudflare, so `curl` gets a 403. Open each link in a browser signed in to claude.ai and save the file here under the name shown.

| Language | Link | Save as |
|---|---|---|
| English | https://claude.ai/i18n/en-US.json | `en-US.json` |
| 简体中文 | https://claude.ai/i18n/zh-Hans.json | `zh-Hans.json` |
| 繁體中文 | https://claude.ai/i18n/zh-Hant.json | `zh-Hant.json` |
| 日本語 | https://claude.ai/i18n/ja-JP.json | `ja-JP.json` |
| 한국어 | https://claude.ai/i18n/ko-KR.json | `ko-KR.json` |
| Deutsch | https://claude.ai/i18n/de-DE.json | `de-DE.json` |
| Français | https://claude.ai/i18n/fr-FR.json | `fr-FR.json` |
| Español | https://claude.ai/i18n/es-ES.json | `es-ES.json` |
| Português (Brasil) | https://claude.ai/i18n/pt-BR.json | `pt-BR.json` |
| Italiano | https://claude.ai/i18n/it-IT.json | `it-IT.json` |
| Русский | https://claude.ai/i18n/ru.json | `ru.json` |
| हिन्दी | https://claude.ai/i18n/hi-IN.json | `hi-IN.json` |

Write the download date to `VERSION`, for example `2026-10-12`, then run `python3 scripts/build.py`.

## Other languages

claude.ai serves the same 43 languages as `sources/desktop/`, at `https://claude.ai/i18n/<locale>.json` with the desktop file name as the locale, for example `vi`, `th` or `tr`. Adding a language to the glossary also needs its candidate translations in `glossary/terms.json`.

Optional dynamic strings, English only: https://claude.ai/i18n/dynamic/en-US.json, saved as `dynamic/en-US.json`.
