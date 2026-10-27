# Code provenance

This starter extracts the rendering implementation from an existing job-hunt
workspace. Personal source documents, archives, profile data and historical QA
fixtures were excluded.

| Original component | Starter component | Adaptation |
| --- | --- | --- |
| `materials/resumes/paper/build.py` | `build.py` | Fictional source registry, portable custom-source CLI, strategy dispatch, generic metadata and JetBrains Mono Word fallback |
| `materials/resumes/paper/swe_layout.py` | `swe_layout.py` | Rendering logic preserved; comments edited for clarity |
| `materials/resumes/paper/strategy_layout.py` | `strategy_layout.py` | Copied unchanged |
| Shared resume CSS and fonts | Same files and `fonts/` | Copied unchanged |
| Role-specific `build_cover_letter.py` | `build_cover_letter.py` | Same paragraph/rendering logic, font sizes and margins; source, output and metadata exposed as arguments |
| Candidate-specific QA | `qa.py` | New portable source-driven checks, replacing identity-specific assertions and machine paths |

The former Playwright implementation was removed. ReportLab generates PDFs;
python-docx generates editable CVs. HTML supplies the content and browser
preview. The Python renderers read supported CSS tokens; new design features
may require changes in the layout modules.

The strategy example uses the same fictional history to demonstrate aligned
dates. The quantitative example demonstrates the original compact renderer.
All variants describe the same fictional candidate.
