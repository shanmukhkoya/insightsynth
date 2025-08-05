import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name).strip().replace(" ", "_")

def save_markdown(insight_text, metadata, email_body=None, filename=None):
    if not filename:
        subject = sanitize_filename(metadata.get("subject", "No_Subject"))
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{subject}_{date_str}"

    filepath = os.path.join("outputs/markdown", f"{filename}.md")

    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Email Insight\n\n")
            f.write(f"**From:** {metadata.get('from', 'Unknown')}\n\n")
            f.write(f"**Date:** {metadata.get('date', 'Unknown')}\n\n")
            f.write("---\n\n")
            f.write("## Extracted Insights\n\n")
            f.write(insight_text + "\n\n")
            if email_body:
                f.write("---\n\n")
                f.write("## Original Email\n\n")
                f.write(email_body + "\n")
        print(f"✅ Markdown saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error saving Markdown: {e}")
        return None

def save_pdf(insight_text, metadata, email_body=None, filename=None):
    if not filename:
        subject = sanitize_filename(metadata.get("subject", "No_Subject"))
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{subject}_{date_str}"

    filepath = os.path.join("outputs/pdf", f"{filename}.pdf")

    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        doc = SimpleDocTemplate(filepath, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        story.append(Paragraph("<b>Email Insight</b>", styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"<b>From:</b> {metadata.get('from', 'Unknown')}", styles['Normal']))
        story.append(Paragraph(f"<b>Date:</b> {metadata.get('date', 'Unknown')}", styles['Normal']))
        story.append(Spacer(1, 12))
        story.append(Paragraph("<b>Extracted Insights</b>", styles['Heading2']))
        story.append(Spacer(1, 12))

        for line in insight_text.split("\n"):
            if line.strip() == "":
                story.append(Spacer(1, 12))
            else:
                story.append(Paragraph(line, styles['Normal']))

        if email_body:
            story.append(Spacer(1, 24))
            story.append(Paragraph("<b>Original Email</b>", styles['Heading2']))
            story.append(Spacer(1, 12))
            for line in email_body.split("\n"):
                if line.strip() == "":
                    story.append(Spacer(1, 12))
                else:
                    story.append(Paragraph(line, styles['Normal']))

        doc.build(story)
        print(f"✅ PDF saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error saving PDF: {e}")
        return None
