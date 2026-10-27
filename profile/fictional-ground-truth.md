# Fictional ground truth

Avery Quill and all career facts below are invented for this starter.
Both CV types draw from this single record. F entries preserve identity,
roles, dates, skills and achievements. S entries are approved example summaries
of those facts for each focus. Reordering facts changes emphasis; factual edits
must be made here and reconciled across both CV sources.

The agent prepares the focused HTML drafts from this record. The Python
renderers export those drafts. Example QA checks every named fact against this
record and verifies that both CVs contain the same underlying F entries.
Personal facts belong in the private `profile/ground-truth.md` file.

## Facts

- **F001** Avery Quill
- **F002** Example City | avery.quill@example.com | Contact via email
- **F003** example.com | Portfolio | Professional profile
- **F004** Fictional example - all career details and results are invented.
- **F006** Engineering: Python, TypeScript, PostgreSQL, REST APIs, background workers.
- **F007** Data and quality: Search evaluation, SQL modelling, integration tests, performance profiling.
- **F008** Delivery: Docker, Git, CI/CD, cloud hosting, metrics, logs and release automation.
- **F009** Collaboration: Technical discovery, design reviews, mentoring, documentation and incident response.
- **F010** Senior Software Engineer | Lantern Studio | 2024 - Present
- **F011** - Built a review service for design teams, bringing six approval steps into one shared workspace.
- **F012** - Improved asset processing with queued jobs and caching, reducing typical turnaround from 12 minutes to under 3 minutes.
- **F013** - Led discovery with eight designers and production coordinators, mapping review decisions and exception paths before defining the service API and its initial release scope.
- **F014** - Designed idempotent background workers with bounded retries and a failed-job queue, allowing interrupted processing to resume without creating duplicate assets or notifications.
- **F015** - Introduced structured logs, queue-depth alerts and a service dashboard; reduced the time needed to locate common processing failures from roughly 45 minutes to 15 minutes.
- **F016** - Established contract tests for three external integrations and staged releases with rollback checks, helping the team ship weekly without relying on a manual release checklist.
- **F017** - Mentored two developers through code reviews and paired debugging sessions; wrote decision records explaining storage boundaries, failure handling and operational trade-offs.
- **F018** Software Engineer | Mosslight Tools | 2022 - 2024
- **F019** - Designed a searchable asset catalogue with PostgreSQL; validated relevance with a curated evaluation set.
- **F020** - Partnered with support and design to automate imports, saving five hours of manual work each week.
- **F021** - Built a versioned import API for customer asset libraries, separating validation from persistence so rejected records could be corrected and replayed without restarting a complete batch.
- **F022** - Profiled slow catalogue queries and introduced targeted indexes, reducing the median response time for the most-used listing endpoint from 900 milliseconds to 240 milliseconds.
- **F023** - Migrated an older metadata format through additive schema changes and a resumable backfill, preserving existing client integrations throughout the transition.
- **F024** - Created a representative set of 180 search queries with support colleagues and tracked regressions before releases, documenting how each ranking change affected the results.
- **F025** - Rotated through production support, documented recurring failure patterns and added automated checks for common failures and error messages with recovery steps.
- **F026** Junior Developer | Kitebox Workshop | 2020 - 2022
- **F027** - Developed internal reporting tools; added integration tests, documented release steps and supported team handover.
- **F028** - Implemented scheduled exports and reconciliation checks for weekly operational reports, replacing spreadsheet copy-and-paste steps with a repeatable pipeline and reviewable exceptions.
- **F029** - Added integration fixtures covering permissions, invalid inputs and interrupted imports; used the failures to clarify expected behaviour with the product owner.
- **F030** - Prepared onboarding notes and a local development setup used by new team members, including example data, troubleshooting steps and a walkthrough of the release process.
- **F031** Queue Garden | Project notes | 2025
- **F032** - Built a small Python job runner to explore retry policies, cancellation and worker recovery. Added fault-injection scenarios for process termination, delayed responses and duplicate delivery; documented which guarantees belonged to the worker and which required application-level checks.
- **F033** - Published a reproducible local demo with a queue dashboard and example workloads, allowing colleagues to compare throughput and failure behaviour under controlled conditions.
- **F034** Find the Frame | Technical walkthrough | 2023
- **F035** - Prototyped a catalogue for a community film archive, combining structured metadata filters with text search. Interviewed volunteer librarians, defined a small relevance benchmark and compared ranking changes against the same query set.
- **F036** - Added keyboard navigation, clear empty states and import validation. Used feedback from five trial sessions to simplify the search form and make missing metadata visible before publication.
- **F037** BSc, Computer Science | Westmere College | 2020
- **F038** Graduation project: Designed and evaluated a task-scheduling simulator, comparing queue policies under uneven workloads and reporting latency, fairness and recovery behaviour.
- **F039** Selected coursework: Algorithms, database systems, distributed computing, software testing and human-computer interaction.
- **F040** Cloud Foundations | Example Learning Institute
- **F041** Accessible Product Delivery | Example Learning Institute | 2024
- **F042** Cloud SystemsAutomationRelease Testing
- **F043** - Wrote a guide to diagnosing background-job failures, using worked examples to explain timeouts, retries and duplicate processing to engineers joining the team.
- **F044** - Facilitated a monthly engineering reading group on reliability and testing; captured short notes linking each discussion to a concrete improvement in the team's development process.
- **F045** - Volunteered at a community coding club, helping beginners debug projects, write error messages and document installation steps.

## Focused summaries

- **S001** Software engineer working on asset catalogues, review services and reporting tools for creative teams. Builds Python and TypeScript services with PostgreSQL, background workers and automated tests. Works with designers and support teams to define requirements, investigate production failures and maintain integrations through schema changes and releases.
- **S002** Software engineer focused on delivering workflow tools with designers, production coordinators and support teams. Maps user needs and exception paths, defines release scope and coordinates testing and handover. Experience includes approval workflows, asset search, automated imports, developer mentoring and operational documentation.
