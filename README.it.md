# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · **Italiano** · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Progetto non ufficiale, non affiliato ad Anthropic.

Questa skill fa scrivere all’IA testi di prodotto con la terminologia e il tono dei testi ufficiali di Claude.

Lingue supportate: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Include regole di scrittura per ogni lingua, le traduzioni consigliate di 80 termini principali e uno script di controllo. Ogni regola segue l’uso più frequente nei testi ufficiali di Claude.

Segue la [specifica Agent Skills](https://agentskills.io/specification), quindi funziona con Claude Code, Codex, Cursor e altri agenti compatibili.

Glossario: [GLOSSARY.md](GLOSSARY.md) · Guida di stile: [STYLE.md](STYLE.md)

## Installazione

**Chiedi alla tua IA**

```
Installa la skill claude-i18n-style da https://github.com/cyrus-cai/claude-i18n-style nella tua cartella delle skill.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor e altri strumenti che supportano gli Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Scarica [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Apri Impostazioni → Funzionalità → Competenze, fai clic su “Carica competenza” e scegli il file

**Manualmente**: copia `skills/claude-i18n-style` nella cartella delle skill del tuo agente, ad esempio `~/.claude/skills/` o `~/.codex/skills/`.

## Licenza

[MIT](LICENSE). I testi dell’interfaccia di Claude citati sono di proprietà di Anthropic.
