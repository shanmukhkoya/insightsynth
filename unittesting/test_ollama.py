import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.genai_client import extract_insights

sample_body = """
Hello Team,

Here are this week's AI updates:
- OpenAI released a new model.
- HuggingFace added Whisper-ASR to Transformers.

Regards,
AI Team
"""

response = extract_insights(sample_body)
print("🔍 Insights:\n", response)
