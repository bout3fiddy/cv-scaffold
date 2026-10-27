# Personal master documents

`master/resume.html` is the editable reusable CV; `master/cover-letter.md` is the
letter draft. `master/outputs/` contains draft exports.
`master/review.md` records source checks, validation, approvals and open questions.
`status.md` holds the next action. These private files are created on first use.

Preserve the selected renderer's semantic HTML classes and metadata. Keep facts
aligned with the profile. Before replacing an approved version, snapshot its
source and exports under `master/approved/<version>/` and record that version in
the review log. Never call an output approved because a build passed.

Use the explicit-source build and QA commands in `../docs/onboarding.md`.
Store tailored documents under `applications/` and retain one personal master.
