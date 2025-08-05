import os
from email import policy
from email.parser import BytesParser

def load_email(filepath):
    _, ext = os.path.splitext(filepath)

    if ext.lower() == ".eml":
        with open(filepath, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        subject = msg["subject"] or "No Subject"
        from_ = msg["from"] or "Unknown Sender"
        date = msg["date"] or "Unknown Date"

        # Get plain text body
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_content()
                    break
            else:
                body = ""
        else:
            body = msg.get_content()

        return {
            "subject": subject,
            "from": from_,
            "date": date,
            "body": body,
        }

    else:
        # For .txt or others: simple parsing assuming headers in first 3 lines
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        subject = lines[0].replace("Subject:", "").strip() if lines else "No Subject"
        from_ = lines[1].replace("From:", "").strip() if len(lines) > 1 else "Unknown Sender"
        date = lines[2].replace("Date:", "").strip() if len(lines) > 2 else "Unknown Date"
        body = "".join(lines[4:]) if len(lines) > 4 else ""

        return {
            "subject": subject,
            "from": from_,
            "date": date,
            "body": body,
        }
