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

.PHONY: all pdf clean
all: $(TEXS) $(DOCXS)
	@echo "regenerated $(words $(TEXS)) .tex and $(words $(DOCXS)) .docx files"

pdf: $(PDFS)

%.tex: %.md
	pandoc -f markdown -t latex --standalone -o $@ $<

%.docx: %.md
	pandoc -f markdown -t docx -o $@ $<

# PDF rule: math-Unicode handled via xelatex + STIX Two Text so the .md stays
# Unicode-pristine (AI-readable) for downstream tooling.
%.pdf: %.md
	pandoc -f markdown -t pdf --pdf-engine=xelatex \
	  -V geometry:margin=1in \
	  -V mainfont="STIX Two Text" \
	  -V monofont="Menlo" \
	  -o $@ $<

clean:
	rm -f $(TEXS) $(DOCXS) $(PDFS)
