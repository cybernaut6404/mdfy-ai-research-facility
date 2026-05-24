# mdfy-ai-research-facility

## Charter & Operating Manual — v0.0.4

**Prepared:** 2026-05-24 (founding session)
**Founding decisions baked in:** 2026-05-24 (v0.0.2)
**Scaffold completed (LICENSE files, CI, review prompt v1, worked-example DEMO):** 2026-05-24 (v0.0.3)
**Last open question closed (CI maturity-progression triggers ratified; Tier 3/4 boundary sharpened; compliance-artifact paths fixed; transcript-mirror procedure defined):** 2026-05-24 (v0.0.4)
**Source workspace:** founding session (Cowork) + bootstrap session
**Status:** v0.0.4 — in effect (latest tag `v0.0.4-charter`; founding-commit tag `v0.0.3-charter` retained)
**Document owner:** Rick Weakley (rick@minorgod.com)

---

## 0. How to read this document

This is the founding charter for an internal AI research unit. It is written to be the single source of truth for how research is planned, executed, reviewed, published, and archived under the `mdfy-ai-research-facility` name. It is not a wish list. Every standard described here is intended to be enforced from day one, including against the founder.

The founding decisions for v0 are resolved and baked into the body of this document. As of v0.0.4, the two original v1 open questions are also both closed: the hardened Gate-6 review prompt lives at `templates/internal-review-prompt_v1.md` (closed at v0.0.3), and the CI maturity-progression triggers are ratified in §18 (closed at v0.0.4). The next scheduled review is the annual charter review per §16; no genuine open questions remain in the meantime.

Anywhere a referenced standard has a canonical source, it is cited in §17. Where the literature is genuinely unsettled or the canonical source is in flux, the charter says so out loud rather than guessing.

---

## 1. Mission

The mission of `mdfy-ai-research-facility` is to produce a small body of AI-related research whose methods, evidence, and disclosures would withstand the editorial review of the strongest journals and conferences in the relevant fields. The unit exists not to maximize publication count, but to ensure that every output bearing its name is independently verifiable, ethically defensible, and useful to the field.

The unit is the central research function shared across all of the founder's project repositories. Project repos produce experiments and code; the unit publishes, archives, and certifies the resulting research.

## 2. Founding principles

Six principles take precedence over local convenience whenever they conflict.

**Integrity over speed.** No deadline justifies skipping pre-registration, reproducibility packaging, or disclosure. If a study cannot meet the unit's standards by a target date, the target moves.

**Falsifiability over advocacy.** Every confirmatory claim is paired with the conditions that would disprove it. Exploratory work is labelled as such, not retrofitted into confirmation.

**Transparency over polish.** The lab notebook, dead ends, failed runs, and revised hypotheses are part of the record. A clean narrative that hides the actual research path is a defect.

**Calibrated claims.** The size of the evidence determines the size of the claim. A single-subject pilot is reported as a single-subject pilot; an LLM-judged outcome is reported as an LLM-judged outcome; a confirmatory result is reported only when it actually was confirmatory.

**Independence of accountability.** No human or AI contributor is exempt from review. Where the unit currently has only one human reviewer, that limitation is disclosed.

**Reproducibility by construction.** Anything the unit publishes ships with the artifacts needed to re-run it from scratch. Reproducibility is not added in revision; it is the deliverable's first draft.

## 3. Identity and scope

