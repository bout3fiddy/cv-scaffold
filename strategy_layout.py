"""Strategy-only date alignment, using the shared resume typography and spacing."""
from functools import partial
from html import escape

from docx.enum.text import WD_TAB_ALIGNMENT
from docx.shared import Pt
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer

import build
import swe_layout


class DatedHeading(Flowable):
    """One semantic heading with its date anchored at the content boundary."""

    def __init__(self, node, style, tokens):
        super().__init__()
        self.details = node.xpath('./span[@class="heading-details"]')[0]
        self.date = node.xpath("./time")[0]
        self.style = style
        self.left = Paragraph(swe_layout.markup(self.details, tokens), style)
        right_style = ParagraphStyle("RightDate", parent=style, alignment=TA_RIGHT)
        self.right = Paragraph(swe_layout.markup(self.date, tokens), right_style)
        self.date_width = stringWidth(build.source_text(self.date), "JBMono-Italic", style.fontSize) + 0.1
        self.spaceBefore, self.spaceAfter = style.spaceBefore, style.spaceAfter

    def wrap(self, available_width, available_height):
        self.width = available_width
        left_width = available_width - self.date_width - 12
        _, left_height = self.left.wrap(left_width, available_height)
        _, right_height = self.right.wrap(self.date_width, available_height)
        if max(left_height, right_height) > self.style.leading + 0.1:
            raise ValueError("Dated heading does not fit at the approved font size")
        self.height = max(left_height, right_height)
        return self.width, self.height

    def draw(self):
        self.left.drawOn(self.canv, 0, 0)
        # A flexible whitespace glyph preserves heading/date reading order
        # without padding source text or changing visible letter spacing.
        left_width = stringWidth(build.source_text(self.details), "JBMono", self.style.fontSize)
        date_start = self.width - self.date_width + 0.1
        gap = date_start - left_width
        space_width = stringWidth(" ", "JBMono", self.style.fontSize)
        self.canv.saveState()
        spacer = self.canv.beginText(left_width, self.height - self.style.fontSize)
        spacer.setFont("JBMono", self.style.fontSize)
        spacer.setHorizScale(100 * gap / space_width)
        spacer.textOut(" ")
        self.canv.drawText(spacer)
        self.canv.restoreState()
        self.right.drawOn(self.canv, self.width - self.date_width, 0)


def align_docx_dates(document, source, tokens):
    """Use native right tab stops so the Word document remains editable."""
    nodes = build.select(source.article, "p.dated-heading")
    by_text = {build.source_text(node): node for node in nodes}
    width = build.A4[0] - 2 * swe_layout.measure(tokens, "horizontal-margin")
    size = swe_layout.measure(tokens, "body-size")
    matched = 0
    for paragraph in document.paragraphs:
        node = by_text.get(" ".join(paragraph.text.split()))
        if node is None:
            continue
        paragraph.clear()
        paragraph.paragraph_format.tab_stops.add_tab_stop(Pt(width), WD_TAB_ALIGNMENT.RIGHT)
        swe_layout.append_docx_markup(paragraph, node.xpath('./span[@class="heading-details"]')[0], tokens, size)
        build.set_run_font(paragraph.add_run("\t"), "JetBrains Mono", size, build.color_hex(tokens, "paper-body"))
        swe_layout.append_docx_markup(paragraph, node.xpath("./time")[0], tokens, size)
        matched += 1
    if matched != len(nodes):
        raise ValueError(f"Aligned {matched} of {len(nodes)} dated headings")


def build_pdf(source, output_path, tokens):
    """Keep the shared page rhythm, adding a right edge to dated headings."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    build.register_fonts()
    measure = partial(swe_layout.measure, tokens)
    styles = build.pdf_styles(tokens, source.variant)
    styles["title"].spaceAfter = measure("title-gap")
    styles["title"].fontName = styles["section"].fontName = "JBMono-Bold"
    styles["contact"].leading = measure("contact-leading")
    styles["job_heading"].textColor = styles["body"].textColor
    styles["bullet"].spaceBefore = styles["compact"].spaceBefore = measure("bullet-gap")
    styles["bullet"].leftIndent = measure("bullet-indent")
    styles["bullet"].firstLineIndent = -measure("bullet-indent")
    styles["first-bullet"] = ParagraphStyle("FirstBullet", parent=styles["bullet"], spaceBefore=0)

    def paragraph(node, style):
        if "dated-heading" in node.get("class", "").split():
            return DatedHeading(node, styles[style], tokens)
        return Paragraph(swe_layout.markup(node, tokens), styles[style])

    story = [paragraph(source.article.xpath(".//h1")[0], "title")]
    for index, contact in enumerate(build.select(source.article, "p.contact")):
        if index:
            story.append(Spacer(1, measure("contact-gap")))
        story.append(paragraph(contact, "contact"))
    story.extend([Spacer(1, measure("summary-gap")), paragraph(build.select(source.article, "p.summary")[0], "summary")])
    for section in source.article.xpath("./section"):
        story.extend([
            Spacer(1, measure("section-gap")),
            Paragraph(escape(build.source_text(section.xpath("./h2")[0]).upper()), styles["section"]),
            Spacer(1, measure("section-content-gap")),
        ])
        jobs = section.xpath("./article[@class='job']")
        if not jobs:
            for index, node in enumerate(section.xpath("./p")):
                story.append(paragraph(node, "compact" if index else "body"))
        for index, job in enumerate(jobs):
            if index:
                story.append(Spacer(1, measure("job-gap")))
            bullets = build.select(job, "p.bullet")
            story.append(KeepTogether([
                paragraph(build.select(job, "p.job-heading")[0], "job_heading"),
                Spacer(1, measure("role-content-gap")),
                paragraph(bullets[0], "first-bullet"),
            ]))
            story.extend(KeepTogether([paragraph(node, "bullet")]) for node in bullets[1:])
    document = SimpleDocTemplate(
        str(output_path), pagesize=build.A4,
        leftMargin=measure("horizontal-margin") - 6, rightMargin=measure("horizontal-margin") - 6,
        topMargin=measure("vertical-margin") - 6, bottomMargin=measure("vertical-margin") - 6,
        title=source.title, author=source.author, subject=source.subject,
        invariant=1, pageCompression=1,
    )
    document.build(story, canvasmaker=partial(
        build.ResumeCanvas, title=source.title, author=source.author, subject=source.subject,
    ))
