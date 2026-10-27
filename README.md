# Python CV and cover-letter starter

The Python rendering toolkit used in an existing job-hunt workflow, packaged
with fictional inputs and portable paths. This is the actual ReportLab and
python-docx implementation, including the standard, quantitative and
right-aligned strategy CV layouts, plus the shared cover-letter renderer.
No browser, Node.js, hosted service or API key is needed to generate documents.

**Avery Quill is fictional.** All sample employers, education, credentials,
projects and results are invented. The same sample facts illustrate the layout
options; the quantitative and strategy examples are not separate real careers.

![Standard CV](output/avery-quill-swe.png)

[Standard PDF](output/avery-quill-swe.pdf) · [Editable Word version](output/avery-quill-swe.docx) ·
[Strategy PDF](output/avery-quill-strategy.pdf) · [Quantitative layout PDF](output/avery-quill-quant.pdf) ·
[Cover letter](output/avery-quill-cover-letter.pdf)

## Start in a few minutes

Use a private copy for personal work. Install Python 3.10 or newer, then:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python build.py --all
python build_cover_letter.py
python qa.py
```

On Windows, activate with `.venv\Scripts\activate` instead.
The default build (`python build.py`) generates the standard CV as PDF and DOCX.
All example PDFs fit one A4 page. Longer CVs may flow onto multiple pages;
validate the intended page count rather than shrinking individual lines.

**You can let your agent do the setup and ask you for the facts.** Paste:

> Set up my CV workspace using AGENTS.md and docs/onboarding.md. Initialize the
> private files and interview me in small batches. Use my existing CV or notes
> if available, resolve uncertainties, and draft my CV and cover letter from
> confirmed facts. Build and review them with the existing Python tooling.
> Preserve the styling unless I ask for changes. Do not publish or submit.

The agent runs `python init_workspace.py`, which creates private profile,
preferences, master sources, a review log and status file without overwriting
anything. You supply your information conversationally; the agent maintains
the files. The fictional examples remain reusable references.

See [agent onboarding](docs/onboarding.md) for the interview sequence and exact
personal-document commands, and [housekeeping](docs/housekeeping.md) for source
ownership, approvals, versions, privacy and session handoff.

## Files and responsibilities

| File | Purpose |
| --- | --- |
| `build.py` | Original shared parsing, fonts, PDF/DOCX helpers, quantitative renderer and build CLI |
| `swe_layout.py` | Original standard CV PDF/DOCX renderer and CSS-token mapping |
| `strategy_layout.py` | Original right-aligned dates for PDF and Word |
| `build_cover_letter.py` | Existing cover-letter renderer with portable CLI arguments |
| `resume.css`, `swe.css`, `strategy.css` | Original styling, measurements and HTML preview rules |
| `examples/*.html` | Fictional CV source documents |
| `examples/cover-letter.md` | Fictional plain-text letter source |
| `fonts/` | Embedded JetBrains Mono fonts and licence |
| `qa.py` | Portable source-content, links, geometry, font and page-count checks |
| `profile/ground-truth.example.md` | Fact collection and claim ledger worksheet |
| `AGENTS.md`, nested instructions, `CLAUDE.md` | Shared agent rules and folder ownership |
| `init_workspace.py`, `templates/` | Non-overwriting private workspace initialization |
| `personal/` | Private master sources, review log and status |
| `applications/` | Private role briefs, tailored sources and exports |
| `STATUS.md` | Distributed starter status; personal progress lives in `personal/status.md` |
| `output/` | Generated PDFs, editable DOCX files, previews and QA report |

See [code provenance](docs/provenance.md) for what was reused and what changed.

## Generate different CVs

```sh
python build.py --variant swe
python build.py --variant strategy
python build.py --variant quant
python build.py --all --format pdf
python build.py --variant swe --source examples/software-engineering.html --stem my-cv --output-dir output/custom
```

To tailor an application, copy an example into a local `applications/` folder,
edit content from ground truth and pass its path with `--source`. Keep separate
sources and output names for each role. Do not overwrite an approved master
while trying a new draft. Custom HTML must retain `article.resume`, the
`data-variant`, metadata, contact, summary, sections and paragraph classes.
For the strategy layout, keep `.dated-heading`, `.heading-details` and `time`.
The quantitative renderer expects one contact paragraph.

Without arguments, QA checks the three fictional examples and letter. For your
own documents, pass explicit source and output paths:

```sh
python qa.py --source personal/master/resume.html --pdf personal/master/outputs/resume.pdf --docx personal/master/outputs/resume.docx --personal
python qa.py --kind letter --source personal/master/cover-letter.md --pdf personal/master/outputs/cover-letter.pdf --personal
```

Use `--pages 2` for an intentionally two-page CV. Personal checks require a
ground-truth file and reject recognizable fictional details and metadata;
they do not verify professional claims. Record factual review separately.

## Generate cover letters

```sh
python build_cover_letter.py --source examples/cover-letter.md --output output/my-cover-letter.pdf --author "Your Name" --title "Your Name - Cover Letter" --subject "Role title"
```

The source uses blank lines between paragraphs and two spaces before a newline
for an explicit line break. It is a small plain-text format, not a full Markdown
renderer: headings, lists and emphasis syntax are printed literally.
The original letter styling is JetBrains Mono, 10 pt text, 15.5 pt leading,
14 pt paragraph spacing, 42 pt side margins and a 48 pt top margin. Edit the
`ParagraphStyle` and page settings in `build_cover_letter.py` to change it.
The cover-letter builder produces PDF; CV builders also produce editable DOCX.

## Develop your styling in Paper or Figma

Use either design tool as a visual exploration space. The steps below are a
manual workflow; this starter does not include a Paper or Figma integration.

1. **Create a page frame.** Use an A4 portrait ratio: 210 by 297 mm, or
   approximately 794 by 1123 px at 96 px/in. Set side margins to 48 px and
   top/bottom margins to about 51 px. Start with the fictional content to avoid
   uploading private career details during design exploration.
2. **Match the typography.** Install the bundled JetBrains Mono fonts for your
   design tool. Set the name to 28 px, body to 12 px with roughly 19.33 px line
   height, contacts to 11.33 px and headings to 13.33 px. These correspond to
   the source's 21 pt, 9 pt, 8.5 pt and 10 pt sizes (1 pt = 4/3 CSS px).
3. **Build reusable styles.** Define name, contact, section, role, body and tag
   styles. Group a role heading and its bullets as a reusable component. Keep
   natural text wrapping and left alignment. Use spacing rules instead of
   adding spaces to align text.
4. **Try small variations.** Duplicate the frame and vary one thing at a time:
   colour, section hierarchy, spacing or emphasis. Use realistic text lengths.
   Evaluate the whole A4 page and read it at normal size before choosing.
5. **Translate the selected design into CSS.** Map design values into the
   tokens below. Keep content in `examples/software-engineering.html`; use the canvas as the design
   reference. Prefer actual text and CSS to a screenshot of the design.
6. **Render and compare.** Run the Python build and checks, then compare the PDF to
   the selected frame. Browser font metrics can wrap differently. Shorten
   content or adjust global spacing deliberately; do not squeeze individual
   lines. Save a non-personal design reference under `docs/` if useful.

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

The default preserves the established JetBrains Mono CV style. To change fonts,
add appropriately licensed local font files and update the `@font-face` rules
and font family in `swe.css`. Keep the font licence with the files.

An agent prompt for translating a design:

> Use this supplied frame or screenshot as a visual reference. Keep my verified
> CV content in the selected examples/*.html source. Translate the typography, colour and spacing into
> shared CSS tokens. Preserve semantic text, links and A4 printing. Build and
> inspect the PDF, and explain any differences from the reference.

## Validation and previews

```sh
python build.py --all
python build_cover_letter.py
python qa.py
```

The checks cover complete source paragraphs in PDFs and DOCX, expected PDF
pages, A4 size, link destinations, embedded descriptor fonts and text bounds.
Always inspect the rendered pages for collisions and readability. Word is an
editable fallback; install the bundled fonts before viewing it. Word and
LibreOffice can paginate differently from the authoritative ReportLab PDF.

For PNG previews, install Poppler (`pdftoppm`) and run:

```sh
pdftoppm -singlefile -scale-to 1200 -png output/avery-quill-swe.pdf output/avery-quill-swe
```

Refresh previews after changing the source. See [the review workflow](docs/workflow.md).

## Privacy

Personal profile files, evidence, `personal/` and application content are ignored by
Git. Example sources and `output/` are tracked: after personalization they can
contain your career details. Review source, exports, metadata and staged files
before any push. Share the fictional starter separately from personal work.
The supplied files contain no real candidate information, but repository
ownership itself is visible to people with access.
