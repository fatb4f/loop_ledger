#!/usr/bin/env python3
"""Report whether all declared review bundle inputs exist."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_review_bundle_inputs.py <manifest>")

    manifest_path = Path(sys.argv[1]).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    groups = [
        ("include", manifest.get("include", [])),
        ("required_outputs", manifest.get("evidence_bundle", {}).get("required_outputs", [])),
        ("required_checks", manifest.get("evidence_bundle", {}).get("required_checks", [])),
    ]

    missing = False
    for label, items in groups:
        for item in items:
            source = Path(item["source"]).expanduser()
            state = "OK" if source.is_file() else "MISSING"
            print(f"{label}\t{item['role']}\t{state}\t{source}")
            if not source.is_file():
                missing = True

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
