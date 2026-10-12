# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · **Русский** · [हिन्दी](README.hi.md)

> Неофициальный проект, не связан с Anthropic.

С этим Skill ИИ пишет тексты продукта в терминологии и тоне официальных текстов Claude.

Поддерживаемые языки: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Включает правила написания для каждого языка, рекомендуемые переводы 80 ключевых терминов и скрипт проверки. Каждое правило соответствует самому частому варианту в официальных текстах Claude.

Соответствует [спецификации Agent Skills](https://agentskills.io/specification), поэтому работает с Claude Code, Codex, Cursor и другими совместимыми агентами.

Глоссарий: [GLOSSARY.md](GLOSSARY.md) · Руководство по стилю: [STYLE.md](STYLE.md)

## Установка

**Попросите ИИ**

```
Установите Skill claude-i18n-style из https://github.com/cyrus-cai/claude-i18n-style в вашу папку Skills.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor и другие инструменты с поддержкой Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Скачайте [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Откройте Настройки → Возможности → Skills, нажмите «Загрузить Skill» и выберите файл

**Вручную**: скопируйте `skills/claude-i18n-style` в папку Skills вашего агента, например `~/.claude/skills/` или `~/.codex/skills/`.

## Лицензия

[MIT](LICENSE). Цитируемые тексты интерфейса Claude принадлежат Anthropic.
