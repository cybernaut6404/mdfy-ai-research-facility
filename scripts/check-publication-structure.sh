#!/usr/bin/env bash
# check-publication-structure.sh
#
# v0 CI guard for mdfy-ai-research-facility.
# Validates that every folder under publications/ contains the required files.
# Per Charter §6 and STANDARDS.md.
#
# Usage:
#   ./scripts/check-publication-structure.sh
# Exit codes:
#   0 — all publication folders satisfy the structure check (or no publications yet)
#   1 — one or more publication folders are missing required files
#
# Intended to run as a GitHub Actions step on pull requests touching publications/.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUBS_DIR="$REPO_ROOT/publications"

if [ ! -d "$PUBS_DIR" ]; then
  echo "No publications/ directory found at $PUBS_DIR; nothing to check."
  exit 0
fi

# Required artifacts in every publication folder.
REQUIRED_FILES=(
  "README.md"
  "ai-use-disclosure.md"
  "internal-review.md"
)
REQUIRED_DIRS=(
  "reproducibility-bundle"
)

errors=0
checked=0

# Iterate over publication folders (ignore .gitkeep and any non-directory entries).
shopt -s nullglob
for pub_dir in "$PUBS_DIR"/*/; do
  pub_name="$(basename "$pub_dir")"
  # Skip if matches the naming convention check (rough): YYYY-MM-DD prefix.
  if ! [[ "$pub_name" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}_ ]]; then
    echo "  WARN: $pub_name does not match the YYYY-MM-DD_source-repo_short-title_vN naming convention (Charter §14)."
  fi

  checked=$((checked + 1))
  echo "Checking: $pub_name"

  for f in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$pub_dir/$f" ]; then
      echo "  MISSING FILE: $pub_dir$f"
      errors=$((errors + 1))
    fi
  done

  for d in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$pub_dir/$d" ]; then
      echo "  MISSING DIR:  $pub_dir$d/"
      errors=$((errors + 1))
    fi
  done
done

echo
echo "Checked $checked publication folder(s); $errors error(s)."

if [ "$errors" -gt 0 ]; then
  echo
  echo "Publication structure check failed. See Charter §6 and templates/reproducibility-bundle_CHECKLIST.md."
  exit 1
fi

exit 0
