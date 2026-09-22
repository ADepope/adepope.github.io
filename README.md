# adepope.github.io

Personal academic website of [Al Depope](https://adepope.github.io) — Postdoctoral Researcher at the
Institute of Science and Technology Austria (ISTA).

Built with [Jekyll](https://jekyllrb.com/) on top of the
[Contrast](https://github.com/niklasbuschmann/contrast) theme, with a custom stylesheet layered on
top. No external requests: fonts, icons and KaTeX are all vendored.

## Structure

| Path | What it is |
| --- | --- |
| `index.md` | Home page — hero, bio, highlights and news timeline |
| `research.html` | Project list, generated from the `_publications` collection |
| `publications.html` | Papers, preprints and talks |
| `software.html` | Open-source repositories |
| `cv.html` | CV rendered as HTML |
| `gvamp_tutorial.md` | gVAMP tutorial (KaTeX math, `mathjax: true`) |
| `_publications/*.md` | One file per project — front matter drives the cards on `research.html` |
| `assets/css/custom.css` | All custom styling and the light/dark design tokens |
| `assets/cv/Al_Depope_CV.tex` | LaTeX source of the CV |

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

## Adding a project

Drop a file in `_publications/`. The front matter fields that matter:

```yaml
---
layout: page
title: Project title
authors: A. Author, B. Author
year: 2026
order: 50            # controls position on /research/ (higher = first)
status: Work in progress
teaser: slug_small.svg   # optional; defaults to images/<slug>_small.jpg
doi: https://...         # optional link buttons
preprint: https://...
code: https://...
pdf: true                # looks for download/<slug>.pdf
summary: One paragraph shown on the research page.
---
```

## Updating the CV

`cv.html` is the canonical, always-current version. To also offer a PDF, compile
`assets/cv/Al_Depope_CV.tex`, commit the result next to it, and point `cv_pdf` in `_config.yml` at
it — the download button appears automatically.

## Icons

Icons come from a generated sprite at `assets/fontawesome/icons.svg`. To use a new Font Awesome 5
free icon anywhere on the site, add its name to `extra_icons` in `_config.yml`, then:

```liquid
{% include icon.html name="microscope" %}
```

## License

Site content © Al Depope. Theme and tooling: [public domain](http://unlicense.org/).
