# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · **Français** · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Projet non officiel, sans lien avec Anthropic.

Cette compétence permet à l’IA de rédiger des textes produit avec la terminologie et le ton des textes officiels de Claude.

Langues prises en charge : English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Il comprend des règles de rédaction pour chaque langue, les traductions recommandées de 80 termes clés et un script de vérification. Chaque règle suit l’usage le plus fréquent dans les textes officiels de Claude.

Elle suit la [spécification Agent Skills](https://agentskills.io/specification) et fonctionne avec Claude Code, Codex, Cursor et les autres agents compatibles.

Glossaire : [GLOSSARY.md](GLOSSARY.md) · Guide de style : [STYLE.md](STYLE.md)

## Installation

**Demandez à votre IA**

```
Installez la compétence claude-i18n-style depuis https://github.com/cyrus-cai/claude-i18n-style dans votre dossier de compétences.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor et les autres outils compatibles avec les Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Téléchargez [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Ouvrez Paramètres → Capacités → Compétences, cliquez sur « Importer une compétence » et choisissez le fichier

**Manuellement** : copiez `skills/claude-i18n-style` dans le dossier des compétences de votre agent, par exemple `~/.claude/skills/` ou `~/.codex/skills/`.

## Licence

[MIT](LICENSE). Les textes d’interface de Claude cités sont la propriété d’Anthropic.
