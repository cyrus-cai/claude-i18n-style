# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · **Deutsch** · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Inoffizielles Projekt, nicht mit Anthropic verbunden.

Mit diesem Skill schreibt KI Produkttexte in der Terminologie und im Ton der offiziellen Claude-Texte.

Unterstützte Sprachen: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Enthalten sind Schreibregeln für jede Sprache, empfohlene Übersetzungen für 80 Kernbegriffe und ein Prüfskript. Jede Regel folgt der häufigsten Verwendung in den offiziellen Claude-Texten.

Der Skill folgt der [Agent-Skills-Spezifikation](https://agentskills.io/specification) und funktioniert mit Claude Code, Codex, Cursor und anderen kompatiblen Agenten.

Glossar: [GLOSSARY.md](GLOSSARY.md) · Styleguide: [STYLE.md](STYLE.md)

## Installation

**Frag deine KI**

```
Installiere den Skill claude-i18n-style aus https://github.com/cyrus-cai/claude-i18n-style in dein Skills-Verzeichnis.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor und andere Tools mit Unterstützung für Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Lade [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip) herunter
2. Öffne Einstellungen → Funktionen → Skills, klicke auf „Skill hochladen“ und wähle die Datei aus

**Manuell**: Kopiere `skills/claude-i18n-style` in das Skills-Verzeichnis deines Agenten, etwa `~/.claude/skills/` oder `~/.codex/skills/`.

## Lizenz

[MIT](LICENSE). Zitierte Claude-UI-Texte unterliegen dem Urheberrecht von Anthropic.
