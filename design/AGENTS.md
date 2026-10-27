# Design files

Keep CV rendering, styles, fonts and design references in `cv/`. Keep letter
rendering, typography and references in `cover_letter/`. Root build scripts
are entry points. Shared fonts currently live in `cv/fonts/` with their licence.

Content belongs in examples or private document sources. When moving a design
file, update Python imports, HTML stylesheet links, workspace initialization
and documentation in the same change. Verify builds from the repository root
and from another working directory. Preserve the selected page count and
compare exports with the last reviewed version.
