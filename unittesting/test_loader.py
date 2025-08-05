import sys
import os

# 👇 Add the project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.loader import load_email

data = load_email("emails/sample_email.txt")
print(data)

