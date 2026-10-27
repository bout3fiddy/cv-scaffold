# CV and cover-letter workspace

Use this repository with your agent to create and maintain your CV and cover
letters. Give the agent your experience, preferences and any existing documents;
it organises the information, drafts the text, applies the design and checks
the finished files.

You can create a master CV, tailor it for different roles, write cover letters,
try layouts and keep approved versions. CVs are available as PDF and editable
Word documents; cover letters are available as PDF.

## Start with your agent

Open this repository in your agent's workspace and send:

> Help me set up my CV and cover-letter workspace. Read the repository's agent
> instructions, then ask me for my details in small batches. I can provide an
> existing CV or notes. Confirm uncertain facts with me, create a first draft
> and show me the finished documents. Keep them private until I approve sharing.

The agent handles setup and maintains the files as you answer. It records your
confirmed facts, flags questions and remembers the next step. You review the
wording and appearance, then decide which version to approve.

## What you can ask for

**Create your first CV**

> Build my CV for software engineering roles using the experience I have given
> you. Use the standard layout and aim for two pages. Ask about missing dates
> or unclear achievements before including them.

**Tailor an application**

> Here is a job posting. Make a tailored copy of my CV using the experience
> most relevant to this role. Keep my master CV unchanged and explain the edits.

**Write a cover letter**

> Draft a cover letter for this role using my confirmed experience. Focus on
> why I want the job and two relevant examples. Keep the tone direct and show
> me the draft before treating it as final.

**Update a fact**

> I have completed this certification. Add the confirmed details to my profile,
> update the relevant CV drafts and tell me which documents changed.

**Review the writing**

> Review my CV for vague claims, repetition and filler. Suggest specific edits
> and flag any achievement that needs supporting detail.

**Change the design**

> Show me two options for the typography and spacing while keeping my content
> and page count. Use this Paper or Figma reference for the look I want.

**Prepare files to send**

> Prepare the PDF and Word versions of this CV. Check every page, confirm the
> contact links and show me anything that still needs my review.

**Resume later**

> Summarise where we left off, list the unresolved questions and help me finish
> the next step.

## Where your information lives

The agent creates your working files during setup. You can ask it to show or
explain any of them.

| Location | What it contains |
| --- | --- |
| `profile/ground-truth.md` | Confirmed personal facts, sources and unresolved questions |
| `profile/preferences.md` | Target roles, language, page count, tone and contact preferences |
| `profile/evidence/` | Supporting documents you choose to provide |
| `personal/master/` | Both focused CV sources, letter draft, review record and approved versions |
| `personal/master/outputs/` | Generated drafts of your personal documents |
| `personal/status.md` | Current progress and the next action |
| `applications/` | Role briefs, tailored documents, outputs and submission records |
| `design/cv/` | CV layouts, typography and design references |
| `design/cover_letter/` | Cover-letter layout and design references |
| `examples/` and `output/` | Fictional demonstration documents and their exports |

## Two CV types from one ground truth

Your ground truth is the shared record of your experience, education, skills
and confirmed results. The agent uses it to prepare two CVs for different
audiences:

| CV | Focus | What it leads with |
| --- | --- | --- |
| **CV type 1** | Backend engineering and systems | Implementation, APIs, data processing, testing and performance |
| **CV type 2** | Technical delivery and product collaboration | Discovery, release planning, stakeholder work, mentoring and adoption |

Both describe the same person. Employers, titles, dates, qualifications and
results stay consistent. The agent changes the summary and the order and
emphasis of skills, achievements and projects to suit each audience. You can
choose different focuses for your own two versions.

The agent records your facts once in `profile/ground-truth.md` and keeps the
two CV drafts under `personal/master/`. It prepares the focused wording, then
generates the PDF and Word files from those drafts. When you correct a fact,
it updates the profile and checks both active CVs for the same correction.
Each version has its own review and approval history.

> Create CV type 1 for backend engineering roles and CV type 2 for technical
> delivery roles from my confirmed profile. Explain the emphasis in each,
> keep the career facts consistent, and show me both versions for review.

The examples use **Avery Quill, a fictional candidate**. Both draw from the
same [fictional ground truth](profile/fictional-ground-truth.md), and checks
compare their factual text with that record. All employers, qualifications
and achievements are invented. Both CVs span two pages and share the same
visual style. The preview below shows the first page of CV type 1.

![CV type 1, first page](output/CV%20type%201.png)

[CV type 1 PDF](output/CV%20type%201.pdf) · [CV type 1 Word](output/CV%20type%201.docx) ·
[CV type 2 PDF](output/CV%20type%202.pdf) · [CV type 2 Word](output/CV%20type%202.docx) ·
[Cover letter](output/avery-quill-cover-letter.pdf)

Ask your agent to compare the versions or develop a style from a reference.
The agent follows the design instructions stored under `design/`.

## Privacy and approval

Your personal profile, evidence and application folders stay local by default
and are excluded from normal repository uploads. They remain readable on your
computer. Keep your copy private and tell your agent before sharing documents
or sending personal information to an external service.

The agent keeps drafts, reviewed versions and submitted copies separately.
You approve the content and decide when to share or submit it. Ask the agent
to check exactly which files will be shared before authorising an upload.
