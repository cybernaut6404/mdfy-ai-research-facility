# `correspondence/` — review correspondence + journal letters

This directory is the canonical home for:
- Editor and reviewer correspondence at each submission venue
- Response-to-reviewers documents (per submission round)
- Decision letters (accept / minor / major revisions / reject)
- Any pre-submission inquiry correspondence (e.g. Registered Reports
  pre-acceptance discussions)

## Current contents

*Empty as of 2026-05-24.* No external submission has been made for this
publication. Per ROADMAP_TO_TOP_VENUES.md §"Recommended sequencing", the
first submission will be an arXiv preprint posting, which does not produce
correspondence (arXiv is not editorialised). The first correspondence-
generating submission will be the TMLR pass (Tier 1 of the roadmap) or a
NeurIPS / ICLR workshop submission.

## Naming convention

When correspondence accumulates, file names follow:

```
YYYY-MM-DD_venue_kind_v<N>.{pdf,md,eml}
```

Examples:

- `2026-07-15_tmlr_submission-letter_v0.md` — cover letter at first
  submission
- `2026-08-02_tmlr_reviewer-1_v0.md` — reviewer's full report
- `2026-08-02_tmlr_reviewer-2_v0.md`
- `2026-08-02_tmlr_action-editor_v0.md`
- `2026-08-12_tmlr_response-to-reviewers_v0.md` — author response
- `2026-08-15_tmlr_revised-submission_v1.md` — manuscript revision letter

Where the correspondence is from the venue and arrives in HTML / EML
form, preserve the original and add a `.md` extract of the key content
for searchability.

## Privacy

Reviewer identities (where known or guessable) are NOT recorded in this
directory. Only the venue-assigned anonymous identifier ("Reviewer 1",
"Action Editor") is used. If a reviewer self-identifies after the fact,
their identity is not added to historical records.

## Cross-reference

When a manuscript revision is made in response to reviewer feedback, the
`deviations.md` is updated with the revision rationale and cross-
referenced to the relevant correspondence file in this directory.
