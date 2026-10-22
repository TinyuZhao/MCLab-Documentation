# Minimal makefile for the Ednex / MC4 Sphinx documentation.

SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SPHINX_PARALLEL ?= 8
SOURCEDIR = source
BUILDDIR = build

ifneq ($(strip $(SPHINX_PARALLEL)),)
SPHINX_PARALLEL_FLAG = -j $(SPHINX_PARALLEL)
endif

.PHONY: help Makefile en html api-stubs check-api-stubs

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

en:
	@$(SPHINXBUILD) -W $(SPHINX_PARALLEL_FLAG) -b html -D language=en "$(SOURCEDIR)" "$(BUILDDIR)/html/en" $(SPHINXOPTS) $(O)

api-stubs:
	@python3 tools/generate_api_stubs.py

check-api-stubs:
	@python3 tools/generate_api_stubs.py --check

html: en

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
