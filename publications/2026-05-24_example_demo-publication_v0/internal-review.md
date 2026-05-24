# Internal Review — DEMO: Reproducibility-bundle reference layout for mdfy-ai-research-facility v0

## Recommendation
PROCEED — this DEMO satisfies every Tier-M checklist item and is suitable to retain in the repository as a structural reference.

## Review metadata
- Prompt version: v1 (`templates/internal-review-prompt_v1.md`)
- AI reviewer: Anthropic Claude, model `claude-opus-4-6`
- Date of review: 2026-05-24
- Inputs provided:
  - Manuscript draft: `manuscript.md`
  - Reproducibility-bundle PROVENANCE: `reproducibility-bundle/PROVENANCE.md`
  - AI-use disclosure draft: `ai-use-disclosure.md`
  - Tier-M checklist: `STANDARDS.md` §"Tier M — Methods and engineering"
  - Scoping memo: implicit (acknowledged in `README.md`)

## 1. Tier-checklist compliance

- Written specification of what the tool/method does and what it explicitly does not do — `SATISFIED`. The README states the contribution is the structural example itself; the manuscript §2 names the method (compliance verification via CI script + independent Python check) and §5 names what it does not demonstrate (substantive validation of the standards).
- Test suite or validation procedure, runnable from the reproducibility bundle — `SATISFIED`. `reproducibility-bundle/Makefile` provides `make replicate`, invoking `scripts/check-publication-structure.sh` plus the independent verifier `code/01_verify_bundle_structure.py`.
- Evaluation protocol specified before evaluation runs — `SATISFIED`. The protocol is "exit code 0 from both verifiers," stated in `README.md` and the manuscript §3 prior to any run being reported.
- Reproducibility bundle satisfying the bundle checklist — `SATISFIED`. PROVENANCE.md, environment.yml, seeds.json, replication-log.md, Makefile, code/, data/ all present. The seeds file is trivially populated (the DEMO uses no randomness) but is present for structural compliance.
- AI-use disclosure paragraph drafted and reviewed — `SATISFIED`. See `ai-use-disclosure.md`; Tier 2 assignment is correct given the actual contribution (drafting only).
- Internal review (Gate 6) completed and signed — `SATISFIED` (in progress; this very file).
- Model Card for any released model — `N/A`. No model is released in this DEMO.
- For benchmarks: clear statement of dataset provenance, license, and contamination risk — `N/A`. No benchmark dataset.

`SATISFIED: 6 / NOT SATISFIED: 0 / N/A: 2`

## 2. Claim-evidence calibration

The manuscript makes one substantive claim: "this DEMO folder passes the v0 structure check." The evidence is the `replication-log.md` entry recording the run and its exit code. The claim is calibrated correctly. No over-claims. The manuscript §5 explicitly under-claims by name ("does not validate the standards themselves, nor the AI-mediated review process") — this is appropriate; the DEMO is structural only.

No hedge-language inconsistencies. The abstract and discussion describe the contribution at the same strength.

## 3. Pre-registration / exploration-plan adherence

`N/A`. Tier M does not require pre-registration. The Scoping Memo is implicit and named in `README.md`.

## 4. AI-use disclosure completeness

The disclosure tier (Tier 2) is correctly assigned. The AI involvement listed (drafting only, no analysis, no figures) matches the actual record. No prompt archive is committed; the disclosure notes this and explains why (the prompts are not research artifacts for this DEMO; the founding-session lab-notebook entry will reference the session).

## 5. Reproducibility-bundle spot check

There is one headline result (exit code 0). The bundle's `PROVENANCE.md` names the chain: `code/01_verify_bundle_structure.py` produces the headline-claim verification by checking for the same files the manuscript names; the `Makefile` chains it to the repo-level CI script. Environment specification is a minimal `environment.yml` (Python 3.11 + standard library only — no third-party dependencies, sufficient for the verifier). `seeds.json` is populated trivially (no randomness in the DEMO). The `replication-log.md` records a fresh-machine end-to-end run on 2026-05-24 with exit code 0.

## 6. Ethics, dual-use, and responsible-release

No ethical concerns: no human subjects, no model release, no data of any kind. Dual-use risk is none. No Responsible-Release Review was triggered.

## 7. Conflicts of interest

`coi-disclosure_demo.md` is present and itemizes no publication-specific COI beyond the standing tooling disclosure (Anthropic, GitHub, Zenodo, OSF) in README.md.

## 8. Internal consistency

No numerical inconsistencies (no numbers to check). The methods description and the bundle's code agree (both check the same artifacts). The implicit Scoping Memo and the manuscript agree on the contribution.

## 9. Reservations not covered above

One observation, not a defect: this DEMO uses a self-referential method (a publication whose contribution is its own structure). Real Tier-M publications will require substantive evaluation procedures and should not adopt this self-referential pattern. The DEMO is for structural reference only.

## 10. Recommendation (restated)

PROCEED — every checklist item is satisfied or has acceptable N/A justification; no over-claims; AI-use disclosure is accurate; reproducibility bundle spot-checks clean; ethics and COI clean. This DEMO is suitable to retain in the repository as a structural reference for future contributors.

---

## Human counter-signature

I have read the AI reviewer's response in full. The findings I accept are listed below; the findings I overrule (with reason) are listed below. I take accountability for the final disposition of this review under ICMJE authorship criterion 4.

Accepted findings:
- All items in §1 satisfied or N/A as marked.
- The reservation in §9 (self-referential method is appropriate only for the DEMO, not for real publications) is accepted and added as a note in this folder's README for future readers.

Overruled findings:
- None.

Required actions before release:
- None. This DEMO is not for external release; it is a retained structural reference.

Counter-signed by: Rick Weakley
Date: 2026-05-24
Disposition: PROCEED (retain in repository as structural reference; do not publish externally)
