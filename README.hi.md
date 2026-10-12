# claude-i18n-style

[English](README.md) · [简体中文](README.zh-Hans.md) · [繁體中文](README.zh-Hant.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · **हिन्दी**

> अनौपचारिक प्रोजेक्ट, Anthropic से संबद्ध नहीं।

यह स्किल AI को प्रोडक्ट टेक्स्ट Claude के आधिकारिक टेक्स्ट जैसी शब्दावली और स्टाइल में लिखने में मदद करता है।

समर्थित भाषाएं: English, 简体中文, 繁體中文, 日本語, 한국어, Deutsch, Français, Español, Português (Brasil), Italiano, Русский, हिन्दी।

इसमें हर भाषा के लेखन नियम, 80 मुख्य शब्दों के सुझाए गए अनुवाद और एक जांच स्क्रिप्ट शामिल हैं। हर नियम Claude के आधिकारिक टेक्स्ट में सबसे अधिक इस्तेमाल होने वाले रूप पर आधारित है।

यह [Agent Skills स्पेसिफ़िकेशन](https://agentskills.io/specification) का पालन करता है, इसलिए Claude Code, Codex, Cursor और अन्य संगत एजेंट के साथ काम करता है।

शब्दावली: [GLOSSARY.md](GLOSSARY.md) · स्टाइल गाइड: [STYLE.md](STYLE.md)

## इंस्टॉल करें

**अपने AI से कहें**

```
https://github.com/cyrus-cai/claude-i18n-style से claude-i18n-style स्किल को अपनी स्किल्स डायरेक्टरी में इंस्टॉल करें।
```

**Claude Code**

```
/plugin marketplace add cyrus-cai/claude-i18n-style
/plugin install claude-i18n-style@claude-i18n-style
```

**Codex, Cursor और Agent Skills को सपोर्ट करने वाले अन्य टूल**

```bash
npx skills add https://github.com/cyrus-cai/claude-i18n-style
```

**claude.ai / Claude Desktop**

1. डाउनलोड करें: [claude-i18n-style.zip](https://github.com/cyrus-cai/claude-i18n-style/releases/latest/download/claude-i18n-style.zip)
2. सेटिंग्स → क्षमताएं → Skills खोलें, “कौशल अपलोड करें” पर क्लिक करें और फ़ाइल चुनें

**मैन्युअल रूप से**: `skills/claude-i18n-style` को अपने एजेंट की स्किल्स डायरेक्टरी में कॉपी करें, जैसे `~/.claude/skills/` या `~/.codex/skills/`।

## लाइसेंस

[MIT](LICENSE)। उद्धृत Claude UI टेक्स्ट का कॉपीराइट Anthropic के पास है।
