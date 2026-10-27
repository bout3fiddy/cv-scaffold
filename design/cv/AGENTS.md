# CV design

Read README.md for the Paper/Figma workflow and token map. `build.py` contains
shared helpers and the quantitative layout. `swe_layout.py` owns the standard
layout; `strategy_layout.py` owns aligned dates. CSS and Python must agree on
typography and spacing. Store design references under `references/` here.

Use `python build.py --all` and `python qa.py` from the repository root.
Inspect all affected PDF and DOCX pages after a visible design change. For a
file move, byte-identical exports retain the previous visual review evidence.
Keep content edits in the HTML sources and retain font redistribution terms.
