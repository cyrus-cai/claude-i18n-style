# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · **Português (Brasil)** · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Projeto não oficial, sem relação com a Anthropic.

Esta habilidade faz a IA escrever textos de produto com a terminologia e o tom dos textos oficiais do Claude.

Idiomas compatíveis: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Inclui regras de escrita para cada idioma, traduções recomendadas de 80 termos principais e um script de verificação. Cada regra segue o uso mais frequente nos textos oficiais do Claude.

Segue a [especificação de Agent Skills](https://agentskills.io/specification), então funciona com Claude Code, Codex, Cursor e outros agentes compatíveis.

Glossário: [GLOSSARY.md](GLOSSARY.md) · Guia de estilo: [STYLE.md](STYLE.md)

## Instalação

**Peça à sua IA**

```
Instale a habilidade claude-i18n-style de https://github.com/cyrus-cai/claude-i18n-style na sua pasta de habilidades.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor e outras ferramentas compatíveis com Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Baixe [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Abra Configurações → Recursos → Habilidades, clique em “Fazer upload de habilidade” e escolha o arquivo

**Manualmente**: copie `skills/claude-i18n-style` para a pasta de habilidades do seu agente, por exemplo `~/.claude/skills/` ou `~/.codex/skills/`.

## Licença

[MIT](LICENSE). Os textos de interface do Claude citados são de propriedade da Anthropic.
