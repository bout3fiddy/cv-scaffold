# CV design

Create a design in Paper or Figma, then transfer its measurements to the CSS
and Python layout code using the steps below.

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

An agent prompt for translating a design:

> Use this supplied frame or screenshot as a visual reference. Keep my verified
> CV content in the selected HTML content source. Translate the typography, colour and spacing into
> shared CSS tokens. Preserve semantic text, links and A4 printing. Build and
> inspect the PDF, and explain any differences from the reference.


Run builds from the repository root with `python build.py`. This folder owns
CV layouts, CSS tokens and the font files shared with the cover-letter renderer.
