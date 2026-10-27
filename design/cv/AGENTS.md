# CV design

README.md explains design choices to the user. Use the implementation guide below. `build.py` contains
shared helpers and the quantitative layout. `swe_layout.py` owns the standard
layout; `strategy_layout.py` owns aligned dates. CSS and Python must agree on
typography and spacing. Store design references under `references/` here.

Use `python build.py --all` and `python qa.py` from the repository root.
Inspect all affected PDF and DOCX pages after a visible design change. For a
file move, byte-identical exports retain the previous visual review evidence.
Keep content edits in the HTML sources and retain font redistribution terms.

## Implement a design reference

1. **Create page frames.** Use an A4 portrait ratio: 210 by 297 mm, or
   approximately 794 by 1123 px at 96 px/in, for each page. Set side margins to 48 px and
   top/bottom margins to about 51 px. Start with the fictional content to avoid
   uploading private career details during design exploration.
2. **Match the typography.** Install the bundled JetBrains Mono fonts for your
   design tool. Set the name to 28 px, body to 12 px with roughly 19.33 px line
   height, contacts to 11.33 px and headings to 13.33 px. These correspond to
   the source's 21 pt, 9 pt, 8.5 pt and 10 pt sizes (1 pt = 4/3 CSS px).
3. **Build reusable styles.** Define name, contact, section, role, body and tag
   styles. Group a role heading and its bullets as a reusable component. Keep
   natural text wrapping and left alignment. Use layout spacing to align text.
4. **Try small variations.** Duplicate the frame and vary one thing at a time:
   colour, section hierarchy, spacing or emphasis. Use realistic text lengths.
   Evaluate the whole A4 page and read it at normal size before choosing.
5. **Translate the selected design into CSS.** Map design values into the
   tokens below. Keep content in `../../examples/software-engineering.html`; use the canvas as the design
   reference. Implement the design with selectable text and CSS.
6. **Render and compare.** Run the Python build and checks, then compare the PDF to
   the selected frame. Browser font metrics can wrap differently. Shorten
   content or adjust global spacing deliberately; do not squeeze individual
   lines. Save a non-personal design reference under `design/cv/references/` if useful.

| Design decision | Source token/file | Current value |
| --- | --- | --- |
| Name size | `--swe-title-size` in `swe.css` | 21 pt |
| Body size / line height | `--swe-body-size` / `--swe-body-leading` | 9 / 14.5 pt |
| Section headings | `--swe-section-size` / `--swe-section-leading` | 10 / 13 pt |
| Page margins | `--swe-horizontal-margin` / `--swe-vertical-margin` | 36 / 38 pt |
| Section / role gaps | `--swe-section-gap` / `--swe-job-gap` | 11 / 12 pt |
| Body / section colours | `--paper-body` / `--paper-muted` in `resume.css` | Warm black / muted brown |
| Links | `--paper-link` in `resume.css` | Blue |
| New-build emphasis | `--swe-zero-to-one` in `swe.css` | Muted red |
| Outlined tags | `--swe-tag-*` in `swe.css` | Transparent, black border |

The default preserves the established JetBrains Mono CV style across pages. To change fonts,
add appropriately licensed local font files and update the `@font-face` rules
and font family in `swe.css`. Keep the font licence with the files.

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
