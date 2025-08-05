import sys
import os
from pathlib import Path
import yaml

# Add project root to path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.loader import load_email
from src.genai_client import extract_insights
from src.formatter import save_markdown, save_pdf

def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def process_file(file_path, config):
    try:
        email_data = load_email(str(file_path))
        insights = extract_insights(email_data["body"])

        metadata = {
            "subject": email_data["subject"],
            "from": email_data["from"],
            "date": email_data["date"]
        }

        if config["save_output"].get("markdown", False):
            save_markdown(insights, metadata, email_data["body"], filename=file_path.stem)

        if config["save_output"].get("pdf", False):
            save_pdf(insights, metadata, email_data["body"], filename=file_path.stem)

        print(f"✅ Processed: {file_path.name}")

    except Exception as e:
        print(f"❌ Error processing {file_path.name}: {e}")

def main():
    config = load_config()
    input_path = Path(config["input_path"])

    if input_path.is_file():
        # Process single file
        process_file(input_path, config)

    elif input_path.is_dir():
        # Process all .txt or .eml files
        input_type = config.get("input_type", "txt").lower()
        pattern = f"*.{input_type}"

        files = sorted(input_path.glob(pattern))
        if not files:
            print(f"⚠️ No {input_type.upper()} files found in {input_path}")
            return

        print(f"📂 Found {len(files)} {input_type.upper()} file(s) in {input_path}...\n")

        for file_path in files:
            process_file(file_path, config)

    else:
        print("❌ Invalid input_path specified in config.yaml")

if __name__ == "__main__":
    main()
