---
name: capability-poster
description: Generate a functional cheatsheet poster from a tool or product URL, README, or pasted context. Use when the user asks for a 功能海报, 功能速查图, capability poster, feature poster, tool cheatsheet poster, or wants a multi-column functional overview image rather than a prose summary.
---

# Capability Poster

Turn a URL or pasted content into a 4-column functional capability poster.

This skill is generic across tools and products, but v1 supports one fixed visual system: a multi-column functional cheatsheet that groups capabilities by domain and renders them to HTML plus PNG when Playwright is available.

## Use This Skill For

- Tool or product docs that should become a visual capability overview
- README pages, docs pages, landing pages, or pasted product descriptions
- CLI or developer-tool capability posters
- Cases where the user wants a shareable image instead of a long text summary

Do **not** use this skill for generic marketing posters, arbitrary infographic styles, or diagrams unrelated to functional capability grouping.

## Input Contract

Supported inputs:

- A URL
- Pasted content or prior conversation context
- Optional style hint: default to `功能优先`
- Optional ratio hint: default to `medium`
- Optional language hint: default to the user's language
- Optional title override: if absent, infer from the source

## Output Contract

Create these files under `output/capability-poster/` relative to the current working directory unless the surrounding task already has a better artifact directory:

- `poster_data.json`
- `poster.html`
- `poster.png` when rendering succeeds

Write the JSON directly. Do **not** generate an intermediate Python or HTML-building script.

## Workflow

1. Read the source.
   - If the user provided a URL, fetch and read it with the available web/browsing tools.
   - If the user provided pasted text or context, use it directly.
2. Normalize the content into the poster schema from [references/schema.md](references/schema.md).
3. Save `poster_data.json`.
4. Render with:

```bash
mkdir -p output/capability-poster
python3 "$CODEX_HOME/skills/capability-poster/scripts/render.py" \
  --data output/capability-poster/poster_data.json \
  --output output/capability-poster/poster.png \
  --ratio medium
```

5. If Python `playwright` is unavailable, keep `poster.html` and tell the user the HTML preview is ready for manual or browser-tool screenshot capture.

## Schema Rules

Use the v1 schema exactly as documented in [references/schema.md](references/schema.md).

Important defaults:

- Keep exactly 4 top-level capability columns when possible.
- Use the fixed color set: `blue`, `green`, `orange`, `purple`.
- Each block should contain:
  - `heading`
  - `summary`
  - `commands[]`
- Prefer short summaries plus command-entry chips over long paragraphs.
- Keep source metadata public-facing. Never expose local filesystem paths.

## Content Guidance

- Group by user-facing capability, not by implementation layer or onboarding phase.
- Make the 4 columns mutually legible:
  - collaboration / communication
  - content / knowledge
  - data / execution
  - platform / agent
- Use command chips or short entry strings for concrete starting points.
- Keep badges compact and high-signal.
- Prefer public URLs in `snapshot`.

## References

- Schema: [references/schema.md](references/schema.md)
- Prompt and content examples: [references/examples.md](references/examples.md)

