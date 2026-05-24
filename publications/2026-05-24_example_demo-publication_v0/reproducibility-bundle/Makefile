# Reproducibility-bundle Makefile — DEMO
#
# `make replicate` is the entry point. For real publications, this target
# should reproduce the headline figures of the manuscript from raw inputs.
# For this DEMO, it runs the structural-compliance verifiers.

.PHONY: replicate verify-structure verify-bundle clean help

# Resolve the repo root regardless of where `make` is invoked.
REPO_ROOT := $(shell git rev-parse --show-toplevel 2>/dev/null || echo "$(CURDIR)/../../..")
PUB_DIR := $(REPO_ROOT)/publications/2026-05-24_example_demo-publication_v0

help:
	@echo "Targets:"
	@echo "  replicate         — run both structural verifiers (the DEMO's headline result)"
	@echo "  verify-structure  — run the repo-level CI guard"
	@echo "  verify-bundle     — run the independent Python verifier"
	@echo "  clean             — remove generated artifacts (none in this DEMO)"

replicate: verify-structure verify-bundle
	@echo
	@echo "DEMO: replication complete. Headline result = exit code 0."

verify-structure:
	@echo ">> Running repo-level structure check: $(REPO_ROOT)/scripts/check-publication-structure.sh"
	@bash $(REPO_ROOT)/scripts/check-publication-structure.sh

verify-bundle:
	@echo ">> Running bundle-level structure check: code/01_verify_bundle_structure.py"
	@python3 code/01_verify_bundle_structure.py "$(PUB_DIR)"

clean:
	@echo "Nothing to clean in this DEMO."
