const { chromium } = require('playwright');
const { PDFDocument } = require('pdf-lib');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const fs = require('node:fs/promises');
const assert = require('node:assert/strict');

(async () => {
  const root = __dirname;
  const pdf = await PDFDocument.load(await fs.readFile(path.join(root, 'output/cv-scaffold.pdf')));
  assert.equal(pdf.getPageCount(), 1, 'Expected exactly one PDF page; shorten content.');
  const { width, height } = pdf.getPage(0).getSize();
  assert(Math.abs(width - 595.28) < 1 && Math.abs(height - 841.89) < 1, 'Expected A4.');
  const browser = await chromium.launch({ headless: true,
    ...(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {}) });
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: 'print' });
    const result = await page.evaluate(() => {
      const resume = document.querySelector('.resume');
      const box = resume.getBoundingClientRect();
      const style = getComputedStyle(resume);
      const right = box.right - parseFloat(style.paddingRight);
      const bottom = 297 * 96 / 25.4 - parseFloat(style.paddingBottom);
      const overflows = [...resume.querySelectorAll('p, h1, h2')].filter(el => {
        const rect = el.getBoundingClientRect();
        return rect.right > right + 1 || rect.bottom > bottom + 1 || el.scrollWidth > el.clientWidth + 1;
      }).map(el => el.textContent);
      return { text: resume.innerText, overflows,
        links: [...document.querySelectorAll('a')].map(a => a.getAttribute('href')),
        fontsReady: [...document.fonts].every(font => font.status === 'loaded') };
    });
    assert(result.fontsReady, 'Local fonts must be loaded.');
    assert.deepEqual(result.overflows, [], 'Content overflows the printable area.');
    assert(result.links.every(link => /^(https:\/\/|mailto:)/.test(link)), 'Use explicit HTTPS/mailto links.');
    if (process.argv.includes('--personal')) {
      try { await fs.access(path.join(root, 'profile/ground-truth.md')); }
      catch { throw new Error('Copy profile/ground-truth.example.md to profile/ground-truth.md and fill it with confirmed facts first.'); }
      const leftovers = /Avery Quill|Lantern Studio|Mosslight Tools|Kitebox Workshop|Westmere College|Example Learning Institute|fictional example|\[[^\]]+\]/i;
      assert(!leftovers.test(result.text), 'Replace all fictional content and bracketed prompts.');
      assert(!result.links.some(link => /example\.com/i.test(link)), 'Replace example.com links.');
      console.log('Personalization checks passed. Manually verify every claim against ground truth.');
    }
    console.log('PASS: one A4 page, loaded fonts, content within margins, valid link schemes.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error.message); process.exitCode = 1; });
