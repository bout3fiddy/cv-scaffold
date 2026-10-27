# Document design

This is the design reference for the CV and cover-letter layouts. Read it
before developing a style, interpreting a Paper/Figma reference or changing
layout measurements. Keep design decisions and specifications here; execution
commands live in the design folders' AGENTS.md files.

## Layout choices

CV type 1 and CV type 2 use the same standard layout, with coloured emphasis
and outlined skill tags. Their content emphasises different parts of the same
profile. Both examples are two pages. The code also retains aligned-date and
compact layout helpers for future design work; the example build exports only
the two named CV types.

The cover letter uses JetBrains Mono on A4 with paragraph spacing and a
one-page target. CV content belongs in the profile and document sources;
letter content belongs in the personal or role-specific draft.

## Paper and Figma workflow

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
   tokens below. Keep content in `../examples/cv-type-1.html`; use the canvas as the design
   reference. Implement the design with selectable text and CSS.
6. **Render and compare.** Run the Python build and checks, then compare the PDF to
   the selected frame. Browser font metrics can wrap differently. Shorten
   content or adjust global spacing deliberately; do not squeeze individual
   lines. Save a non-personal design reference under `cv/references/` if useful.

| Design decision | Source token/file | Current value |
| --- | --- | --- |
| Name size | `--swe-title-size` in `cv/swe.css` | 21 pt |
| Body size / line height | `--swe-body-size` / `--swe-body-leading` | 9 / 14.5 pt |
| Section headings | `--swe-section-size` / `--swe-section-leading` | 10 / 13 pt |
| Page margins | `--swe-horizontal-margin` / `--swe-vertical-margin` | 36 / 38 pt |
| Section / role gaps | `--swe-section-gap` / `--swe-job-gap` | 11 / 12 pt |
| Body / section colours | `--paper-body` / `--paper-muted` in `cv/resume.css` | Warm black / muted brown |
| Links | `--paper-link` in `cv/resume.css` | Blue |
| New-build emphasis | `--swe-zero-to-one` in `cv/swe.css` | Muted red |
| Outlined tags | `--swe-tag-*` in `cv/swe.css` | Transparent, black border |

The default preserves the established JetBrains Mono CV style across pages. To change fonts,
add appropriately licensed local font files and update the `@font-face` rules
and font family in `cv/swe.css`. Keep the font licence with the files.

## Cover-letter specification

`cover_letter/build.py` owns the ReportLab `ParagraphStyle` and `SimpleDocTemplate` settings:

| Setting | Value |
| --- | --- |
| Typeface | JetBrains Mono |
| Body size / line height | 10 / 15.5 pt |
| Space after paragraphs | 14 pt |
| Side and bottom margins | 42 pt |
| Top margin | 48 pt |
| Page | A4 |

Font registration and PDF metadata helpers come from `cv/build.py`; the font
files and licence live in `cv/fonts/`. For Paper/Figma, use an A4 frame and
multiply point values by 4/3 for CSS pixels. Transfer approved design values to
the Python settings and save reference images under `cover_letter/references/`.

## Working with a reference

Ask which aspects of a supplied screenshot, document or frame the user wants
to preserve. Compare typography, margins, section hierarchy, emphasis and text
wrapping. Use the fictional examples for initial experiments. Obtain the user's
authorization before sending personal content to an external design service.

Keep approved wording and links while trying layout variations. Show the user
the generated document and explain material differences from the reference.
Record their selected design in the private preferences file. The standard
font files and redistribution licence live in `cv/fonts/` and are shared with
the letter renderer.

## Prompts the agent should support

> Compare CV type 1 and CV type 2. Explain which experience each version
> emphasises and how it relates to the target role.

> Use this Paper or Figma frame as a reference for my CV. Keep my wording and
> contact links, match the typography and spacing, and show me the result.

> Make the CV easier to scan. Show me a version with clearer section headings
> and more space between roles while keeping it to two pages.

> Style this letter to match my approved CV. Keep it to one page and show me
> the PDF so I can review the text and spacing together.

> Compare the current letter with a version that has more space between
> paragraphs. Keep both available until I choose one.

## Review

Inspect every page at normal reading size. Check text wrapping, spacing,
headings, links and page breaks. Keep headings with their content. Preserve
readable type sizes and select content to fit the agreed length. Word and
LibreOffice can paginate differently; use the rendered PDF as the reference
for exact appearance and inspect any Word version being delivered.
