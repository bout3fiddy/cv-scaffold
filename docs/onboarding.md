# First session with your agent

Paste this into the agent after opening the repository:

> Set up my CV workspace using AGENTS.md and docs/onboarding.md. Initialize the
> private files, then interview me in small batches. Use any CV or notes I supply
> as evidence and confirm uncertain claims with me. Build my master CV and a
> cover-letter draft from confirmed information. Keep the current styling unless
> I request a change. Check and show the documents, record open questions, and
> wait for my approval before calling them final. Do not publish or submit them.

## Agent procedure

1. Read root and relevant nested instructions. Initialize the private workspace
   using the setup instructions in `AGENTS.md`. Existing files are preserved. The
   copied sources are still fictional: never present them as the user's CV.
2. Ask first for target role, any existing CV/notes, preferred language and what
   contact details to show. Collect answers in conversation and update the files.
3. Extract supplied evidence into the profile. Ask about two or three connected
   gaps at a time: dates, individual contribution, outcomes, education, links.
   Ask the user to confirm uncertain claims. Use metrics only when supported.
4. Confirm the preferred layout and page count. Draft from confirmed facts only.
   Replace all fictional source text, comments, title/author/description metadata,
   URLs and letter content. A reusable letter can be a draft until a target exists.
5. Build with the shared Python modules, check the actual custom files, and inspect
   the PDF visually. Record results and limits in `personal/master/review.md`.
6. Present the draft and remaining questions. Record explicit approval only when
   received; set the next concrete action in `personal/status.md`.

## Agent instructions

Environment setup belongs in [the root instructions](../AGENTS.md).
Personal-document commands belong in [the master instructions](../personal/AGENTS.md).
Role-specific work follows [the application instructions](../applications/AGENTS.md).
The agent handles these operations and presents the resulting documents for review.
