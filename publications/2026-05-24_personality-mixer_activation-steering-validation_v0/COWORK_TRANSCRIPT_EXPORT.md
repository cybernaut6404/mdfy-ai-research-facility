# Cowork transcript export — procedure

Per `AI_USE_POLICY.md` §"Archive requirements" and CHARTER §10 (transcript-mirror procedure for **publication-touching sessions**), every Tier 3 / Tier 4 publication must commit a prompt archive of the AI sessions that materially shaped the manuscript. This file is the operator's guide to exporting the relevant Cowork sessions for this publication and committing them to `prompts/` in this folder.

**Status:** ⏳ pending Rick's manual export. This is the last open closure before arXiv preprint posting (per `ARXIV_SUBMISSION_README.md` item 6).

---

## Which sessions to export

Two distinct Cowork sessions touched this publication:

### Session 1 — the originating draft (highest priority)

**When:** 2026-05-23 → 2026-05-24 morning, before unit adoption.
**Where:** Cowork session(s) on the MacMini.
**What it produced:** MANUSCRIPT.md, SUPPLEMENTARY_TABLES.md, ROADMAP_TO_TOP_VENUES.md, WORK_LOG.md, the original pack README.md, the Makefile (pandoc rendering), the validation harness extensions (mg-digital-twin commits 9260aa8, 1c0f4ce, 6d02ed3, ecefbae, f492844), the channel_set 2.0.0 + 2.1.0 publishes, the shadow-archetype re-weight (central-db commits b5051be, 72a2c1f, 2bdf13b), the runner activation-steering wire (runner commits e22f36a, 9ace574, d55296b), and the Modal steering-server deployment (mg-twin 9260aa8).
**AI model used:** `claude-opus-4-7` (per `analyse.py` source); WORK_LOG also references `claude-opus-4-6` and `claude-opus-4-7-1m` for different portions of the work.
**Tier classification (per CHARTER §10):** publication-touching session.
**Disposition:** Tier 3 + Tier 4 (per `ai-use-disclosure.md` §2.3 — drafting was Tier 3, the three methodological findings + RLHF-floor framing + 4-tier ROADMAP structure + "overturns" verb choice + sycophancy reminder + multi-layer recommendation + publishability assessment + Broader Impacts content were Tier 4 originations Rick accepted).

### Session 2 — the unit-intake + v1 revisions (also publication-touching)

**When:** 2026-05-24 afternoon, after unit adoption (v0.0.3-charter founding commit).
**Where:** Claude Code session on the MacBook (Rick's primary research machine).
**What it produced:** the bootstrap commits, the personality-mixer pack intake commit `827669c`, the Gate-6 internal-review.md (via a sub-agent), the Gate-6 counter-signature in `6f62989`, the v1 manuscript revisions in `ef45b3b`, the Zenodo DOI integration in `d65380a`, the ORCID + email canonicalization in `d67845f`, the autonomous-mode pre-arXiv work (stats analysis, figures, bibliography, real `make replicate`) in `49490e9`, and this very checkpoint commit.
**AI model used:** `claude-opus-4-7-1m`.
**Tier classification:** publication-touching session.
**Disposition:** Tier 3 + Tier 4 (the v1 manuscript-revision content includes Tier 4 framings — softened verbs, alternative-explanations enumeration for sadism, Broader Impacts subsection content; documented in `ai-use-disclosure.md` §2.3 with v1-revision annotations).

---

## Export procedure for Session 1 (Cowork on the MacMini)

Cowork (Anthropic's coding-collaboration product) does not currently offer a one-click bulk-export of session transcripts. Three options to assemble Session 1's archive:

### Option A — manual copy-paste per session (slow but reliable)

1. Open Cowork on the MacMini.
2. Navigate to the session list / history.
3. For each session in the work-window 2026-05-23 → 2026-05-24 morning:
   - Open the session.
   - Click "Share" → "Copy session as text" (or equivalent — exact UI string depends on the Cowork build).
   - Paste into a file: `prompts/session_<NN>_<short-title>.md` in this publication folder.
4. After all sessions are pasted, write `prompts/INDEX.md` summarising which session produced which artifact.
5. Run `bash scripts/check-publication-structure.sh` from the repo root — should still pass.

### Option B — Anthropic account export (faster if available)

1. Sign into your Anthropic account at https://console.anthropic.com.
2. Settings → Data → "Export all data" (if available — this is account-level export, may include conversations).
3. Filter the export for Cowork sessions in the work-window.
4. Convert to markdown and commit to `prompts/`.

### Option C — Anthropic Support assistance

If Options A/B are unworkable:
1. Email support@anthropic.com requesting a Cowork session-data export for the 2026-05-23 → 2026-05-24 window.
2. Cite the publication's intended use (research-reproducibility prompt-archive deposition per ICMJE AI Use guidance).
3. Anthropic will typically respond within 1–3 business days.

## Export procedure for Session 2 (Claude Code on this MacBook)

Claude Code's session transcripts are stored locally. To export:

```bash
# Find Claude Code transcripts for this workspace
ls /private/tmp/claude-501/-Users-richardweakley-ai-workspace-mdfy-ai-research-facility/

# The session-transcript JSON files live at the path above (per Claude Code's
# storage convention as of 2026-05-24). For the autonomous-mode session
# starting at the timestamp of this commit, the file path follows the pattern:
# /private/tmp/claude-501/<workspace-slug>/<session-uuid>/tasks/*.output
```

Convert the relevant `.output` files to markdown and commit to `prompts/`. The
session-uuid for this autonomous-mode run can be found in the system context.

## Redactions

Per `AI_USE_POLICY.md` §"Archive requirements", redactions are permitted with rationale. Specifically:

- **Anthropic API keys / Modal tokens / Supabase credentials** must be redacted from the export. Replace with `[REDACTED — credential]` and note in `prompts/REDACTIONS.md`.
- **Personally-identifying information of third parties** (none expected in this work since the only subject is Rick himself, but check).
- **Discussions of unrelated work** (other repos, personal matters) that may have come up in the same session may be redacted with rationale.

Document every redaction in `prompts/REDACTIONS.md` per the unit's standard.

## Verification

After export:

1. `ls prompts/` should show at least one session file plus `INDEX.md` and `REDACTIONS.md` (if any redactions made).
2. `MANUSCRIPT.md` §"Author note" + `ai-use-disclosure.md` should reference the `prompts/` directory; the references already exist as forward-looking notes ("to be deposited at `prompts/`"). After export, update them to past tense.
3. Commit:
   ```
   git add prompts/ MANUSCRIPT.md ai-use-disclosure.md
   git commit -m "publication: deposit Cowork session transcripts as prompt archive (Gate-7 closure for AI_USE_POLICY archive requirement)"
   git push origin main
   ```
4. arXiv submission item 6 is now ✅.

## If you can't recover the original Cowork sessions

If the sessions are unrecoverable (deleted, account migration, etc.), the
unit's standard says document the gap rather than fabricate. Create
`prompts/RECOVERY_NOTE.md` explaining:
- What sessions were lost and approximately when.
- What information about those sessions IS preserved (the commit chronology
  in WORK_LOG.md §3 names every commit; the git history names every change;
  the contrastive items + probe libraries are committed; the rubrics are
  committed verbatim in `analyse.py::JUDGE_PROMPTS`).
- That the prompt archive cannot be reconstructed.

The unit's transparency-over-polish standard (CHARTER §2) accepts this
honest disclosure as a closure, even if it's a weaker closure than the
full archive. Reviewers can verify the deterministic-content claims (probes,
rubrics, contrastive items) directly from the committed source; only the
session-flow context is lost.
