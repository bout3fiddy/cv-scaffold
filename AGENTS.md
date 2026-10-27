# CV workspace

## Start here

Read `README.md` and the nearest nested `AGENTS.md` before editing a folder.
If `profile/ground-truth.md` is missing, follow `docs/onboarding.md`: initialize
the workspace and interview the user. Otherwise read that profile,
`profile/preferences.md` and `personal/status.md`. `STATUS.md` describes only
the distributed starter. Keep personal work out of the fictional examples.

## Sources of truth

1. User-confirmed facts and the claim ledger in `profile/ground-truth.md`.
2. Supporting evidence in `profile/evidence/` and supplied public sources.
3. Editable master sources in `personal/master/`.
4. Role-specific sources in `applications/<organisation>--<role>/`.
5. Generated exports are derivatives, never the factual source of truth.

Never invent claims, dates, credentials, metrics or application state. Record
conflicts as `needs-review`; ask concise questions and continue independent
work. Fictional examples provide structure and styling only.

## Ownership and housekeeping

- `profile/`: private facts, preferences and evidence; see its instructions.
- `personal/`: reusable master, review records and working status.
- `applications/`: role briefs, tailored copies and their exports.
- `examples/` and `output/`: fictional demonstration sources and outputs.
- `design/cv/`: CV layouts, stylesheets, fonts and design references.
- `design/cover_letter/`: letter layout, typography and design references.
- Root Python build scripts: command entry points for the design packages.
- `templates/`: blank intake/review records; `docs/`: reusable procedures.

Keep durable rules in the nearest instruction file and volatile facts in the
profile, status or review records. Update instructions and README together when
paths, commands or ownership change. Do not create duplicate masters. Preserve
uncommitted work and approved exports; inspect exact scope before any deletion.
Use `docs/housekeeping.md` for versions, approval and handoff rules.

## Build and verify

Use the existing Python renderers; do not create a replacement rendering stack.
Follow `docs/onboarding.md` for personal-source commands and `docs/workflow.md`
for final review. Shared-renderer changes require the fictional regression build:
`python build.py --all`, `python build_cover_letter.py`, `python qa.py`.
The fictional CV examples declare two pages in `data-expected-pages`; the letter
is one page. Inspect every page even when the README preview shows only the first.
Select content to fit the agreed page count; do not shrink individual lines or
clip overflow. Keep text selectable, links intact and font licences present.

## Writing

State the action, evidence and result directly. Use concrete verbs and ordinary
words. Remove slogans, filler introductions, stock transitions, exaggerated
claims and rhetorical contrasts. Describe what changed and why it matters.
Keep CV bullets specific to the candidate's work. Keep instructions concise.

## Permissions and handoff

Local initialization, drafting, building and checking are normal task work.
Ask before publishing, pushing personal data, uploading to external tools,
emailing or submitting unless already authorized. Ignored files remain readable on the local filesystem.
Review staged files, exports and metadata before an authorized push.
Record actual checks, unresolved questions and one next action in the private
review/status files. Call a draft approved only after explicit user approval.
