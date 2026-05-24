# NeurIPS Paper Checklist — [PUBLICATION TITLE]

Per `mdfy-ai-research-facility` STANDARDS.md Tier-M ML-work checklist,
completed against the NeurIPS Paper Checklist Guidelines. This is the unit's
reproducibility floor for any ML methods publication.

For each item: answer Yes / No / N/A, with evidence (manuscript section,
bundle file path) and any partial / TODO status flagged explicitly. TODO
items are acceptable for arXiv preprint posting if disclosed; must close
before any NeurIPS / TMLR / ML-venue submission.

---

## 1. Claims

**Q:** Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?

**Answer:** [Yes / No / Partial — with explanation]

**Evidence:** [manuscript sections; deviations.md cross-references; Gate-6 calibration flags]

## 2. Limitations

**Q:** Does the paper discuss the limitations of the work performed by the authors?

**Answer:** [Yes / No / Partial]

**Evidence:** [manuscript Limitations section with numbered items]

## 3. Theory assumptions and proofs

**Q:** For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

**Answer:** [Yes / No / N/A]

## 4. Experimental result reproducibility

**Q:** Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper?

**Answer:** [Yes / Partial — bundle in stub state / No]

**Evidence:** [reproducibility-bundle structure status; PROVENANCE.md; environment.yml]

## 5. Open access to data and code

**Q:** Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

**Answer:** [Yes / Access-on-request / No]

**Evidence:** [reproducibility-bundle/code/README.md access procedure; data/README.md license + provenance]

## 6. Experimental setting/details

**Q:** Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

**Answer:** [Yes / Partial / No]

**Evidence:** [manuscript Methods section; environment.yml; seeds.json]

## 7. Experiment statistical significance

**Q:** Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

**Answer:** [Yes / No — load-bearing TODO]

**Evidence:** [confidence intervals; effect sizes; binomial tests; multiple-comparisons correction]

**Note:** This item is the most common gap for proof-of-concept ML methods work. Closure typically requires a half day of scipy.stats work: 95% CIs on point estimates, binomial tests vs chance per channel/condition, Bonferroni or BH-FDR correction across the family of comparisons. If TODO at v0, must close before any external submission beyond raw arXiv.

## 8. Experiments compute resources

**Q:** For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

**Answer:** [Yes / Partial / No]

**Evidence:** [manuscript Methods §"Engineering scaffolding"; SUPPLEMENTARY_TABLES "Compute and cost provenance"; reproducibility-bundle README]

## 9. Code of ethics

**Q:** Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics?

**Answer:** [Yes / Concerns flagged]

**Evidence:** [human subjects status; IRB if applicable; dual-use considerations; privacy / data protection]

## 10. Broader impacts

**Q:** Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

**Answer:** [Yes / Partial / No — TODO before NeurIPS submission]

**Evidence:** [manuscript Broader Impacts subsection; mitigations enumerated; cross-references to deviations.md and COI]

## 11. Safeguards

**Q:** Does the paper describe safeguards that have been put in place for responsible release of data or models with a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)?

**Answer:** [Yes / Partial / N/A]

**Evidence:** [Model Card if released; refusal-cosine / safety probe status; access-on-request gating; responsible-release review per CHARTER §11]

## 12. Licenses for existing assets

**Q:** Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

**Answer:** [Yes / Partial / No]

**Evidence:** [References section citations; license respect for any redistributed assets; data/README.md license documentation]

## 13. New assets

**Q:** Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

**Answer:** [Yes / Partial / No]

**Evidence:** [per-asset README files; PROVENANCE.md for derivation chain]

## 14. Crowdsourcing and research with human subjects

**Q:** For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

**Answer:** [Yes / N/A — no crowdsourced or human-subjects experiments / Founder-only self-experimentation, disclosed in §X]

## 15. Institutional review board (IRB) approvals

**Q:** Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

**Answer:** [IRB letter committed / N/A — author-only self-experimentation per CHARTER §11 / N/A — computational study with no human subjects]

## 16. Author contributions

**Q:** (For multi-author work) Does the paper specify the contributions of each author?

**Answer:** [Yes — CRediT taxonomy in §X / N/A — sole-authored]

---

## Summary

| Item | Status |
|---|---|
| 1. Claims | [Yes / Flagged] |
| 2. Limitations | [Yes / Partial] |
| 3. Theory / proofs | [Yes / N/A] |
| 4. Experimental reproducibility | [Yes / Partial / Bundle TODO] |
| 5. Open access to data and code | [Yes / Access-on-request / Public-release TODO] |
| 6. Experimental setting/details | [Yes / Partial] |
| 7. Statistical significance | [Yes / Load-bearing TODO] |
| 8. Compute resources | [Yes] |
| 9. Code of ethics | [Yes / Concerns flagged] |
| 10. Broader impacts | [Yes / TODO] |
| 11. Safeguards | [Yes / Partial / N/A] |
| 12. Licenses for existing assets | [Yes] |
| 13. New assets | [Yes / TODO] |
| 14. Crowdsourcing / human subjects | [N/A / Self-experimentation only] |
| 15. IRB | [N/A / Letter committed] |
| 16. Author contributions | [N/A / CRediT in §X] |

**Bottom line:** [acceptability at arXiv with disclosed gaps; not yet acceptable at NeurIPS main track until items X, Y, Z close; per the ROADMAP].

---

*Completed by:* [Claude (model version) / human author] per `templates/internal-review-prompt_v1.md` workflow OR independently as part of pre-Gate-6 preparation.
*Date:* [YYYY-MM-DD]
*Counter-signed by:* [HUMAN NAME] as the v0.0.4 Gate-6 procedure.
