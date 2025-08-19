import streamlit as st
from src.loader import load_email
from src.genai_client import extract_insights
from src.formatter import save_markdown, save_pdf
import tempfile
import os

st.set_page_config(page_title="InsightSynth", layout="wide")

st.title("📧 InsightSynth - Email Intelligence")
st.write("Upload emails or paste text to generate structured insights using LLMs.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload an email (.txt or .eml)", type=["txt", "eml"])

# --- Direct Text Input ---
email_text = st.text_area("Or paste email content here", height=200)

if st.button("🔍 Generate Insights"):
    if uploaded_file:
        # Save uploaded file to temp
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        email_data = load_email(tmp_path)
        os.unlink(tmp_path)
    elif email_text.strip():
        email_data = {
            "subject": "Manual Input",
            "from": "User",
            "date": "N/A",
            "body": email_text
        }
    else:
        st.error("Please upload a file or paste some text.")
        st.stop()

    st.info(f"**Processing email:** {email_data['subject']}")

    insights = extract_insights(email_data["body"])

    st.subheader("🧠 Extracted Insights")
    st.markdown(f"```\n{insights}\n```")

    with st.expander("📄 Original Email"):
        st.text(email_data["body"])

    # Save to outputs
    md_path = save_markdown(insights, email_data, email_data["body"])
    pdf_path = save_pdf(insights, email_data, email_data["body"])

    if md_path:
        with open(md_path, "rb") as f:
            st.download_button("⬇️ Download Markdown", f, file_name=os.path.basename(md_path))

    if pdf_path:
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name=os.path.basename(pdf_path))
