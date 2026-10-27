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

The agent follows [the shared design reference](../design/DESIGN.md) when
applying or changing a style. Personal sources live in `personal/master/`;
examples stay fictional.

## 4. Build and review

The agent follows [the personal-document instructions](../personal/AGENTS.md)
to generate and check drafts. Shared-renderer changes require the full example
checks defined in the root instructions.
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

Review pending changes and staged files using the root agent instructions. The ignored
profile stays local, but rendered files and HTML can contain all your CV facts.
Keep an approved version before experimenting, and distinguish a new draft from
an approved export. Update `personal/status.md` with open questions and the next action.
Publish, push, email or submit only when authorized by the owner.
