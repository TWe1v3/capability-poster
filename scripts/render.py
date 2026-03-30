#!/usr/bin/env python3
"""
Render a capability-poster JSON payload to HTML and optionally PNG.

Usage:
  python3 render.py --data poster_data.json --output poster.png --ratio medium
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RATIO_SIZES = {
    "narrow": (1200, None),
    "medium": (1600, None),
    "wide": (1920, None),
}


def load_template(template_path: Path) -> str:
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text(encoding="utf-8")


def write_preview_html(template_html: str, data: dict, output_path: Path) -> Path:
    preview_path = output_path.with_suffix(".html")
    json_str = json.dumps(data, ensure_ascii=False)
    html = template_html.replace("__POSTER_DATA__", json_str)

    preview_path.write_text(html, encoding="utf-8")
    return preview_path


def take_screenshot(preview_path: Path, output_path: Path, width: int) -> tuple[bool, str]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False, "Playwright for Python is not installed. HTML preview was created instead."

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": 900})
        page.goto(preview_path.resolve().as_uri(), wait_until="networkidle")
        page.wait_for_timeout(800)

        content_height = page.evaluate(
            """
            () => {
              const node = document.getElementById('poster');
              const height = node ? node.scrollHeight : document.body.scrollHeight;
              return Math.ceil(height + 32);
            }
            """
        )

        page.set_viewport_size({"width": width, "height": content_height})
        page.wait_for_timeout(150)
        page.screenshot(path=str(output_path), full_page=False, type="png")
        browser.close()
    return True, f"Rendered PNG at {output_path}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render capability poster to HTML and PNG")
    parser.add_argument("--data", required=True, help="Path to poster_data.json")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument(
        "--ratio",
        default="medium",
        choices=RATIO_SIZES.keys(),
        help="Width preset: narrow|medium|wide",
    )
    parser.add_argument(
        "--template",
        default=None,
        help="Optional path to template-functional-v2.html",
    )
    args = parser.parse_args()

    data_path = Path(args.data).resolve()
    output_path = Path(args.output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if args.template:
        template_path = Path(args.template).resolve()
    else:
        template_path = Path(__file__).resolve().parent.parent / "assets" / "template-functional-v2.html"

    data = json.loads(data_path.read_text(encoding="utf-8"))
    template_html = load_template(template_path)
    preview_path = write_preview_html(template_html, data, output_path)

    width, _ = RATIO_SIZES[args.ratio]
    ok, message = take_screenshot(preview_path, output_path, width)

    print(f"HTML preview: {preview_path}")
    print(message)
    return 0 if ok or preview_path.exists() else 1


if __name__ == "__main__":
    sys.exit(main())
