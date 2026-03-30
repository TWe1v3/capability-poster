# capability-poster

Local Codex skill for turning a tool or product document into a multi-column functional capability poster.

## What it does

- Reads a public URL or pasted content
- Normalizes it into a fixed functional poster schema
- Produces `poster_data.json`
- Renders `poster.html`
- Tries to render `poster.png`

## Default install location

Install under:

- `$CODEX_HOME/skills/capability-poster`
- or `~/.codex/skills/capability-poster` when `CODEX_HOME` is unset

## Example prompts

```text
$capability-poster https://github.com/larksuite/cli/blob/main/README.zh.md
$capability-poster https://cli.github.com/manual/ capability poster
$capability-poster https://example.com/docs 功能优先 16:9
$capability-poster
根据上下文生成一张功能速查海报
```

## Expected outputs

Default output directory:

```text
output/capability-poster/
  poster_data.json
  poster.html
  poster.png
```

## Swapping the template

The default template is:

```text
assets/template-functional-v2.html
```

To change the visual system:

1. Keep the v1 JSON schema stable.
2. Replace the HTML/CSS/JS in the template.
3. Keep the `__POSTER_DATA__` placeholder in the template.
4. Re-run the renderer against a known example JSON.

## Rendering fallback

`scripts/render.py` always writes the HTML preview first.

If Python `playwright` is unavailable:

- the script keeps `poster.html`
- prints a fallback message
- does not fail as long as the HTML preview was generated

That HTML can then be screenshotted manually or with browser automation tools.

