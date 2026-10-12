# Style guide

Counts are occurrences in official Claude copy.

## English (en-US)

| Rule | Official usage | Count |
|---|---|---|
| Capitalization | Sentence case for buttons, titles and menus: `Start new chat`, not `Start New Chat` | 8994 : 750 |
| Feature names | Lowercase mid-sentence: project, skill, artifact, connector, plugin, session | project 668 : 11, session 2231 : 30 |
| Product names | Capitalized: Claude Code, Cowork, Remote Control | Claude Code ×535, Cowork ×286 |
| Voice | Address the user as you; rarely use we | 3775 : 271 |
| Contractions | can’t, isn’t, don’t, you’re | 1723 : 292 |
| Errors | `Couldn’t <verb>. Try again.` Avoid Failed to, Unable to and Please | Couldn’t 1834 : Failed to 601 : Unable to 92; Try again 1770 : Please try again 41 |
| Tone | No apologies, no exclamation marks | Sorry / Oops ×4, ! ×38 |
| Sign in | sign in / sign out, not log in | 330 : 18 |
| Apostrophes and quotes | Curly `’` and `“”` | ’ 8117 : ' 148; “ 547 : " 30 |
| Ellipsis | `…` | 654 : 163 |
| Dashes | Spaced em dash: `A — B` | — 791 : ` - ` 10 |
| Lists | Oxford comma: `A, B, and C` | 271 : 63 |

## Simplified Chinese (zh-Hans)

| Rule | Official usage | Count |
|---|---|---|
| Address | 您, not 你 | 8889 : 1 |
| Mixed scripts | Space between Han characters and Latin letters or digits: `在 Claude Code 中打开` | 20449 : 2 |
| Quotes | `“”` | 1443 : 0 ASCII |
| Ellipsis | `…`, including menu items such as `设置…` | 809 : 1 |
| Punctuation | Fullwidth after Han characters: ，。：？ | 9161 : 0 |
| Instructions | 请… | ×6548 |
| Product names | Keep in English, without quotation marks | see references/terms.<locale>.md |
| Placeholders | Keep `{host}`, `{count}` as is, with spaces around them | `主机 {host} 的密钥` |

| Pattern | Form | Example |
|---|---|---|
| Error | `无法 + verb` or `X 失败` | 无法打开该会话。扩展安装失败 |
| Error with retry | `无法 X。请重试。` | 无法收藏项目。请重试。 |
| Button | Verb phrase, no period | 立即重启、重新登录 |
| Confirmation | Ends with a fullwidth question mark | 启用开发者模式？ |
| Create | `新建 X` | 新建对话、新建会话 |
| In progress | `正在 X…` | 正在压缩… |

## Traditional Chinese (zh-Hant)

Same as zh-Hans, except:

| Rule | Official usage | Count |
|---|---|---|
| Address | 您 | 9088 : 2 |
| Mixed scripts | Space between Han characters and Latin letters or digits | 18572 : 0 |
| Quotes | `「」` | 2029 : 0 “” |
| Vocabulary | Taiwan usage: 資料夾、視窗、工作階段、終端機、重新啟動、登入 | |
| Confirmation | `要…嗎？`: `要啟用開發人員模式嗎？` | |

## Japanese (ja-JP)

| Rule | Official usage | Count |
|---|---|---|
| Politeness | です・ます, not だ・である | 10980 : 1 |
| Quotes | `「」` | ×1198 |
| Ellipsis | `…` | ×672 |
| Long vowels | `フォルダ` over `フォルダー` | 584 : 127 |
| Menu items | Noun endings or `〜を開く`: `フォルダを開く…` | |

## Korean (ko-KR)

| Rule | Official usage | Count |
|---|---|---|
| Politeness | `합니다/습니다` in messages | 14104 : 6069 `~요` |
| Buttons | Noun forms: `다시 시작`, `설정` | |
| Instructions | `~하세요` | |
| Loanwords | Official transliterations: 세션, 폴더, 워크트리, 아티팩트 | |

## German (de-DE)

| Rule | Official usage | Count |
|---|---|---|
| Address | du, not Sie | 10779 : 432 |
| Quotes | `„…“` | 1201 : 10 »« |
| Errors | `… konnte nicht …`, not `Fehler beim …` | 1953 : 115 |
| Ellipsis | `…` | 689 : 140 |

## French (fr-FR)

| Rule | Official usage | Count |
|---|---|---|
| Address | vous, not tu | 10687 : 103 |
| Quotes | `« … »` | 647 : 76 “” |
| Spacing | Narrow no-break space before `? ! ; :` | 2679 : 6 |
| Apostrophe | `’` | 13662 : 3619 |
| Errors | `Impossible de …`, then `Réessayez.` | Impossible de 1238 : Échec 522 |
| Ellipsis | `…` | 663 : 156 |

## Spanish (es-ES)

| Rule | Official usage | Count |
|---|---|---|
| Address | tú, not usted | 6832 : 8 |
| Questions | Open with `¿` | 850 : 15 |
| Quotes | `“”` | 522 : 198 « » |
| Errors | `No se pudo …` | 1109 : 356 Error al |
| Retry | `Inténtalo de nuevo` | 915 : 444 Vuelve a intentarlo |
| Ellipsis | `…` | 655 : 162 |

## Portuguese, Brazil (pt-BR)

| Rule | Official usage | Count |
|---|---|---|
| Address | você, not tu | 3091 : 0 |
| Quotes | `“”` | 614 : 42 |
| Errors | `Não foi possível …` | 1726 : 603 Falha ao |
| Retry | `Tente novamente` | ×1390 |
| Ellipsis | `…` | 658 : 159 |

## Italian (it-IT)

| Rule | Official usage | Count |
|---|---|---|
| Address | tu, not Lei | 5616 : 0 |
| Quotes | `“”` | 504 : 126 « » |
| Apostrophe | `’` | 5316 : 1572 |
| Errors | `Impossibile …`, then `Riprova` | 1896 : 13 Errore durante |
| Politeness | Avoid per favore | ×7 |
| Ellipsis | `…` | 661 : 157 |

## Russian (ru)

| Rule | Official usage | Count |
|---|---|---|
| Address | вы, not ты | 4121 : 59 |
| Quotes | `«…»` | 1750 : 4 |
| Dash | `—` | ×1452 |
| Errors | `Не удалось …` | 2557 : 73 Ошибка |
| Ellipsis | `…` | 1125 : 1 |

## Hindi (hi-IN)

| Rule | Official usage | Count |
|---|---|---|
| Address | आप, not तुम | 7825 : 7 |
| Sentence end | `।` | 22213 : 308 |
| Quotes | `“”` | 677 : 54 |
| Loanwords | Product terms are transliterated: सेशन, प्रोजेक्ट, फ़ोल्डर | |
| Ellipsis | `…` | 649 : 167 |

## All languages

- Never translate Claude, Claude Code, Cowork, MCP, model names such as Opus, Sonnet and Haiku, file names or commands.
- Menu items that open a dialog end with `…`.
