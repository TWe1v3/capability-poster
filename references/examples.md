# Example Prompts

## Canonical `lark-cli` example

Prompt:

```text
$capability-poster https://github.com/larksuite/cli/blob/main/README.zh.md
```

Expected behavior:

- Read the public README
- Group capabilities into 4 functional columns
- Save `poster_data.json`
- Render `poster.html`
- Render `poster.png` if Python Playwright is available

## Non-lark example

Prompt:

```text
$capability-poster https://cli.github.com/manual/ 功能优先
```

Expected behavior:

- Treat GitHub CLI as the subject, not `lark-cli`
- Rebuild the 4 columns around GitHub CLI domains
- Use public URLs only in metadata

## Context-only example

Prompt:

```text
$capability-poster
根据下面这段产品说明生成一张功能速查图，语言用中文，默认比例。
```

Expected behavior:

- Use pasted context as the source
- Infer the title if the user did not specify one
- Leave `snapshot` as a public label such as `Provided context`

## Example `snapshot` values

Good:

- `GitHub · https://github.com/larksuite/cli/blob/main/README.zh.md`
- `Official Docs · https://cli.github.com/manual/`
- `Provided context`

Bad:

- `/Users/name/project/README.md`
- `~/Downloads/internal-notes.md`

