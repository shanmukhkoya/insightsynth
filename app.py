import gradio as gr
from src.genai_client import extract_insights

def analyze_input(email_text, email_file):
    if email_file is not None:
        try:
            with open(email_file.name, "r", encoding="utf-8") as f:
                email_text = f.read()
        except Exception as e:
            return f"❌ Error reading uploaded file: {e}"

    if not email_text.strip():
        return "⚠️ Please provide email text or upload a file."

    return extract_insights(email_text)

with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue")) as demo:
    gr.Markdown("## ✨ InsightSynth — Email Insight Extractor")
    gr.Markdown("Upload an email file **or** paste text directly to generate structured insights.")

    with gr.Row():
        email_input = gr.Textbox(label="📩 Paste Email Text", lines=10, placeholder="Paste email body here...")
        email_file = gr.File(label="📎 Upload Email File", file_types=[".txt", ".eml"], type="file")

    analyze_btn = gr.Button("🔍 Extract Insights")
    output = gr.Textbox(label="📑 Insights", lines=15)

    analyze_btn.click(analyze_input, inputs=[email_input, email_file], outputs=output)

if __name__ == "__main__":
    demo.launch()