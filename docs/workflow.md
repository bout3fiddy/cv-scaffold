# From evidence to a reviewable CV

## 1. Establish ground truth

Copy the worksheet and collect user-confirmed facts. Distinguish attendance
from degree award dates, employee roles from contracts, and personal work from
team results. Record the source for each claim. Mark ambiguous dates,
estimates and ownership `needs-review`; resolve them or omit the claim.
The fictional example is never a source for a real candidate.

## 2. Select and write

Choose the target audience, then select relevant experience from the profile.
Write bullets as action + method + outcome. Use metrics only when evidence
supports the unit, baseline, result and attribution. Describe the observed outcome when a metric is unavailable. Preserve accurate job titles
and dates when tailoring. Keep the profile broader than the selected CV.

## 3. Design and implement

Use the [CV design guide](../design/cv/README.md) and
[letter design guide](../design/cover_letter/README.md) to explore styling with fictional text.
Keep CV values in `design/cv/` CSS tokens and letter values in
`design/cover_letter/build.py`. Keep semantic headings, text and links
in HTML. Personal sources live in `personal/master/`; examples stay fictional. Maintain readable type; remove low-value content before reducing size.

## 4. Build and review

Use the explicit-source build and QA commands in [onboarding](onboarding.md)
for personal documents. Run the full example build and `python qa.py` after
shared-renderer changes.
The personal check requires your ground-truth file and rejects recognizable
sample names, example links and bracketed prompts. Complete the factual,
privacy and visual reviews before sharing a document.

Review the final exported PDF:

- Expected A4 page count (two for the CV examples, one for the letter); no clipping or collisions.
- Readable at normal size; consistent margins, spacing and emphasis.
- Correct name, contact links, employers, role titles and dates.
- Every claim reconciled with the profile and the candidate's actual contribution.
- Working links and selectable text; no example links or fictional notice.
- No private notes, hidden comments or identifying PDF metadata you did not intend.

Refresh the PNG preview after any change. If you cannot render or visually
inspect the PDF, record the review as incomplete and explain the limitation.

## 5. Save and share deliberately

Review `git diff` and `git diff --cached --stat` before committing. The ignored
profile stays local, but rendered files and HTML can contain all your CV facts.
Keep an approved version before experimenting, and distinguish a new draft from
an approved export. Update `personal/status.md` with open questions and the next action.
Publish, push, email or submit only when authorized by the owner.
