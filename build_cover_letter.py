"""Portable version of the shared job-hunt cover-letter PDF renderer."""
import argparse
from functools import partial
from html import escape
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate

import build


def build_letter(source, output, author, title, subject):
    build.register_fonts()
    style = ParagraphStyle('Letter', fontName='JBMono', fontSize=10,
                           leading=15.5, spaceAfter=14)
    blocks = source.read_text(encoding='utf-8').strip().split('\n\n')
    if not blocks or not blocks[0].strip():
        raise ValueError('Cover letter is empty')
    story = [Paragraph(escape(block).replace('  \n', '<br/>').replace('\n', ' '), style)
             for block in blocks]
    output.parent.mkdir(parents=True, exist_ok=True)
    SimpleDocTemplate(str(output), pagesize=A4,
                      leftMargin=42, rightMargin=42, topMargin=48, bottomMargin=42,
                      title=title, author=author).build(
        story, canvasmaker=partial(build.ResumeCanvas, title=title,
                                  author=author, subject=subject))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=build.ROOT / 'examples/cover-letter.md')
    parser.add_argument('--output', type=Path, default=build.ROOT / 'output/avery-quill-cover-letter.pdf')
    parser.add_argument('--author', default='Avery Quill')
    parser.add_argument('--title', default='Avery Quill - Fictional Cover Letter')
    parser.add_argument('--subject', default='Fictional application example')
    args = parser.parse_args()
    build_letter(args.source, args.output, args.author, args.title, args.subject)
    print(args.output)


if __name__ == '__main__':
    main()