`mdfy-ai-research-facility` is, in its v0 form, a solo research unit operated by the founder with substantial assistance from large language models (primarily Anthropic's Claude family). It is architected to scale to a small group of one to three collaborators without rearchitecture.

The unit is not a legal entity. Should formal entity status (LLC, nonprofit, or 501(c)(3)) be pursued in future, this charter will be amended to add a Governance Annex covering IP assignment, conflict-of-interest disclosure, and incorporation-specific obligations. Until then, all IP produced under the unit is the personal property of the founder, released under the licenses specified in §13.

The unit's domain is intentionally interdisciplinary. Current and anticipated work spans interpretability of large language models, computational behavioral science, single-case experimental designs applied to AI systems, and AI safety methodology. The unit does not claim expertise outside the disciplines covered by its current outputs.

## 4. The tiered standards framework

The unit recognizes four study types. Each type has a fixed minimum standard. The "lighter" tiers are not relaxed; they are calibrated to the actual epistemic claim being made. Nothing produced under the unit's name falls below the standard for its type.

**Tier C — Confirmatory.** Pre-registered hypothesis tests. Required: a public pre-registration time-stamped before data collection (OSF or AsPredicted), a power analysis or sequential design justification, primary and secondary outcomes named in advance, an analysis script written before unblinding, a Reproducibility Bundle (§9), and internal review (§16). Deviations from the pre-registration are reported in a dedicated section.

**Tier E — Exploratory.** Hypothesis-generating studies. Required: an Exploration Plan time-stamped before data collection (lighter than a pre-reg; states the research question, design, and what counts as an interesting result), full Reproducibility Bundle, internal review, and explicit labelling of every result as exploratory. Tier E results may not be presented as confirmatory in subsequent outputs; they require a follow-up Tier C study to upgrade.

**Tier M — Methods and engineering.** Tooling, benchmarks, new measurement instruments, ablations. Required: a written specification of what the tool or method does and what it does not do, a test suite or validation procedure, Reproducibility Bundle, internal review. No pre-registration required, but any claim about the method's performance must include the evaluation protocol.

**Tier T — Theoretical and review.** Conceptual papers, frameworks, literature reviews, meta-analyses. Required: a written protocol for any systematic search or meta-analysis (PRISMA 2020 where applicable), full bibliography under version control, conflict-of-interest disclosure (§12), internal review. Meta-analyses additionally require pre-registration of the inclusion criteria and analysis plan.

Every output carries its tier in its metadata header. Cross-tier outputs (e.g., a paper containing both Tier E and Tier C studies) state the tier per study.

## 5. Research workflow

The lifecycle of a project moves through nine gates. Each gate produces an artifact committed to the unit's repository; nothing is informal.

**Gate 1 — Idea capture.** A short entry in the Lab Notebook (§10) describing the question, why it matters, and the expected tier.

**Gate 2 — Scoping.** A one-to-two-page Scoping Memo identifying the study type (Tier), the population and materials, the dependencies, and the anticipated risks (including dual-use concerns; §11).

**Gate 3 — Pre-registration or Exploration Plan.** Time-stamped on OSF (Tier C, Tier T meta-analyses), AsPredicted (Tier C when an OSF preregistration is disproportionate), or as a signed-and-dated commit in the unit's `preregistrations/` directory (Tier E).

**Gate 4 — Execution.** Code, data collection, prompt logs, and notebook entries are committed continuously to the project's source repository. The unit's repo only sees the finished bundle.

**Gate 5 — Analysis.** Analysis scripts are committed before unblinding (Tier C). Exploratory analysis is permitted and disclosed (Tier E).

**Gate 6 — Internal review.** A reviewer who is not the primary author reads the draft against the tier's standard checklist. In v0, with a single human reviewer, this review is performed by Claude under a structured review prompt (working draft in `STANDARDS.md`; the prompt is itself a versioned artifact tracked in `templates/`) and counter-signed by the founder. The limitation is disclosed in the AI-use disclosure of every paper this review touches (§7). When the first non-founder collaborator joins, the review duty moves to that human and AI review becomes supplementary rather than primary; at that point, an external advisor will also be sought (§16).

**Gate 7 — Reproducibility bundle finalization.** Per §9.

**Gate 8 — Release.** Tagged git release in the unit's repo, DOI minted via Zenodo, CITATION.cff updated, preprint posted (arXiv or domain-appropriate server) before any journal submission. The unit's default is preprint-first.

**Gate 9 — Archival and lessons.** A short post-publication entry in the Lab Notebook recording what went well, what failed, and what should change in the next study. Major lessons are escalated into amendments of this charter.

## 6. Repository structure

The unit lives in a single dedicated git repository at `/Users/richardweakley/ai-workspace/mdfy-ai-research-facility`, initialized as a private repo with the following structure:

```
mdfy-ai-research-facility/
├── CHARTER.md                          # this document
├── STANDARDS.md                        # detailed tier standards & checklists
├── AI_USE_POLICY.md                    # the disclosure policy
├── README.md                           # entry point, masthead, citation
├── CITATION.cff                        # citable repo metadata
├── LICENSE-CODE                        # Apache-2.0 full text
├── LICENSE-CONTENT                     # CC-BY-4.0 reference + attribution language
├── CHANGELOG.md                        # charter amendments + releases
├── BOOTSTRAP.md                        # one-time setup steps
├── .gitignore / .gitattributes / .editorconfig
│
├── .github/
│   └── workflows/
│       └── structure-check.yml         # GitHub Actions CI invoking the v0 guard
│
├── scripts/
│   └── check-publication-structure.sh  # v0 CI guard (§6)
│
├── publications/
│   ├── 2026-05-24_example_demo-publication_v0/   # worked example, Tier-M DEMO
│   └── YYYY-MM-DD_source-repo_short-title_vN/    # real publications use this pattern
│       ├── manuscript.pdf
│       ├── manuscript.md (or .tex source)
│       ├── README.md
│       ├── deviations.md
│       ├── coi-disclosure_*.md
│       ├── internal-review.md
│       ├── ai-use-disclosure.md
│       ├── reproducibility-bundle/
│       │   ├── code/
│       │   ├── data/
│       │   ├── environment.yml
│       │   ├── seeds.json
│       │   ├── PROVENANCE.md
│       │   ├── replication-log.md
│       │   └── Makefile
│       └── correspondence/
│
├── preregistrations/                   # all pre-regs and exploration plans
│   └── YYYY-MM-DD_source-repo_short-title.md
│
├── notebooks/                          # the lab notebook (§10)
│   └── YYYY/MM/YYYY-MM-DD_short-title.md
│
├── coi/                                # annual COI disclosure snapshots
│   └── YYYY_founder-disclosure.md
│
├── templates/                          # the templates referenced by this charter
│   ├── publication-folder_GUIDE.md     # operator's guide to publication-folder structure
│   ├── pre-registration_TEMPLATE.md
│   ├── exploration-plan_TEMPLATE.md
│   ├── scoping-memo_TEMPLATE.md
│   ├── reproducibility-bundle_CHECKLIST.md
│   ├── ai-use-disclosure_PARAGRAPH.md
│   ├── lab-notebook-entry_TEMPLATE.md
│   ├── paper-README_TEMPLATE.md
│   ├── coi-disclosure_TEMPLATE.md
│   ├── deviations_TEMPLATE.md          # pre-registration-deviations document (Tier C/E required, others optional)
│   ├── neurips-checklist_TEMPLATE.md   # NeurIPS Paper Checklist for Tier M ML work
│   ├── internal-review-prompt_v1.md    # hardened Gate-6 review prompt
│   ├── internal-review-counter-signature_TEMPLATE.md   # standalone human counter-signature block
│   └── reproducibility-bundle_TEMPLATE/                # subfolder structure for publication bundles
│       ├── README_TEMPLATE.md
│       ├── PROVENANCE_TEMPLATE.md
│       ├── environment_TEMPLATE.yml
│       ├── seeds_TEMPLATE.json
│       ├── replication-log_TEMPLATE.md
│       ├── Makefile_TEMPLATE
│       ├── code/README_TEMPLATE.md
│       └── data/README_TEMPLATE.md
│
└── references/                         # the unit's master bibliography
    └── references_v0.md                # standards & methods references
```

The repo's `main` branch is protected: nothing merges without a PR, even from the founder. PRs run a lightweight CI check — the shell script `scripts/check-publication-structure.sh` — that validates the structure of new or modified `publications/` folders against the reproducibility-bundle checklist (presence of `README.md`, `reproducibility-bundle/`, `ai-use-disclosure.md`, and `internal-review.md`). The CI is deliberately minimal in v0 and can grow into link-validation, citation-validation, and on-tag reproducibility runs as the unit matures.

## 7. AI use and disclosure policy

The unit's policy on AI assistance is fully aligned with the International Committee of Medical Journal Editors recommendations (current as of 2024–2025) and the editorial policies of Nature, Science, JAMA, and the major ML venues. The policy is summarized here; the full policy lives in `AI_USE_POLICY.md`.

AI systems are never listed as authors. This is non-negotiable. The ICMJE authorship criteria require accountability, which an AI system cannot bear; AI use therefore appears in Acknowledgments or Methods, never in the author byline.

Every output published under the unit's name includes an **AI-Use Disclosure** paragraph, located in the Methods section when AI touched data, analysis, or figure generation, and in Acknowledgments when AI use was limited to drafting, editing, or summarization. The disclosure specifies: which AI system was used (name and version), which sections or operations it contributed to, whether prompts and outputs are archived (default: yes), and where the archive lives.

For every publication, the corresponding `ai-use-disclosure.md` file in the publication folder contains the full archive of prompts and any non-trivial outputs that materially shaped the work. The published paper references this archive by its Zenodo DOI.

When AI assistance reaches the level of substantive analytical contribution — running analyses, generating new model interpretations, drafting whole sections — the disclosure is upgraded to itemize each contribution, and a human author signs an explicit accountability statement for the AI's output.

## 8. Pre-registration protocol

Tier C studies and Tier T meta-analyses require pre-registration on the Open Science Framework using the standard COS preregistration template (or AsPredicted's nine-question form where appropriate). The pre-registration must be time-stamped before any data is collected or any analysis touches the data.

Each pre-registration contains, at minimum: the research question, the directional hypothesis or hypotheses, the design and sampling plan with justified target n, the operational definitions of every variable, the primary and secondary outcomes named explicitly, the analysis plan including the exact statistical tests and decision rules, the falsification criteria, and the conditions under which the study would be abandoned.

A copy of the time-stamped pre-registration is committed to the unit's `preregistrations/` directory at the time of registration, named per §14. Any deviation from the pre-registration is reported in the eventual publication's "Deviations from Pre-Registration" section. Undisclosed deviations are a serious breach and trigger a charter-level review.

## 9. Reproducibility bundle standard

Every Tier C, E, and M output ships with a Reproducibility Bundle that satisfies, at minimum, the NeurIPS Paper Checklist for ML work and the Transparency and Openness Promotion (TOP) guidelines at Level 2 for behavioral/empirical work. The bundle contains:

The full source code for data collection, analysis, and figure generation, frozen at a tagged commit; a complete dependency specification including a lockfile (Python: `pip-tools` or `uv` lockfile; conda: explicit `environment.yml` with pinned versions); the data, or — when data cannot be released — a pointer plus cryptographic checksums plus a documented access procedure; the random seeds, hyperparameters, and any non-deterministic operations made deterministic where possible; the prompts and prompt templates used with any AI system; a `PROVENANCE.md` describing the chain from raw data to published figure; a runnable replication script (`make replicate` or equivalent) that re-derives the headline figures from raw inputs; a brief reproduction log recording that the founder (or, in future, an independent third party) ran the bundle end-to-end on a fresh machine and recovered the published results.

The bundle is archived at Zenodo via the GitHub–Zenodo integration; a DOI is minted per release and cited in the published paper.

## 10. Internal lab notebook

The lab notebook is a continuous, dated record of research activity. Entries are markdown files committed to the `notebooks/` directory, organized by year and month. Entries are not retroactively edited; corrections take the form of a new entry that cites the original.

Each entry contains: a date and time, a short title, the project or projects it touches, a free-form record of what was tried, what worked, what failed, what was learned, and any decisions taken. Dead ends are recorded as fully as successes. Where AI assistance played a meaningful role in a session, the entry notes which AI, the prompt strategy, and a link to or excerpt from the transcript.

The procedure for preserving an AI-session transcript referenced by a notebook entry depends on the stake of the session. Every AI-assisted session falls into exactly one of three categories.

A **publication-touching session** is one whose AI assistance materially shapes a forthcoming publication's methods, analysis, code, figures, or text. The full prompt-and-output archive is committed to that publication's `ai-use-disclosure.md` per §7 and the AI Use Policy. The notebook entry cites the publication's `ai-use-disclosure.md` by path; no separate transcript mirror is required in `notebooks/`.

A **charter- or standards-touching session** is one whose AI assistance shapes a charter amendment, a standards refinement, a template, or any unit-level policy decision. The transcript — or its decision-relevant excerpts, with a one-line rationale for any redaction — is committed to `notebooks/YYYY/MM/_transcripts/YYYY-MM-DD_short-title_transcript.md`. The corresponding notebook entry cites the transcript file by path.

An **operational session** is one whose AI assistance produces no published artifact and touches no unit-level standard (build, test, dogfooding, scaffolding, bootstrap). The notebook entry records the vendor session identifier (URL or API session ID) and a one-line rationale for why no transcript is preserved. No transcript mirror is required.

The operator classifies each session into exactly one of these three categories at the time of writing the notebook entry. When in doubt, the operator mirrors rather than omits.

The notebook is the primary evidence that the unit conducted its research as it claims. Published papers reference relevant notebook entries by their committed file path.

## 11. Ethics, risk, and dual-use review

The unit takes ethical and dual-use considerations seriously even when no external IRB or review board has jurisdiction over its work.

The v0 scope is explicitly limited to founder self-experimentation, computational studies of AI systems, and analyses of publicly available data. The unit does not recruit or run human subjects beyond the founder in v0. Should the scope expand in v1 or beyond, the unit will identify and contract with an appropriate Institutional Review Board (commercial options such as WCG, Advarra, or Pearl IRB serve independent researchers) or equivalent independent ethics review service before any recruitment begins, and this charter will be amended.

Self-experimentation by the founder is permitted under the unit's standards, with the following constraints: it is disclosed prominently in every output (including in the abstract where applicable); single-subject results are never generalized beyond the founder without an independent multi-subject follow-up; and the SCRIBE 2016 reporting guidelines for single-case experimental designs are followed where applicable.

Every project's Scoping Memo (§5, Gate 2) includes a Dual-Use and Responsible-Release section that asks: could this research, if released as planned, materially uplift a malicious actor? If the answer is anything other than a confident no, the project triggers a Responsible-Release Review before any external release. The review considers staged release, capability-threshold gating, model cards (per Mitchell et al. 2019), and pre-release consultation with relevant safety teams. US federal dual-use research policy is in a transitional state as of mid-2026; the unit defers to current NIH guidance where applicable and otherwise operates by analogy to the most recent stable framework.

## 12. Authorship, credit, and conflicts of interest

Authorship on outputs published by the unit follows the four ICMJE criteria: substantial contribution to conception/design or data; drafting or critical revision; final approval; accountability for the integrity of the work. All four must be satisfied. Anyone who satisfies fewer than all four appears in Acknowledgments.

When and if collaborators join, an authorship agreement is signed at project kickoff specifying the lead author, the corresponding author, the contribution of each author against the CRediT taxonomy, and the agreed order. The agreement is committed to the project folder.

Conflicts of interest are disclosed using the ICMJE Disclosure Form on a per-publication basis (committed to each publication folder) and as an annual snapshot (committed to the repo root each calendar year in `coi/YYYY_founder-disclosure.md`), regardless of whether the venue requires it. The founder's financial interest in any company whose products are evaluated or referenced is disclosed by default. The unit's standing tooling-and-vendor dependencies (notably Anthropic, as the primary AI provider) are stated in the repo `README.md` and restated in each publication's Methods section.

## 13. Licensing and IP

The unit adopts the following default licenses: Apache-2.0 for code; CC-BY-4.0 for written content, data, and figures; CC0 for trivial artifacts (configuration files, ancillary scripts) where attribution would be a burden. The choice of Apache-2.0 over MIT reflects the explicit patent grant; the choice of CC-BY-4.0 over CC-BY-SA reflects a preference for maximum downstream reuse, including in proprietary settings. Each publication folder inherits these defaults; deviations are documented in the folder's README.

Each publication folder includes its own LICENSE files inheriting from the repo defaults; deviations require explicit documentation in the folder's README.

When external data with restrictive licenses is used, the publication's README documents the license and the unit honors the more restrictive terms.

Patentable inventions are not anticipated for the unit's research, but if any arises, the founder reserves all rights and will document the assignment posture in an amendment.

## 14. Naming conventions

All artifacts that may need to be cited, retrieved, or related back to their originating workspace follow a standard naming pattern:

`YYYY-MM-DD_source-repo_short-kebab-title_vN.ext`

The date is the date of preparation (or, for pre-registrations, the registration date). The source-repo is the slug of the originating project repository, or `founding-session` for unit-level documents, or `cross-repo` for outputs aggregating multiple repos. The short-kebab-title is two to five hyphenated lower-case words. The version is `v0`, `v1`, etc.; pre-publication revisions live as `_v0-draft-N`. The extension reflects the artifact.

Examples:

- `2026-05-24_founding-session_CHARTER_v0.md`
- `2026-07-15_personality-steering-qwen_PREREG_v0.md`
- `2026-09-02_personality-steering-qwen_MANUSCRIPT_v1.pdf`
- `2027-01-10_cross-repo_meta-review_PREREG_v0.md`

Folders inside `publications/` follow the same pattern minus the extension.

## 15. Publication and venue strategy

The unit's default disposition is preprint-first. Every Tier C, E, and M output is posted to an appropriate preprint server (arXiv for ML/CS, PsyArXiv for psychology, OSF Preprints for interdisciplinary work) before or simultaneously with journal/conference submission. The preprint cites the unit's Zenodo DOI for the reproducibility bundle.

Venue choice for each project is decided at the Scoping Memo gate, not after results are known, and recorded in writing. Choosing a venue post hoc on the basis of result favorability is a defect.

Where possible, the unit pursues Registered Reports for Tier C work, accepting in-principle review of the protocol before data collection. This protects against publication bias and matches the unit's stated principle of falsifiability.

**Null and negative findings.** The unit treats null and negative results as first-class outputs. Every Tier C and Tier E study completed under the unit's name is published with equal effort to positive findings: preprinted, accompanied by a full reproducibility bundle, and submitted to a peer-reviewed venue when a venue is appropriate (PLOS ONE, Royal Society Open Science, the *Journal of Articles in Support of the Null Hypothesis*, or the originally chosen Tier C journal when it accepts null results). Choosing not to pursue formal submission of a null requires written justification in the project's Lab Notebook entry; "the result wasn't interesting enough" is not such a justification. This commitment is part of the unit's external identity: a track record that publishes its nulls is a track record reviewers can trust.

The unit does not pursue press coverage or non-peer-reviewed promotion of its results.

## 16. Governance and internal review

In v0, the unit's review function is performed by Claude under a structured review prompt (the prompt is itself a versioned artifact in `templates/`), counter-signed by the founder. This is acknowledged as the weakest part of v0's posture and is disclosed in every paper this arrangement touches.

The path to v1 governance is staged. As soon as one external collaborator joins, internal review duty transfers to that human, with AI review becoming supplementary, **and** the unit will simultaneously seek one named external advisor — a senior researcher in a relevant field who reviews a sampling of outputs annually without authorship rights. This pairing (first human collaborator + first external advisor) is the v1 governance milestone. The unit does not seek an external advisor before this point: a one-person unit with an external advisor has nothing for the advisor to review and creates a relationship that is hard to scope. As a second external collaborator joins, a rotating two-person internal review is implemented. Beyond three contributors, the unit establishes a formal internal review board with a written charter.

The charter itself is reviewed at least annually, and immediately after any incident, near-miss, or external criticism that bears on the unit's standards. Amendments are recorded in `CHANGELOG.md` with date, rationale, and the studies (if any) affected.

## 17. Standards referenced by this charter

The charter draws on, and intends to remain consistent with, the following external standards. The full annotated bibliography lives in `references/references_v0.md`.

ICMJE Recommendations on Authorship and AI Use (current edition). The four authorship criteria; the prohibition on AI as author; the disclosure standard for AI use.

OSF Preregistration Templates (Center for Open Science). The canonical template structure for Tier C pre-registration.

Registered Reports model (Center for Open Science). The mechanism the unit prefers for Tier C confirmatory work where the venue supports it.

NeurIPS Paper Checklist and the ML Reproducibility Checklist (Pineau et al.). The minimum reproducibility standard for ML work.

TOP Guidelines (Center for Open Science). Operates the unit's reproducibility bundle at Level 2 across the eight TOP standards.

Munafò et al. (2017), "A manifesto for reproducible science," *Nature Human Behaviour*. The conceptual frame for the unit's posture on reproducibility, incentives, and reporting.

FAIR Data Principles (Wilkinson et al., 2016) and the GO FAIR operational guidance. The standard governing the unit's data releases.

SCRIBE 2016 Statement (Tate, Perdices, Rosenkoetter, et al.). The reporting standard for any single-case experimental design the unit produces.

Mitchell et al. (2019), "Model Cards for Model Reporting." The template for documenting any model the unit releases.

FORCE11 Software Citation Principles. The basis for the unit's CITATION.cff and Zenodo DOI workflow.

Citation File Format (CFF) specification. The format for the unit's `CITATION.cff`.

ICMJE Disclosure of Interest Form. The COI standard adopted by default for every publication.

PRISMA 2020 Statement. The reporting standard for any systematic review or meta-analysis (Tier T).

The Turing Way (community handbook). A continuing reference for reproducible and ethical practice.

## 18. Open questions and decision points

The v0 founding decisions are resolved in the body of this charter. As of v0.0.4, the two original v1 open questions are also both closed: the hardened Gate-6 internal-review prompt lives at `templates/internal-review-prompt_v1.md` (closed at v0.0.3), and the CI maturity-progression triggers are ratified below (closed at v0.0.4). No genuine open questions remain for v1; the next charter review is the scheduled annual review per §16.

**CI maturity progression (ratified at v0.0.4).** v0 ships with the *Light* tier — `scripts/check-publication-structure.sh` plus the GitHub Actions workflow `.github/workflows/structure-check.yml` — invoked on every push and pull request touching `publications/`. The upgrade triggers and procedure are now fixed:

- *Light → Medium* (adds link/DOI validation, lockfile integrity checks, and citation-target reachability). Triggers, whichever comes first: (a) a published reference, DOI, or external link in any released publication 404s; (b) a third party reports they could not replicate because a lockfile or dependency drifted out from under the bundle.
- *Medium → Heavy* (adds on-tag end-to-end `make replicate` runs of the reproducibility bundle in fresh containers). Triggers, whichever comes first: (a) a real (non-DEMO) publication's reproducibility bundle silently breaks between release and a downstream replication attempt; (b) the unit reaches three concurrent Tier C / Tier E / Tier M publications under active maintenance.

When a trigger fires, the operator opens a CHARTER amendment within seven days naming the triggering incident or condition, bumps the charter version, and only then implements the upgraded CI tier. CI does not quietly upgrade: every upgrade is a deliberate, recorded act with the triggering event on the permanent record.

The following items were considered during v0 founding and resolved as follows, and are recorded here for clarity rather than as open questions:

- *Default licenses:* Apache-2.0 (code) + CC-BY-4.0 (content), per §13. LICENSE-CODE and LICENSE-CONTENT files committed at v0.0.3.
- *IRB posture in v0:* self-experimentation only; no external recruitment; IRB partner identified at v1 if scope expands, per §11.
- *COI cadence:* per-publication + annual snapshot, per §12.
- *Null/negative findings:* equal-effort publication commitment, per §15.
- *AI-provider disclosure:* standing statement in README + per-paper Methods, per §12.
- *Dual-use posture:* case-by-case at the Scoping Memo gate, per §11.
- *External advisor:* sought when the first non-founder collaborator joins, paired with the human-review transition, per §16.
- *Gate-6 review prompt:* hardened structured prompt committed at v0.0.3 as `templates/internal-review-prompt_v1.md`.
- *CI maturity progression:* triggers and procedure ratified at v0.0.4 (see body of this section above).

## 19. Adoption

The unit was adopted when the founder committed the charter to the `mdfy-ai-research-facility` repository as `CHARTER.md` on the `main` branch and tagged the commit `v0.0.3-charter` on 2026-05-24. The repository's README and CITATION.cff were populated at the same commit. No research output may bear the unit's name until adoption is complete; adoption is one-time, and the `v0.0.3-charter` tag is retained as the permanent founding marker. Subsequent charter amendments (the first being v0.0.4 on 2026-05-24) update the charter in effect but do not re-adopt the unit; each amendment is recorded in `CHANGELOG.md` with its own annotated tag.

A worked-example publication folder at `publications/2026-05-24_example_demo-publication_v0/` demonstrates a Tier-M-compliant publication structure and is retained in the repository as a structural reference. It is clearly labelled as a DEMO and is not for external citation or release.

---

*Cite this charter as:*
Weakley, R. (2026). *mdfy-ai-research-facility Charter & Operating Manual, v0.0.4.* Zenodo. https://doi.org/10.5281/zenodo.20365323 (version DOI). Concept DOI (resolves to latest version): https://doi.org/10.5281/zenodo.20365321. Source: https://github.com/cybernaut6404/mdfy-ai-research-facility.
