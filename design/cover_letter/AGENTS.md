# Cover-letter design

Read [the design reference](../DESIGN.md) before styling work. This folder owns
the letter renderer. Store references under `references/` here and keep the
specification in DESIGN.md current. The renderer uses the CV package's shared
font and metadata helpers.

Use `python build_cover_letter.py` and `python qa.py` from the repository root.
Inspect the exported page after a visible design change. For a file move,
byte-identical output retains the previous visual review evidence. Letter text
belongs in the example or private source passed to the builder.

## Content format

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
