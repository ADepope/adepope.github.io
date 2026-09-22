#!/usr/bin/env bash
# Compile assets/cv/Al_Depope_CV.tex to assets/cv/Al_Depope_CV.pdf.
# The CV page picks the PDF up automatically via `cv_pdf` in _config.yml.
set -euo pipefail

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
src="$repo/assets/cv/Al_Depope_CV.tex"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

# ISTA cluster: TeX Live comes from the module system.
if ! command -v pdflatex >/dev/null 2>&1; then
  if command -v module >/dev/null 2>&1 || [ -n "${LMOD_CMD:-}" ]; then
    # shellcheck disable=SC1090
    module load texlive
  fi
fi
command -v pdflatex >/dev/null 2>&1 || { echo "pdflatex not found (try: module load texlive)" >&2; exit 1; }

cp "$src" "$work/"
cd "$work"
# twice, so hyperref outlines and the page count settle
pdflatex -interaction=nonstopmode -halt-on-error Al_Depope_CV.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error Al_Depope_CV.tex >/dev/null

cp Al_Depope_CV.pdf "$repo/assets/cv/Al_Depope_CV.pdf"
echo "wrote assets/cv/Al_Depope_CV.pdf ($(ls -lh "$repo/assets/cv/Al_Depope_CV.pdf" | awk "{print \$5}"))"
