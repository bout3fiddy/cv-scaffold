# Personal master documents

`master/resume.html` is the editable reusable CV; `master/cover-letter.md` is the
reusable letter draft. `master/outputs/` contains candidates, not approval evidence.
`master/review.md` records source checks, validation, approvals and open questions.
`status.md` holds the next action. These private files are created on first use.

Preserve the selected renderer's semantic HTML classes and metadata. Keep facts
aligned with the profile. Before replacing an approved version, snapshot its
source and exports under `master/approved/<version>/` and record that version in
the review log. Never call an output approved because a build passed.

Use the explicit-source build and QA commands in `../docs/onboarding.md`.
Tailoring belongs under applications, not a second competing personal master.
