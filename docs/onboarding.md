# First session with your agent

Paste this into the agent after opening the repository:

> Set up my CV workspace using AGENTS.md and docs/onboarding.md. Initialize the
> private files, then interview me in small batches. Use any CV or notes I supply
> as evidence to review, not facts to assume. Build my master CV and a reusable
> cover-letter draft from confirmed information. Keep the current styling unless
> I request a change. Check and show the documents, record open questions, and
> wait for my approval before calling them final. Do not publish or submit them.

## Agent procedure

1. Read root and relevant nested instructions. Run `python init_workspace.py`.
   It creates private working copies without overwriting existing files. The
   copied sources are still fictional: never present them as the user's CV.
2. Ask first for target role, any existing CV/notes, preferred language and what
   contact details to show. Accept plain conversation; the user need not edit files.
3. Extract supplied evidence into the profile. Ask about two or three connected
   gaps at a time: dates, individual contribution, outcomes, education, links.
   Summarize uncertain claims for confirmation. Do not require fabricated metrics.
4. Confirm the preferred layout and page count. Draft from confirmed facts only.
   Replace all fictional source text, comments, title/author/description metadata,
   URLs and letter content. A reusable letter can be a draft until a target exists.
5. Build with the shared Python modules, check the actual custom files, and inspect
   the PDF visually. Record results and limits in `personal/master/review.md`.
6. Present the draft and remaining questions. Record explicit approval only when
   received; set the next concrete action in `personal/status.md`.

## Commands for the private standard master

Run from the repository root in the Python environment described by the README:

```sh
python init_workspace.py
python build.py --variant swe --source personal/master/resume.html --stem resume --output-dir personal/master/outputs
python build_cover_letter.py --source personal/master/cover-letter.md --output personal/master/outputs/cover-letter.pdf --author "Your Name" --title "Your Name - Cover Letter" --subject "Target role"
python qa.py --source personal/master/resume.html --pdf personal/master/outputs/resume.pdf --docx personal/master/outputs/resume.docx --personal
python qa.py --kind letter --source personal/master/cover-letter.md --pdf personal/master/outputs/cover-letter.pdf --personal
```

The agent substitutes the user's confirmed metadata in the letter command.
Personal QA deliberately fails while example identities or links remain. If a
CV intentionally uses two pages, pass `--pages 2` to its QA command.

For another layout, start from its corresponding example and fix stylesheet
paths relative to the copied HTML. Pass `--variant strategy` or `--variant quant`
to the builder; keep that example's HTML structure. Do not change the shared
renderer just to substitute personal content. For role-specific drafts, use
`applications/<organisation>--<role>/` and the same explicit-source commands.
