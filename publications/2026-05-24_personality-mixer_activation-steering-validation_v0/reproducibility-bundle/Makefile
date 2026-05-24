# Reproducibility-bundle Makefile for the 24-channel validation.
#
# Three replicate targets:
#   make replicate         — Full local verification (no API calls; no money). Re-derives
#                            stats + figures + κ delta from the vendored results.
#                            Default; should complete in ~5 seconds with no external deps.
#   make replicate-full    — Full end-to-end re-run on Modal (regenerates the runs/
#                            from scratch, calls the Anthropic judge, then verifies).
#                            REQUIRES Modal + Anthropic credentials and spends $5–15.
#   make verify-only       — Just the κ delta against published values; no figure / stats
#                            regeneration. Fastest sanity check.
#
# Other:
#   make verify-structure  — Run the unit's structure check from this folder.
#   make clean             — Remove derived data (data/derived/ and data/figures/).
#   make help              — This message.

PY := .venv-stats/bin/python
VENV := .venv-stats
PIP_DEPS := scipy statsmodels matplotlib numpy

.PHONY: replicate replicate-full verify-only verify-structure clean help venv

help:
	@echo "Reproducibility-bundle Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  make replicate         — Local verification: stats + figures + κ delta from vendored results"
	@echo "  make replicate-full    — End-to-end re-run on Modal (needs creds + money)"
	@echo "  make verify-only       — Fastest κ delta check"
	@echo "  make verify-structure  — Run the unit's publication-structure check"
	@echo "  make clean             — Remove derived artifacts"
	@echo "  make venv              — Create the local Python venv (auto-runs on replicate)"
	@echo "  make help              — This message"

# Local venv + deps. Idempotent.
$(VENV)/bin/python:
	@echo "==> creating venv at $(VENV)/"
	python3 -m venv $(VENV)
	@echo "==> installing Python deps: $(PIP_DEPS)"
	$(VENV)/bin/pip install --quiet --upgrade pip
	$(VENV)/bin/pip install --quiet $(PIP_DEPS)

venv: $(VENV)/bin/python
	@echo "venv ready at $(VENV)/"

# Default replicate: local verification, no API calls.
replicate: venv
	@echo "===================================================================="
	@echo " replicate: local verification of the 24-channel substrate"
	@echo "===================================================================="
	@echo ""
	@echo "Step 1 of 3: compute stats (binomial tests, Wilson CIs, FDR)"
	$(PY) code/compute_stats.py
	@echo ""
	@echo "Step 2 of 3: regenerate figures"
	$(PY) code/figures.py
	@echo ""
	@echo "Step 3 of 3: verify κ against published values (9-channel coverage; new-15 are NOT_VENDORED)"
	@$(PY) code/verify_kappa.py
	@echo ""
	@echo "===================================================================="
	@echo " replicate: done."
	@echo "===================================================================="
	@echo ""
	@echo "Derived artifacts:"
	@echo "  data/derived/stats.{json,md}"
	@echo "  data/derived/replication-delta.md"
	@echo "  data/figures/fig{1,2,3}_*.png"
	@echo ""
	@echo "For full end-to-end re-run on Modal (regenerates runs/ from scratch, ~\$$10):"
	@echo "  make replicate-full"

verify-only: venv
	$(PY) code/verify_kappa.py

# Full end-to-end re-run on Modal. REQUIRES credentials.
replicate-full: venv check-creds
	@echo "===================================================================="
	@echo " replicate-full: end-to-end re-run on Modal L4"
	@echo "===================================================================="
	@echo ""
	@echo "WARNING: this target spends real money on Rick's Modal + Anthropic accounts."
	@echo "  Estimated: ~\$$2–4 Modal L4 GPU time + ~\$$5–10 Anthropic Opus judge calls."
	@echo "  Estimated wall-clock: 2–3 hours (each channel = ~3 min generation + 1 min judging)."
	@echo "  Per-coefficient grid: c ∈ {0.5, 1.0, 1.5, 2.0}; psychopathy + sadism also at c=4."
	@echo "  Channels (24): see code/compute_stats.py CHANNELS list."
	@echo ""
	@echo "Press Ctrl-C in the next 10 seconds to abort."
	@sleep 10
	@echo ""
	@echo "Step 1: generate response pairs on Modal"
	@cd code/experiments/d4-fader-intervention && for ch in achievement_striving cheerfulness sociability stimulation dospert_financial dospert_recreational cautiousness conscientiousness_self_discipline self_direction narcissism psychopathy attachment_avoidant hexaco_emotionality honesty_humility machiavellianism hexaco_extraversion self_monitoring openness hexaco_agreeableness locus_of_control attachment_anxious self_defeat sycophancy sadism; do \
		echo "  --- channel: $$ch ---"; \
		$(PY) harness.py eval --channel $$ch --layers 12,16,20 --coef 2.0 --out-dir ../../data/runs/$${ch}_replicate || exit 1; \
	done
	@echo ""
	@echo "Step 2: judge response pairs with Claude Opus 4.7"
	@cd code/experiments/d4-fader-intervention && for ch in achievement_striving cheerfulness sociability stimulation dospert_financial dospert_recreational cautiousness conscientiousness_self_discipline self_direction narcissism psychopathy attachment_avoidant hexaco_emotionality honesty_humility machiavellianism hexaco_extraversion self_monitoring openness hexaco_agreeableness locus_of_control attachment_anxious self_defeat sycophancy sadism; do \
		echo "  --- judging: $$ch ---"; \
		$(PY) analyse.py --channel $$ch --runs ../../data/runs/$${ch}_replicate --out ../../data/results/$${ch}_replicate || exit 1; \
	done
	@echo ""
	@echo "Step 3: verify κ against published values"
	$(PY) code/verify_kappa.py --results-root data/results
	@echo ""
	@echo "==> replicate-full complete; record in replication-log.md per the bundle's standard."

check-creds:
	@test -n "$$MODAL_TOKEN_ID" || (echo "ERROR: MODAL_TOKEN_ID not set"; exit 1)
	@test -n "$$MODAL_TOKEN_SECRET" || (echo "ERROR: MODAL_TOKEN_SECRET not set"; exit 1)
	@test -n "$$ANTHROPIC_API_KEY" || (echo "ERROR: ANTHROPIC_API_KEY not set"; exit 1)
	@echo "==> all required credentials present"

verify-structure:
	@cd ../../.. && bash scripts/check-publication-structure.sh

clean:
	rm -rf data/derived/ data/figures/
	@echo "==> removed data/derived/ and data/figures/"
	@echo "==> venv at $(VENV)/ retained; run 'rm -rf $(VENV)' to remove"
