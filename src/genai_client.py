import requests
import os
import subprocess

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"

def format_prompt(email_body):
    try:
        with open("prompts/insight_prompt.txt", "r", encoding="utf-8") as f:
            template = f.read()
        if "{email_body}" not in template:
            raise ValueError("Prompt template is missing the '{email_body}' placeholder.")
        return template.replace("{email_body}", email_body)
    except FileNotFoundError:
        print("❌ Error: Prompt template file not found at 'prompts/insight_prompt.txt'.")
        return None
    except Exception as e:
        print(f"❌ Error formatting prompt: {e}")
        return None



def extract_insights(email_body: str) -> str:
    prompt = f"""
Summarize the following email in 3 parts:

Summary:
- A concise summary

Action Items:
- List any action items from the email

Categories:
- One or more relevant categories like AI, HR, Marketing, etc.


Email:
{email_body}
"""
    try:
        result = subprocess.run(
            ["ollama", "run", "phi3"],
            input=prompt,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        print("❌ Ollama call failed:")
        print("Return Code:", e.returncode)
        print("STDERR:", e.stderr)
        return "Error: Could not generate insights."


    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()

        if "response" not in data:
            print("⚠️ No 'response' key found in Ollama result.")
            return "⚠️ LLM response missing."

        return data["response"].strip()

    except requests.exceptions.ConnectionError:
        return "❌ Unable to connect to Ollama. Is it running at http://localhost:11434?"

    except requests.exceptions.Timeout:
        return "❌ Request to Ollama timed out. Try again or check performance."

    except requests.exceptions.HTTPError as http_err:
        return f"❌ HTTP error from Ollama: {http_err.response.status_code} - {http_err.response.reason}"

    except Exception as e:
        return f"❌ Unexpected error during LLM call: {str(e)}"
