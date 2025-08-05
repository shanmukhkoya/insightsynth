# 🧠 InsightSynth — Lightweight GenAI Email Insight Extractor

**InsightSynth** is a zero-cost, fully local, GenAI-powered application that extracts structured insights (summary, action items, categories) 
from email text files. It is designed to work in **isolated environments**, using **open-source LLMs like TinyLlama and Phi-3** via Ollama. 
The app supports both single-file and batch processing, and outputs insights in both **Markdown and PDF formats**.

---

## 🚀 Features

- ✅ **LLM-Powered Insight Extraction** using local Ollama models (`phi3`, `tinyllama`)
- 📁 **Batch mode**: Process multiple `.txt` or `.eml` files from a directory
- 📄 **Markdown and PDF Reports**: Clean and shareable summaries
- 🧾 **Metadata Parsing**: Extracts `From`, `Date`, and `Subject` from email headers
- 🧱 **Modular Architecture** 
## 📂 Directory Structure

```

insightsynth/
├── config.yaml                  # Configuration file
├── main.py                      # Entry point for batch/single run
├── outputs/
│   ├── markdown/                # Markdown output files
│   └── pdf/                     # PDF output files
├── src/
│   ├── loader.py                # Email file loader and parser
│   ├── genai\_client.py          # Insight extraction using Ollama
│   └── formatter.py             # Markdown/PDF file generation
├── test\_emails/                 # Sample email `.txt` files
└── unittesting/                 # (Optional) Test scripts

````

---

## ⚙️ Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Ollama model: `phi3` or `tinyllama`

Install dependencies (if any):
```bash
pip install -r requirements.txt  # Not mandatory yet unless expanded
````

---

## 🛠️ Configuration

Edit the `config.yaml` file to control behavior:

```yaml
input_type: "txt"         # or "eml"
input_path: "test_emails/"  # Path to file or folder of email(s)

save_output:
  markdown: true
  pdf: true

ollama_model: "phi3"      # Any model installed locally in Ollama
```

---

## ▶️ Usage

### 🔹 1. Run in Batch Mode

Process all `.txt` or `.eml` files inside a folder:

```bash
python main.py
```

### 🔹 2. Run in Single File Mode

Just change `input_path:` in `config.yaml` to a specific file path:

```yaml
input_path: "test_emails/01_example_email.txt"
```

---

## 📤 Output Examples

For each email processed, you'll get:

* A `.md` file under `outputs/markdown/`
* A `.pdf` file under `outputs/pdf/`

Markdown sample:

```markdown
# Email Insight

**From:** aiupdate@openaiweekly.com  
**Date:** Tue, 5 Aug 2025 09:30:00 +0000

---

## Extracted Insights

**Summary:** HuggingFace integrated Whisper-ASR into its pipeline. OpenAI released a new NLP model “Turing”.

**Action Items:**
- Follow updates from OpenAI and HuggingFace
- Share with internal AI research team

**Category:** AI, NLP

---

## Original Email

Hello Team,  
Here are the top AI highlights for this week...
```

---

## 💡 Sample Use Cases

* 🤖 Summarizing AI weekly updates
* 📩 Processing contact center escalation emails
* 🧠 Internal knowledge gathering for RAG pipelines
* 🗃️ Extracting and storing insights from HR, policy, or product updates

---

## 🏗️ Future Roadmap

* [ ] Add SQLite storage for insights (RAG-ready)
* [ ] CLI-based interface for previewing reports
* [ ] Integration with Gmail or Outlook via IMAP or n8n
* [ ] Support for `.eml` with attachments
* [ ] Embedding support for similarity-based retrieval

---

## 🙌 Credits

Built with ❤️ by **Shanmukh Koya** as part of a self-driven GenAI learning journey
Using open-source models via [Ollama](https://ollama.com/)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

```

---

