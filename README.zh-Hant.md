# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · **繁體中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> 非官方專案，與 Anthropic 無關。

本 Skill 讓 AI 撰寫產品文案時，使用與 Claude 官方一致的術語和表述風格。

支援的語言：English、简体中文、繁體中文、日本語、한국어、Deutsch、Français、Español、Português (Brasil)、Italiano、Русский、हिन्दी。

包含各語言的書寫規範、80 個核心術語的建議譯法和文案檢查指令碼，規則均取自 Claude 官方文案中最常用的寫法。

遵循 [Agent Skills 規範](https://agentskills.io/specification)，可用於 Claude Code、Codex、Cursor 等相容的代理程式。

術語表：[GLOSSARY.md](GLOSSARY.md) · 風格規範：[STYLE.md](STYLE.md)

## 安裝

**請 AI 安裝**

```
請將 https://github.com/cyrus-cai/claude-i18n-style 中的 claude-i18n-style Skill 安裝到你的 Skills 目錄。
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex、Cursor 等支援 Agent Skills 的工具**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. 下載 [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. 開啟設定 → 功能 → Skills，點選「上傳 Skill」，選擇該檔案

**手動安裝**：將 `skills/claude-i18n-style` 複製到代理程式的 Skills 目錄，例如 `~/.claude/skills/` 或 `~/.codex/skills/`。

## 授權

[MIT](LICENSE)。引用的 Claude 介面文案著作權歸 Anthropic 所有。
