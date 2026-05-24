# Regenerate alternate formats from the canonical .md sources.
#   make            — regenerate .tex + .docx for all manuscripts
#   make pdf        — also regenerate .pdf (requires LaTeX engine; brew install basictex)
#   make clean      — remove generated artifacts
#
# Canonical source is .md; never edit .tex/.docx/.pdf by hand (will be overwritten).

SRCS := $(wildcard *.md)
TEXS := $(SRCS:.md=.tex)
DOCXS := $(SRCS:.md=.docx)
PDFS := $(SRCS:.md=.pdf)

# Citation processing: pandoc citeproc + references.bib (when present).
# Currently the manuscript's References section is illustrative text; the
# .bib is available for pandoc citeproc and will be used once the
# manuscript transitions to @cite-key syntax (a future v2 revision).
BIBLIOGRAPHY := references.bib
ifneq ("$(wildcard $(BIBLIOGRAPHY))","")
	CITEPROC := --citeproc --bibliography=$(BIBLIOGRAPHY)
else
	CITEPROC :=
endif

.PHONY: all pdf clean
all: $(TEXS) $(DOCXS)
	@echo "regenerated $(words $(TEXS)) .tex and $(words $(DOCXS)) .docx files"

pdf: $(PDFS)

%.tex: %.md $(BIBLIOGRAPHY)
	pandoc -f markdown -t latex --standalone $(CITEPROC) -o $@ $<

%.docx: %.md $(BIBLIOGRAPHY)
	pandoc -f markdown -t docx $(CITEPROC) -o $@ $<

# PDF rule: math-Unicode handled via xelatex + STIX Two Text so the .md stays
# Unicode-pristine (AI-readable) for downstream tooling.
%.pdf: %.md $(BIBLIOGRAPHY)
	pandoc -f markdown -t pdf --pdf-engine=xelatex $(CITEPROC) \
	  -V geometry:margin=1in \
	  -V mainfont="STIX Two Text" \
	  -V monofont="Menlo" \
	  -o $@ $<

clean:
	rm -f $(TEXS) $(DOCXS) $(PDFS)
	rm -rf arxiv-submission/
	rm -f arxiv-submission.tar.gz

# ---- arXiv submission packaging ----
# `make arxiv` builds a self-contained tarball ready to upload to
# arxiv.org/submit/. Run before each new arXiv version.
.PHONY: arxiv
arxiv: MANUSCRIPT.tex references.bib
	@echo "==> assembling arxiv-submission/ package"
	@rm -rf arxiv-submission/
	@mkdir -p arxiv-submission/figures
	@cp MANUSCRIPT.tex arxiv-submission/main.tex
	@cp references.bib arxiv-submission/
	@cp SUPPLEMENTARY_TABLES.tex arxiv-submission/supplementary.tex
	@cp reproducibility-bundle/data/figures/fig1_kappa_forest.png arxiv-submission/figures/
	@cp reproducibility-bundle/data/figures/fig2_cosine_heatmap_L16.png arxiv-submission/figures/
	@cp reproducibility-bundle/data/figures/fig3_refusal_cosine.png arxiv-submission/figures/
	@echo "==> rewriting figure paths in main.tex to match arxiv layout"
	@sed -i.bak 's|reproducibility-bundle/data/figures/|figures/|g' arxiv-submission/main.tex
	@rm -f arxiv-submission/main.tex.bak
	@echo "==> writing 00README.XXX with arxiv engine directive"
	@printf 'engine: xelatex\n\n# The manuscript uses Greek letters (κ for directional accuracy)\n# and other Unicode characters that require xelatex; pdflatex will fail.\n# This file directs arXiv'\''s AutoTeX to use xelatex.\n' > arxiv-submission/00README.XXX
	@cp ARXIV_SUBMISSION_README.md arxiv-submission/README.md 2>/dev/null || true
	@echo "==> creating arxiv-submission.tar.gz"
	@tar -czf arxiv-submission.tar.gz arxiv-submission/
	@echo ""
	@echo "==> arxiv submission package ready"
	@ls -la arxiv-submission.tar.gz
	@du -sh arxiv-submission/
	@echo ""
	@echo "Contents:"
	@find arxiv-submission/ -type f | sort
	@echo ""
	@echo "Next steps:"
	@echo "  1. Inspect arxiv-submission/main.tex — sanity-check the figure paths and LaTeX compiles."
	@echo "  2. Read ARXIV_SUBMISSION_README.md for the step-by-step browser submission flow."
	@echo "  3. Go to https://arxiv.org/submit/ and upload arxiv-submission.tar.gz."
