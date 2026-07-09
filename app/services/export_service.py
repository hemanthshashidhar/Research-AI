from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate


def generate_pdf(report: str) -> bytes:
    """
    Convert markdown report into a simple PDF.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    for line in report.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"],
                )
            )

    document.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
