# claude-i18n-style

**English** · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Unofficial project. Not affiliated with Anthropic.

This skill makes AI write product copy with the same terminology and voice as Claude’s official copy.

Supported languages: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

It includes writing conventions for each language, recommended translations for 80 core terms, and a lint script. Every rule follows the most common usage in Claude’s official copy.

It follows the [Agent Skills specification](https://agentskills.io/specification), so it works with Claude Code, Codex, Cursor and other compatible agents.

Glossary: [GLOSSARY.md](GLOSSARY.md) · Style guide: [STYLE.md](STYLE.md)

## Install

**Ask your AI**

```
Install the claude-i18n-style skill from https://github.com/cyrus-cai/claude-i18n-style into your skills directory.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor and other tools that support Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Download [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Open Settings → Capabilities → Skills, click Upload skill and choose the file

**Manually**: copy `skills/claude-i18n-style` into your agent’s skills directory, such as `~/.claude/skills/` or `~/.codex/skills/`.

## License

[MIT](LICENSE). Quoted Claude UI copy is copyright Anthropic.
