#!/usr/bin/env python3
import sys
from pathlib import Path
from typing import List, Set

IMG_DIR = Path(__file__).resolve().parent.parent / "imgs"
MAX_SIZE_MB = 5
MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024

# Filenames to ignore if they exceed the size limit
EXCEPTIONS: Set[str] = {
    "feature-tag-browse.gif",
    "feature-create-new-tag.gif",
    "feature-search-all-corners-of-your-datastack.gif",
    "feature-impact-analysis.gif",
    "feature-view-entitiy-details-via-lineage-vis.gif",
    "feature-rich-documentation.gif",
    "atul-saurav.png",
}


def is_exception(file_path: Path) -> bool:
    return file_path.name in EXCEPTIONS


def get_oversized_files(img_dir: Path, max_size_bytes: int) -> List[Path]:
    oversized = []
    for file_path in img_dir.rglob("*"):
        if file_path.is_file() and not is_exception(file_path):
            size = file_path.stat().st_size
            if size > max_size_bytes:
                oversized.append((file_path, size))
    return oversized


def main() -> None:
    oversized_files = get_oversized_files(IMG_DIR, MAX_SIZE_BYTES)
    if oversized_files:
        for file_path, size in oversized_files:
            print(
                f"FAIL: {file_path} is larger than {MAX_SIZE_MB}MB ({size / (1024 * 1024):.2f}MB)",
                file=sys.stderr,
            )
        sys.exit(1)
    print(f"All files are under {MAX_SIZE_MB}MB (except for allowed exceptions).")


if __name__ == "__main__":
    main()
