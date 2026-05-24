#!/usr/bin/env python3
"""
DEMO bundle verifier.

Confirms that the DEMO publication folder contains the files required by
the v0 charter and Tier-M checklist. This is the headline 'result' of the
DEMO publication — exit code 0 means structural compliance.

Run from `make replicate` in the bundle directory, or directly:

    python3 code/01_verify_bundle_structure.py <publication-folder>

For real Tier-M publications, this script is replaced with the actual
analysis or evaluation code that produces the manuscript's headline figures.
"""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_PUBLICATION_FILES = [
    "README.md",
    "manuscript.md",
    "ai-use-disclosure.md",
    "internal-review.md",
    "deviations.md",
    "coi-disclosure_demo.md",
]

REQUIRED_PUBLICATION_DIRS = [
    "reproducibility-bundle",
    "correspondence",
]

REQUIRED_BUNDLE_FILES = [
    "README.md",
    "Makefile",
    "environment.yml",
    "seeds.json",
    "PROVENANCE.md",
    "replication-log.md",
]

REQUIRED_BUNDLE_DIRS = [
    "code",
    "data",
]


def verify(pub_dir: Path) -> int:
    """Return 0 if pub_dir satisfies the DEMO structural requirements; else 1."""
    errors: list[str] = []

    if not pub_dir.is_dir():
        print(f"FAIL: publication folder does not exist: {pub_dir}", file=sys.stderr)
        return 1

    for name in REQUIRED_PUBLICATION_FILES:
        if not (pub_dir / name).is_file():
            errors.append(f"  missing file: {pub_dir / name}")

    for name in REQUIRED_PUBLICATION_DIRS:
        if not (pub_dir / name).is_dir():
            errors.append(f"  missing dir:  {pub_dir / name}/")

    bundle = pub_dir / "reproducibility-bundle"
    for name in REQUIRED_BUNDLE_FILES:
        if not (bundle / name).is_file():
            errors.append(f"  missing file: {bundle / name}")

    for name in REQUIRED_BUNDLE_DIRS:
        if not (bundle / name).is_dir():
            errors.append(f"  missing dir:  {bundle / name}/")

    if errors:
        print("DEMO bundle structural-compliance check: FAILED", file=sys.stderr)
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    print(f"DEMO bundle structural-compliance check: PASSED ({pub_dir.name})")
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python3 code/01_verify_bundle_structure.py <publication-folder>",
            file=sys.stderr,
        )
        return 2

    pub_dir = Path(sys.argv[1]).resolve()
    return verify(pub_dir)


if __name__ == "__main__":
    sys.exit(main())
