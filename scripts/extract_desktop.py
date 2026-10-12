#!/usr/bin/env python3
"""Copy the official i18n files from the locally installed Claude Desktop into sources/desktop/.

Usage: python3 scripts/extract_desktop.py [/Applications/Claude.app]
"""
import json
import plistlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP = Path(sys.argv[1] if len(sys.argv) > 1 else "/Applications/Claude.app")
RES = APP / "Contents" / "Resources"
OUT = ROOT / "sources" / "desktop"


def main():
    if not RES.is_dir():
        sys.exit(f"{RES} not found. Pass the path to Claude.app.")
    version = plistlib.loads((APP / "Contents" / "Info.plist").read_bytes())["CFBundleShortVersionString"]
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.json"):
        old.unlink()
    files = sorted(RES.glob("*.json"))
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        # Sort keys so git diffs stay readable across versions
        (OUT / f.name).write_text(
            json.dumps(dict(sorted(data.items())), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    (OUT / "VERSION").write_text(f"{version}\n", encoding="utf-8")
    print(f"Claude Desktop {version}: copied {len(files)} locale files -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
