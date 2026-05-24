# mdfy-ai-research-facility

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20365321.svg)](https://doi.org/10.5281/zenodo.20365321)

> An internal AI research unit operating to publication-grade standards.

This repository is the central research function shared across all of the founder's project repositories. Project repos produce experiments and code; this repo publishes, archives, and certifies the resulting research under the `mdfy-ai-research-facility` name.

## Read first

- [`CHARTER.md`](./CHARTER.md) — the founding charter; the single source of truth.
- [`STANDARDS.md`](./STANDARDS.md) — detailed tier standards and review checklists.
- [`AI_USE_POLICY.md`](./AI_USE_POLICY.md) — the unit's policy on AI assistance and disclosure.

## What lives where

`publications/` — one folder per published output, each containing the manuscript, the reproducibility bundle, the AI-use disclosure, and any correspondence.

`preregistrations/` — every pre-registration and exploration plan, time-stamped at the moment of registration.

`notebooks/` — the continuous lab notebook, organized by year and month.

`templates/` — the canonical templates referenced throughout the charter. Copy a template into a new project folder, fill it in, commit it.

`references/` — the unit's annotated bibliography of methods and standards.

## How to cite this repository

To cite the unit itself (resolves to the latest charter version):

> Weakley, R. (2026). *mdfy-ai-research-facility Charter & Operating Manual.* Zenodo. https://doi.org/10.5281/zenodo.20365321

To cite a specific charter version:

- v0.0.4-charter (current): https://doi.org/10.5281/zenodo.20365323
- v0.0.3-charter (founding): https://doi.org/10.5281/zenodo.20365322

Full citation metadata in [`CITATION.cff`](./CITATION.cff). For a specific publication produced by the unit, cite that publication's own Zenodo DOI (listed in the publication's folder README).

## Dependencies & tooling disclosure

This unit relies on the following tools and providers. This disclosure is restated, with model and version specifics, in the Methods section of every publication.

- **Anthropic Claude** — primary AI assistant for research drafting, code generation, exploratory analysis scripting, and internal review (Gate 6, v0). Relationship: standard customer-vendor (subscription and/or API). No financial relationship beyond payment for usage exists between the unit's founder and Anthropic as of this disclosure.
- **GitHub** — repository hosting. Relationship: standard customer-vendor.
- **Zenodo** — DOI minting for releases and reproducibility bundles, via the GitHub–Zenodo integration. No financial relationship.
- **Open Science Framework (OSF)** — pre-registration hosting. No financial relationship.

Changes to these relationships (sponsorship, advisory roles, equity, beta-access privileges) are recorded here and in `coi/YYYY_founder-disclosure.md` within the same calendar quarter.

## License

Code released under Apache-2.0 unless otherwise noted (see [`LICENSE-CODE`](./LICENSE-CODE)). Written content, figures, and data released under CC-BY-4.0 unless otherwise noted (see [`LICENSE-CONTENT`](./LICENSE-CONTENT)). Per-publication licenses are documented in each publication's folder.

## Contact

Rick Weakley — rick@minorgod.com
