# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · **日本語** · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md)

> 非公式プロジェクトです。Anthropic とは関係ありません。

この Skill を使うと、AI がプロダクトの文章を書くときに Claude 公式と同じ用語と表現スタイルを使います。

対応言語：English、简体中文、繁體中文、日本語、한국어、Deutsch、Français、Español、Português (Brasil)、Italiano、Русский、हिन्दी。

各言語の表記ルール、80 個の主要用語の推奨訳、文章チェック用スクリプトを含みます。ルールはすべて Claude 公式の文言で最も多く使われている表記に基づいています。

[Agent Skills 仕様](https://agentskills.io/specification)に準拠しているため、Claude Code、Codex、Cursor などの対応エージェントで使えます。

用語集：[GLOSSARY.md](GLOSSARY.md) · スタイルガイド：[STYLE.md](STYLE.md)

## インストール

**AI に依頼**

```
https://github.com/cyrus-cai/claude-i18n-style の claude-i18n-style Skill を Skills ディレクトリにインストールしてください。
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex、Cursor など Agent Skills に対応したツール**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. ダウンロード：[claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. 設定 → 機能 → Skills を開き、「Skills をアップロード」をクリックしてファイルを選択します

**手動インストール**：`skills/claude-i18n-style` をエージェントの Skills ディレクトリ（`~/.claude/skills/` や `~/.codex/skills/` など）にコピーします。

## ライセンス

[MIT](LICENSE)。引用している Claude の UI 文言の著作権は Anthropic に帰属します。
