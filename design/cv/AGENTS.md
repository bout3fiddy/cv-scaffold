# CV design

Read [the design reference](../DESIGN.md) before styling work. `build.py`
contains shared helpers and the quantitative layout. `swe_layout.py` owns the
standard layout; `strategy_layout.py` owns aligned dates. Store references
under `references/` here and keep the specification in DESIGN.md current.

Use `python build.py --all` and `python qa.py` from the repository root.
Inspect all affected PDF and DOCX pages after a visible design change. For a
file move, byte-identical exports retain the previous visual review evidence.
Keep content edits in the HTML sources and retain font redistribution terms.

## Build variants and previews

From the repository root, use the selected Python runtime:

```sh
python build.py --variant swe
python build.py --variant strategy
python build.py --variant quant
python build.py --all --format pdf
python build.py --variant swe --source personal/master/resume.html --stem resume --output-dir personal/master/outputs
python qa.py
```

The default build produces both PDF and DOCX for the standard CV. QA without
arguments checks all registered examples and the example letter; build that
letter before the full check. Personal sources use the explicit-file checks
in `../../personal/AGENTS.md`.

To refresh the README's first-page preview:

```sh
pdftoppm -f 1 -singlefile -scale-to 1200 -png output/avery-quill-swe.pdf output/avery-quill-swe
```

Inspect every page of a changed export, including pages omitted from the README
preview. Install the local fonts in the Word review environment. Word and
LibreOffice pagination can differ from the ReportLab PDF. Keep the PDF as the
reference for exact layout.
