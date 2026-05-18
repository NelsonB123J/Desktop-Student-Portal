from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle,
    Paragraph, Spacer, Image
)
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from datetime import datetime
import os
import sys

def create_transcript(gpa1, gpa2, cgpa, data, data2, student_info, active_year):


    YEAR_TITLE = f"{active_year} Result"
    name = student_info[0][1]
    HEADER_BG = colors.lightblue
    DATA_BG = colors.white
    GRID_COLOR = colors.black
    TEXT_COLOR = colors.black

    OUTPUT_FILE = os.path.join(
        os.path.expanduser("~"),
        "Downloads",
        f"{name}_{active_year}_academic_transcript.pdf"
    )

    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    LOGO_FILE = os.path.join(bundle_dir, "ase_logo.png")

    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    elements = []

    school_style = ParagraphStyle(
        name="SchoolTitle",
        fontSize=16,
        fontName="Helvetica-Bold",
        alignment=TA_CENTER,
        spaceAfter=4,
        leading=20,
        textColor=TEXT_COLOR
    )

    subtitle_style = ParagraphStyle(
        name="Subtitle",
        fontSize=11,
        fontName="Helvetica",
        alignment=TA_CENTER,
        spaceAfter=12,
        textColor=colors.grey
    )

    section_style = ParagraphStyle(
        name="Section",
        fontSize=12,
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        spaceAfter=8,
        textColor=TEXT_COLOR
    )

    gpa_style = ParagraphStyle(
        name="GPA",
        fontSize=12,
        fontName="Helvetica-Bold",
        alignment=TA_LEFT,
        spaceAfter=30,
        textColor=TEXT_COLOR
    )

    footer_style = ParagraphStyle(
        name="Footer",
        fontSize=10,
        fontName="Helvetica",
        alignment=TA_LEFT,
        textColor=TEXT_COLOR
    )

    logo = Image(LOGO_FILE, width=70, height=70)
    logo.hAlign = "CENTER"
    elements.append(logo)
    elements.append(Spacer(1, 8))

    elements.append(
        Paragraph("<b>African School of Economics</b>", school_style)
    )
    elements.append(
        Paragraph("Official Academic Transcript", subtitle_style)
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph("<b>Student Information</b>", section_style)
    )

    info_table = Table(student_info, colWidths=[160, 260])
    info_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("BACKGROUND", (0, 0), (0, -1), HEADER_BG),
        ("BACKGROUND", (1, 0), (-1, -1), DATA_BG),
        ("FONT", (0, 0), (0, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 25))

    elements.append(
        Paragraph(f"<b>{YEAR_TITLE}</b>", section_style)
    )
    elements.append(Spacer(1, 12))


    elements.append(
        Paragraph("<b>First Semester</b>", section_style)
    )

    courses = data[:]
    courses.insert(0, ["Course Code", "Credits", "Score", "Grade"])

    course_table = Table(courses, colWidths=[150, 80, 80, 80])
    course_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("BACKGROUND", (0, 1), (-1, -1), DATA_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(course_table)
    elements.append(Spacer(1, 20))


    elements.append(
        Paragraph("<b>Second Semester</b>", section_style)
    )

    courses2 = data2[:]
    courses2.insert(0, ["Course Code", "Credits", "Score", "Grade"])

    course_table2 = Table(courses2, colWidths=[150, 80, 80, 80])
    course_table2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("BACKGROUND", (0, 1), (-1, -1), DATA_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID_COLOR),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, -1), TEXT_COLOR),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    elements.append(course_table2)
    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(f"<b>First Semester GPA:</b> {gpa1}", gpa_style)
    )
    elements.append(
        Paragraph(f"<b>Second Semester GPA:</b> {gpa2}", gpa_style)
    )
    elements.append(
        Paragraph(f"<b>Cumulative Grade Point Average (CGPA):</b> {cgpa}", gpa_style)
    )

    date = datetime.now().strftime("%B %d, %Y")
    elements.append(
        Paragraph(
            f"This transcript is issued by the African School of Economics "
            f"for official academic purposes. Date: {date}",
            footer_style
        )
    )

    doc.build(elements)


if __name__ == "__main__":
    from Academic_Status import Academic_Status
    instance = Academic_Status(None)
    create_transcript(instance.gpa1, instance.gpa2, instance.cgpa, instance.data, instance.data2)