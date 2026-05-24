# Reproducibility-bundle Makefile for the 24-channel validation.
#
# Target end state: `make replicate` re-derives the headline κ values from
# raw inputs on a fresh machine. As of 2026-05-24 this Makefile is a STUB
# that walks the operator through the pointers in code/README.md and
# data/README.md. A future Gate-7 finalisation pass will either vendor the
# source code into code/ or pin git submodules and have `make replicate`
# clone+run them.

.PHONY: replicate stub-walkthrough verify-structure clean help

help:
	@echo "Reproducibility-bundle Makefile (STUB — Gate-7 finalisation pending)"
	@echo ""
	@echo "Targets:"
	@echo "  make replicate          Stub walkthrough of replication steps"
	@echo "  make verify-structure   Run the unit's structure check against this publication"
	@echo "  make clean              No-op (nothing to clean in stub state)"
	@echo "  make help               This message"

replicate: stub-walkthrough

stub-walkthrough:
	@echo "===================================================================="
	@echo " STUB: end-to-end replication of the 24-channel validation"
	@echo "===================================================================="
	@echo ""
	@echo "This bundle does NOT yet implement a one-command replication."
	@echo "Per replication-log.md, the bundle's Gate-7 finalisation is pending."
	@echo ""
	@echo "What you would need to do manually right now to re-derive the κ values:"
	@echo ""
	@echo "  1. Clone the source repos at the pinned SHAs:"
	@echo "       mg-digital-twin           @ f492844  (extraction + harness + judge)"
	@echo "       personality-central-db    @ 2bdf13b  (channel/construct catalog)"
	@echo "       personality-construct-runner @ d55296b  (steering loadout compiler)"
	@echo "       personality-mixer-codex   @ 5462733  (UI; not needed for κ re-derivation)"
	@echo "       personality-mixer-claude  @ 3963ce4  (UI; not needed for κ re-derivation)"
	@echo ""
	@echo "  2. From mg-digital-twin/, install the env:"
	@echo "       uv sync                 (or 'conda env create -f environment.yml' from this bundle)"
	@echo ""
	@echo "  3. Set credentials:"
	@echo "       export MODAL_TOKEN_ID=..."
	@echo "       export MODAL_TOKEN_SECRET=..."
	@echo "       export ANTHROPIC_API_KEY=..."
	@echo ""
	@echo "  4. Run the validation harness:"
	@echo "       cd mg-digital-twin/experiments/d4-fader-intervention/"
	@echo "       python harness.py eval --channel-set 2.1.0 --layers 12,16,20 --coef 2"
	@echo "       python harness.py eval --channels psychopathy,sadism --layers 12,16,20 --coef 4   # diagnostic"
	@echo "       python analyse.py --results-dir runs/"
	@echo ""
	@echo "  5. Compare the recovered κ values against the manuscript:"
	@echo "       diff -u <(jq -S '.kappa' runs/*/results.json) <(cat ../../publications/2026-05-24_personality-mixer_activation-steering-validation_v0/data/published-results.json)"
	@echo "       (the data/published-results.json file is also Gate-7 TODO)"
	@echo ""
	@echo "  6. Record the run in replication-log.md."
	@echo ""
	@echo "Estimated wall-clock: 2–3 hours of L4 GPU time + ~30 minutes for analyse.py + judge."
	@echo "Estimated cost: ~\$$2–4 Modal + ~\$$5–10 Anthropic Opus."
	@echo ""
	@echo "===================================================================="

verify-structure:
	@cd ../../.. && bash scripts/check-publication-structure.sh

clean:
	@echo "Nothing to clean — this bundle is in stub state."
