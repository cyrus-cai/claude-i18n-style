# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · **Español** · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> Proyecto no oficial, sin relación con Anthropic.

Esta habilidad hace que la IA escriba textos de producto con la terminología y el tono de los textos oficiales de Claude.

Idiomas compatibles: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

Incluye normas de redacción para cada idioma, traducciones recomendadas de 80 términos clave y un script de revisión. Cada norma sigue el uso más frecuente en los textos oficiales de Claude.

Sigue la [especificación de Agent Skills](https://agentskills.io/specification), así que funciona con Claude Code, Codex, Cursor y otros agentes compatibles.

Glosario: [GLOSSARY.md](GLOSSARY.md) · Guía de estilo: [STYLE.md](STYLE.md)

## Instalación

**Pídeselo a tu IA**

```
Instala la habilidad claude-i18n-style de https://github.com/cyrus-cai/claude-i18n-style en tu carpeta de habilidades.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor y otras herramientas compatibles con Agent Skills**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. Descarga [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. Abre Configuración → Capacidades → Skills, haz clic en “Subir habilidad” y elige el archivo

**Manualmente**: copia `skills/claude-i18n-style` en la carpeta de habilidades de tu agente, por ejemplo `~/.claude/skills/` o `~/.codex/skills/`.

## Licencia

[MIT](LICENSE). Los textos de interfaz de Claude citados son propiedad de Anthropic.
