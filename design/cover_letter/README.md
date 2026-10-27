# Cover-letter design

`build.py` owns the letter's ReportLab layout. Run it through the root command:

```sh
python build_cover_letter.py
```

| Setting | Value |
| --- | --- |
| Typeface | JetBrains Mono |
| Body size | 10 pt |
| Line height | 15.5 pt |
| Space after each paragraph | 14 pt |
| Side and bottom margins | 42 pt |
| Top margin | 48 pt |
| Page | A4 |

Edit `ParagraphStyle` and `SimpleDocTemplate` in this folder's `build.py` to
change these values. Font registration and PDF metadata helpers are shared
with `../cv/build.py`; font files and their licence live in `../cv/fonts/`.

For a Paper or Figma reference, create an A4 portrait frame and set text and
margins to the values above. Multiply point values by 4/3 for CSS pixels.
Use the fictional letter during design work, then transfer chosen values to
the Python layout. Save reference images or exports under `references/` here.

Letter content lives in `../../examples/cover-letter.md` or a private working
copy. Blank lines separate paragraphs; two spaces before a newline create an
explicit line break. Rebuild and inspect the complete PDF after design changes.
