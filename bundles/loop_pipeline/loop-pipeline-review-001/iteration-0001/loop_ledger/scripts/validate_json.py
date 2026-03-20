#!/usr/bin/env python3
"""Validate a JSON file against a JSON Schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: validate_json.py <schema> <instance>")

    schema_path = Path(sys.argv[1]).resolve()
    instance_path = Path(sys.argv[2]).resolve()

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    instance = json.loads(instance_path.read_text(encoding="utf-8"))
    jsonschema.validate(instance=instance, schema=schema)
    print(f"OK {instance_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

