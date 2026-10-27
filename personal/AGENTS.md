# Personal master documents

`master/cv-type-1.html` and `master/cv-type-2.html` are the focused CV sources; `master/cover-letter.md` is the
letter draft. `master/outputs/` contains draft exports.
`master/review.md` records source checks, validation, approvals and open questions,
with each entry naming CV type 1 or CV type 2 and its exact version.
`status.md` holds the next action. These private files are created on first use.

Preserve the selected renderer's semantic HTML classes and metadata. Keep facts
aligned with the profile. Before replacing an approved version, snapshot its
source and exports under `master/approved/<version>/` and record that version in
the review log. Never call an output approved because a build passed.

Use the commands below from the repository root with the selected Python runtime.
Store role-specific tailoring under `applications/`; maintain the two focused
master sources against the same profile.

## Generate and check personal documents

Replace letter metadata with user-confirmed values. Preserve approved exports
before rebuilding their paths.

```sh
python build.py --variant type1 --source personal/master/cv-type-1.html --stem "CV type 1" --output-dir personal/master/outputs
python build.py --variant type2 --source personal/master/cv-type-2.html --stem "CV type 2" --output-dir personal/master/outputs
python build_cover_letter.py --source personal/master/cover-letter.md --output personal/master/outputs/cover-letter.pdf --author "Your Name" --title "Your Name - Cover Letter" --subject "Target role"
python qa.py --source personal/master/cv-type-1.html --pdf "personal/master/outputs/CV type 1.pdf" --docx "personal/master/outputs/CV type 1.docx" --personal
python qa.py --source personal/master/cv-type-2.html --pdf "personal/master/outputs/CV type 2.pdf" --docx "personal/master/outputs/CV type 2.docx" --personal
python qa.py --kind letter --source personal/master/cover-letter.md --pdf personal/master/outputs/cover-letter.pdf --personal
```

Personal QA requires the ground-truth file and rejects sample details and metadata.
Check factual claims against their sources separately. QA reads the CV's
`data-expected-pages`; use `--pages` to override the intended count. Letter QA
defaults to one page. Inspect the complete PDF and any delivered Word export.

## Two focused CVs

`master/cv-type-1.html` and `master/cv-type-2.html` are two views of the same
private ground truth. Type 1 defaults to backend engineering; type 2 defaults
to technical delivery and product collaboration. Confirm the user's intended
focuses and record them in preferences. Keep names, employers, titles, dates,
qualifications and numerical results consistent across both views.

Draft each summary and order its skills, bullets and projects for its audience.
Record the facts used and omissions in the review log. When a fact changes,
update the profile first, then reconcile both active CVs. Preserve approved
and submitted copies. Remove the fictional `data-fact-id` and `data-ground-truth`
attributes when drafting personal content, or replace them with personal references.

Build the second view with `--variant type2`, source `personal/master/cv-type-2.html`
and a distinct output stem. Both examples currently use the same visual layout;
focus is controlled by the source content. Preserve `article.resume`, metadata,
contact, summary, sections and paragraph classes. See `../design/cv/AGENTS.md`
for build commands and `../design/cover_letter/AGENTS.md` for letter formatting.
