#!/usr/bin/env python3
"""Create a zip archive for a materialized review bundle."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Path to review bundle manifest")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    output_root = Path(manifest["output_root"]).resolve()
    if not output_root.is_dir():
        raise SystemExit(f"materialized bundle missing: {output_root}")

    dist_root = Path("/home/_404/src/loop_ledger/dist")
    dist_root.mkdir(parents=True, exist_ok=True)
    archive_name = f"{manifest['bundle_id']}.{manifest['iteration_id']}.review.zip"
    archive_path = dist_root / archive_name

    bundle_root = output_root.parent.parent
    if not bundle_root.is_dir():
        raise SystemExit(f"bundle root missing: {bundle_root}")

    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as zf:
        for path in sorted(output_root.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(bundle_root.parent))

    print(archive_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
