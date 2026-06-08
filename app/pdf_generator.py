# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib import colors
# from reportlab.lib.enums import TA_CENTER, TA_LEFT
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# SECTION_HEADINGS = {
#     "video title",
#     "executive summary",
#     "key concepts",
#     "key takeaways",
#     "interview questions",
# }
# BULLET_MARKERS = ("-", "*", "\u2022")


# def _clean_line(line):
#     return (
#         line.strip()
#         .replace("&", "&amp;")
#         .replace("<", "&lt;")
#         .replace(">", "&gt;")
#     )


# def _normalize_heading(line):
#     cleaned = line.strip()

#     if "." in cleaned[:4]:
#         parts = cleaned.split(".", 1)
#         if parts[0].strip().isdigit():
#             cleaned = parts[1].strip()

#     if ":" in cleaned:
#         cleaned = cleaned.split(":", 1)[0].strip()

#     return cleaned.rstrip(":").strip().lower()


# def _build_styles():
#     styles = getSampleStyleSheet()

#     return {
#         "title": ParagraphStyle(
#             "CustomTitle",
#             parent=styles["Title"],
#             fontName="Helvetica-Bold",
#             fontSize=22,
#             leading=28,
#             alignment=TA_CENTER,
#             textColor=colors.HexColor("#16324F"),
#             spaceAfter=18,
#         ),
#         "heading": ParagraphStyle(
#             "CustomHeading",
#             parent=styles["Heading2"],
#             fontName="Helvetica-Bold",
#             fontSize=14,
#             leading=18,
#             alignment=TA_LEFT,
#             textColor=colors.HexColor("#1F4E79"),
#             spaceBefore=10,
#             spaceAfter=8,
#         ),
#         "body": ParagraphStyle(
#             "CustomBody",
#             parent=styles["BodyText"],
#             fontName="Helvetica",
#             fontSize=11,
#             leading=16,
#             alignment=TA_LEFT,
#             textColor=colors.HexColor("#2E2E2E"),
#             spaceAfter=8,
#         ),
#         "bullet": ParagraphStyle(
#             "CustomBullet",
#             parent=styles["BodyText"],
#             fontName="Helvetica",
#             fontSize=11,
#             leading=16,
#             alignment=TA_LEFT,
#             textColor=colors.HexColor("#2E2E2E"),
#             leftIndent=16,
#             bulletIndent=4,
#             spaceAfter=6,
#         ),
#     }


# def generate_pdf(content, filename="notes.pdf"):
#     doc = SimpleDocTemplate(
#         filename,
#         pagesize=A4,
#         rightMargin=50,
#         leftMargin=50,
#         topMargin=60,
#         bottomMargin=50,
#     )
#     styles = _build_styles()

#     elements = []
#     lines = [line.rstrip() for line in content.split("\n")]
#     title_added = False

#     for line in lines:
#         clean_line = _clean_line(line)

#         if not clean_line:
#             continue

#         normalized_heading = _normalize_heading(clean_line)

#         if ":" in clean_line and normalized_heading == "video title":
#             _, _, title_text = clean_line.partition(":")

#             elements.append(Paragraph("Video Title", styles["heading"]))

#             if title_text.strip():
#                 elements.append(Paragraph(title_text.strip(), styles["title"]))
#                 title_added = True

#             continue

#         if normalized_heading in SECTION_HEADINGS:
#             elements.append(Paragraph(clean_line, styles["heading"]))
#             continue

#         if not title_added:
#             elements.append(Paragraph(clean_line, styles["title"]))
#             title_added = True
#             continue

#         if clean_line.startswith(BULLET_MARKERS):
#             bullet_text = clean_line.lstrip("-*\u2022 ").strip()
#             elements.append(Paragraph(f"&bull; {bullet_text}", styles["bullet"]))
#             continue

#         elements.append(Paragraph(clean_line, styles["body"]))

#     doc.build(elements)

#     return filename



from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(content, filename="notes.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "AI Generated Learning Notes",
        styles["Title"]
    )

    elements.append(title)
    elements.append(Spacer(1, 20))

    for line in content.split("\n"):

        if line.strip():

            elements.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            elements.append(
                Spacer(1, 5)
            )

    doc.build(elements)

    return filename