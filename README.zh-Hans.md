# claude-i18n-style

[English](README.md) · **简体中文** · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> 非官方项目，与 Anthropic 无关。

本 Skill 让 AI 写产品文案时，使用与 Claude 官方一致的术语和表述风格。

支持的语言：English、简体中文、繁體中文、日本語、한국어、Deutsch、Français、Español、Português (Brasil)、Italiano、Русский、हिन्दी。

包含各语言的书写规范、80 个核心术语的推荐译法和文案检查脚本，规则均取自 Claude 官方文案中最常用的写法。

遵循 [Agent Skills 规范](https://agentskills.io/specification)，可用于 Claude Code、Codex、Cursor 等兼容的智能体。

术语表：[GLOSSARY.md](GLOSSARY.md) · 风格规范：[STYLE.md](STYLE.md)

## 安装

**让 AI 安装**

```
请把 https://github.com/cyrus-cai/claude-i18n-style 中的 claude-i18n-style Skill 安装到你的 Skills 目录。
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex、Cursor 等支持 Agent Skills 的工具**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. 下载 [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. 打开设置 → 功能 → Skills，点击“上传 Skill”，选择该文件

**手动安装**：把 `skills/claude-i18n-style` 复制到智能体的 Skills 目录，例如 `~/.claude/skills/` 或 `~/.codex/skills/`。

## 许可证

[MIT](LICENSE)。引用的 Claude 界面文案版权归 Anthropic 所有。
