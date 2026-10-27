const { chromium } = require('playwright');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const fs = require('node:fs/promises');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    ...(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {}),
  });
  try {
    const page = await browser.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1.5 });
    await page.goto(pathToFileURL(path.join(__dirname, 'index.html')).href);
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: 'print' });
    await fs.mkdir(path.join(__dirname, 'output'), { recursive: true });
    await page.pdf({ path: path.join(__dirname, 'output/cv-scaffold.pdf'), preferCSSPageSize: true, printBackground: true, displayHeaderFooter: false });
    console.log('Created output/cv-scaffold.pdf');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
