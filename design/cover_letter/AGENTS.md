# Cover-letter design

This folder owns letter layout and typography. Use the measurements below. Keep design references under `references/` here. The renderer
uses the CV package's shared font and metadata helpers.

Use `python build_cover_letter.py` and `python qa.py` from the repository root.
Inspect the exported page after a visible design change. For a file move,
byte-identical output retains the previous visual review evidence. Letter text
belongs in the example or private source passed to the builder.

## Layout and content format

`build.py` owns the ReportLab `ParagraphStyle` and `SimpleDocTemplate` settings:

| Setting | Value |
| --- | --- |
| Typeface | JetBrains Mono |
| Body size / line height | 10 / 15.5 pt |
| Space after paragraphs | 14 pt |
| Side and bottom margins | 42 pt |
| Top margin | 48 pt |
| Page | A4 |

Font registration and PDF metadata helpers come from `../cv/build.py`; the font
files and licence live in `../cv/fonts/`. For Paper/Figma, use an A4 frame and
multiply point values by 4/3 for CSS pixels. Transfer approved design values to
the Python settings and save reference images under `references/` here.

Source text uses blank lines between paragraphs and two spaces before a newline
for an explicit line break. Headings, lists and emphasis syntax print literally.

## Export and check

Run from the repository root with the selected Python runtime:

```sh
python build_cover_letter.py
python build_cover_letter.py --source personal/master/cover-letter.md --output personal/master/outputs/cover-letter.pdf --author "Your Name" --title "Your Name - Cover Letter" --subject "Target role"
python qa.py --kind letter --source personal/master/cover-letter.md --pdf personal/master/outputs/cover-letter.pdf --personal
```

Substitute confirmed metadata before generating personal documents. The letter
builder exports PDF. For the example preview:

```sh
pdftoppm -f 1 -singlefile -scale-to 1200 -png output/avery-quill-cover-letter.pdf output/avery-quill-cover-letter
```
