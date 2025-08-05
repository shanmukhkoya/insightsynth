import sys
import os

# 👇 This adds the root folder (insightsynth/) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.formatter import save_markdown, save_pdf

insight_text = """
**Summary:** AI updates this week include DALL·E 2 and Whisper ASR.

**Action Items:**
- Check OpenAI's new models
- Read Whisper documentation

**Category:** AI
"""

metadata = {
    "subject": "AI Weekly",
    "from": "aiupdate@example.com",
    "date": "Aug 5, 2025"
}

save_markdown(insight_text, metadata)
save_pdf(insight_text, metadata)
