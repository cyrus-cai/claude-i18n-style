# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · **한국어** · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> 비공식 프로젝트이며 Anthropic과 관련이 없습니다.

이 Skill을 사용하면 AI가 제품 문구를 작성할 때 Claude 공식 문구와 같은 용어와 표현 스타일을 사용합니다.

지원 언어: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी.

언어별 작성 규칙, 핵심 용어 80개의 권장 번역, 문구 검사 스크립트가 포함되어 있습니다. 모든 규칙은 Claude 공식 문구에서 가장 많이 쓰인 표기를 기준으로 합니다.

[Agent Skills 사양](https://agentskills.io/specification)을 따르므로 Claude Code, Codex, Cursor 등 호환 에이전트에서 사용할 수 있습니다.

용어집: [GLOSSARY.md](GLOSSARY.md) · 스타일 가이드: [STYLE.md](STYLE.md)

## 설치

**AI에게 요청**

```
https://github.com/cyrus-cai/claude-i18n-style 의 claude-i18n-style Skill을 Skills 디렉터리에 설치해 주세요.
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor 등 Agent Skills를 지원하는 도구**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. 다운로드: [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. 설정 → 기능 → Skills를 열고 Skill 업로드를 클릭한 뒤 파일을 선택합니다

**수동 설치**: `skills/claude-i18n-style`을 에이전트의 Skills 디렉터리(예: `~/.claude/skills/`, `~/.codex/skills/`)에 복사합니다.

## 라이선스

[MIT](LICENSE). 인용된 Claude UI 문구의 저작권은 Anthropic에 있습니다.
