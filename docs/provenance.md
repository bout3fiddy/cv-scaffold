# Code provenance

This starter extracts the rendering implementation from an existing job-hunt
workspace. Personal source documents, archives, profile data and historical QA
fixtures were excluded.

| Original component | Starter component | Adaptation |
| --- | --- | --- |
| `materials/resumes/paper/build.py` | `design/cv/build.py` | Fictional source registry, portable custom-source CLI, strategy dispatch, generic metadata and JetBrains Mono Word fallback |
| `materials/resumes/paper/swe_layout.py` | `design/cv/swe_layout.py` | Rendering logic preserved; comments edited for clarity |
| `materials/resumes/paper/strategy_layout.py` | `design/cv/strategy_layout.py` | Rendering logic preserved; package imports updated |
| Shared resume CSS and fonts | `design/cv/` and `design/cv/fonts/` | Copied unchanged |
| Role-specific `build_cover_letter.py` | `design/cover_letter/build.py` | Same paragraph/rendering logic, font sizes and margins; source, output and metadata exposed as arguments |
| Candidate-specific QA | `qa.py` | New portable source-driven checks, replacing identity-specific assertions and machine paths |

The former Playwright implementation was removed. ReportLab generates PDFs;
python-docx generates editable CVs. HTML supplies the content and browser
preview. The Python renderers read supported CSS tokens; new design features
may require changes in the layout modules.

The two examples use the standard renderer and one fictional ground-truth
record. CV type 1 emphasises backend engineering; CV type 2 emphasises technical
delivery. The original aligned-date and compact rendering helpers remain
available in the design package.

Root build scripts delegate to the design packages. Layout imports and asset
paths follow the package locations; example content remains in `examples/`.
