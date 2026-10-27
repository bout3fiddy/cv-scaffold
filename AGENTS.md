# CV authoring

## Start here

Read `README.md`, `profile/ground-truth.md` (if present), and `STATUS.md`.
The shipped Avery Quill CV is wholly fictional. Its claims are never evidence
for a real person's CV. `profile/fictional-example.md` records example provenance.

## Sources and boundaries

- User-confirmed facts and supplied evidence in `profile/ground-truth.md` are
  the source of truth for a real CV. Ask about missing or contradictory facts.
- Do not invent employers, dates, degrees, metrics, credentials or ownership.
  Mark unresolved facts `needs-review` in the profile, not as confident CV claims.
- `index.html` owns CV content. `swe.css` owns typography and spacing;
  `base.css` owns base colours and print setup. `output/` contains exports.
- Keep one A4 page by editing content. Do not shrink individual lines or clip
  overflow to make a page fit. Preserve selectable text and working links.
- Use local fonts; retain their licence. Do not upload personal information,
  publish, push, or submit an application without the user's authorization.
- Keep private evidence out of Git. Before an authorized push inspect the
  complete diff, staged files, exports and metadata for unintended disclosure.

## Verify and hand off

Run `npm run build` and `npm run check`. For a real CV, also run
`npm run check:personal`; this detects leftover example content, not factual
truth. Reconcile every claim against the profile manually.
Render and visually inspect the final PDF for clipping, overlap, spacing and
readability. See `docs/workflow.md` for the review checklist.
Record unresolved facts and the next concrete action in `STATUS.md`.
