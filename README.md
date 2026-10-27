# One-page CV scaffold

An editable, anonymous A4 CV template. All identity, contact, employment,
academic, credential and achievement details are placeholders. Links use
example.com; no real career history is included.

![One-page preview](output/cv-scaffold.png)

[Download the PDF](output/cv-scaffold.pdf)

## Edit

Open `index.html` directly in a browser. Replace bracketed prompts with your
own verified details and replace every example.com link. Each bullet follows
an action / method / outcome structure; underlines highlight evidence and the
muted red label highlights a new build. Remove any section you do not need.

The design preserves the established CV style: JetBrains Mono, 21 pt name,
9 pt body on 14.5 pt leading, 10 pt uppercase section headings, blue links,
muted red delivery labels and transparent outlined skill tags. `swe.css`
contains the original shared measurements; `base.css` supplies document
colours and print setup. Keep the type scale intact and shorten content to
fit one page.

## Export

Requires Node.js 20 or newer:

```sh
npm ci
npx playwright install chromium
npm run build
```

Alternatively, set `CHROME_PATH` to an installed Chrome executable.
The build loads local fonts and writes `output/cv-scaffold.pdf` without browser
headers or footers. Check the page count and appearance after editing.
To regenerate the preview with Poppler:

```sh
pdftoppm -singlefile -scale-to 1600 -png output/cv-scaffold.pdf output/cv-scaffold
```

The PDF is selectable text, with embedded fonts. Font redistribution terms
are in `fonts/OFL.txt`. The committed example is intentionally generic;
repository account ownership is separate from document anonymization.
