# Personal master documents

`master/resume.html` is the editable reusable CV; `master/cover-letter.md` is the
letter draft. `master/outputs/` contains draft exports.
`master/review.md` records source checks, validation, approvals and open questions.
`status.md` holds the next action. These private files are created on first use.

Preserve the selected renderer's semantic HTML classes and metadata. Keep facts
aligned with the profile. Before replacing an approved version, snapshot its
source and exports under `master/approved/<version>/` and record that version in
the review log. Never call an output approved because a build passed.

Use the commands below from the repository root with the selected Python runtime.
Store tailored documents under `applications/` and retain one personal master.

## Generate and check personal documents

Replace letter metadata with user-confirmed values. Preserve approved exports
before rebuilding their paths.

```sh
python build.py --variant swe --source personal/master/resume.html --stem resume --output-dir personal/master/outputs
python build_cover_letter.py --source personal/master/cover-letter.md --output personal/master/outputs/cover-letter.pdf --author "Your Name" --title "Your Name - Cover Letter" --subject "Target role"
python qa.py --source personal/master/resume.html --pdf personal/master/outputs/resume.pdf --docx personal/master/outputs/resume.docx --personal
python qa.py --kind letter --source personal/master/cover-letter.md --pdf personal/master/outputs/cover-letter.pdf --personal
```

Personal QA requires the ground-truth file and rejects sample details and metadata.
Check factual claims against their sources separately. QA reads the CV's
`data-expected-pages`; use `--pages` to override the intended count. Letter QA
defaults to one page. Inspect the complete PDF and any delivered Word export.

For another CV layout, copy its example, update relative stylesheet links and
select `--variant strategy` or `--variant quant`. Preserve `article.resume`,
metadata, contact, summary, section and paragraph classes. Strategy sources
also require `.dated-heading`, `.heading-details` and `time`. The quantitative
renderer expects one contact paragraph. See `../design/cv/AGENTS.md` for layout
commands and `../design/cover_letter/AGENTS.md` for letter formatting.
