# Capability Poster v1 Schema

Use one fixed schema for v1. Do not invent alternate layouts.

## Top-level shape

```json
{
  "source": "PUBLIC SOURCE LABEL",
  "title": "Poster title",
  "subtitle": "One-sentence positioning text",
  "snapshot": "Public URL or public source string only",
  "badges": ["Badge 1", "Badge 2", "Badge 3"],
  "ribbon": [
    { "title": "Group 1", "text": "service-a · service-b" },
    { "title": "Group 2", "text": "service-c · service-d" },
    { "title": "Group 3", "text": "service-e · service-f" },
    { "title": "Group 4", "text": "service-g · service-h" }
  ],
  "columns": [
    {
      "color": "blue",
      "title": "Column title",
      "blocks": [
        {
          "heading": "Block heading",
          "summary": "One short capability summary.",
          "commands": ["+foo", "+bar", "api GET /..."]
        }
      ]
    }
  ],
  "footerGroups": [
    { "label": "ENV VARS", "items": ["A", "B"] },
    { "label": "GLOBAL FLAGS", "items": ["--x", "--y"] },
    { "label": "RETRIEVAL PATH", "items": ["service", "+shortcut", "api"] }
  ]
}
```

## Rules

- Keep exactly 4 `ribbon` items.
- Keep exactly 4 `columns` in v1.
- Allowed `color` values:
  - `blue`
  - `green`
  - `orange`
  - `purple`
- Each `column.blocks[]` item must contain:
  - `heading`
  - `summary`
  - `commands[]`
- `commands[]` entries should be short chips, not paragraphs.
- `snapshot` must use a public URL or public label. Never use local filesystem paths.
- `summary` should be 1 to 2 short sentences.

## Recommended 4-column grouping

Default grouping order:

1. Collaboration / communication
2. Content / knowledge
3. Data / execution
4. Platform / agent

If the source does not fit these labels exactly, preserve the same structure but rename the column titles to the closest user-facing functional domains.

## What Not To Do

- Do not add extra top-level sections.
- Do not turn this into a narrative article summary.
- Do not use implementation-layer buckets like “backend / frontend / auth / infra” unless the source itself is an internal architecture tool and the user clearly wants that framing.
- Do not expose confidential paths, tokens, or internal-only labels.

