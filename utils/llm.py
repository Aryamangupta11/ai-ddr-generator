import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()["choices"][0]["message"]["content"]

def extract_observations(text, doc_type):
    prompt = f"""
You are an expert inspection analyst.

Extract structured observations from the following {doc_type}.

Return ONLY valid JSON.

IMPORTANT:
- If area is not mentioned → keep "Not Available"
- Do NOT guess or assume areas

Format:
[
  {{
    "area": "...",
    "issue": "...",
    "severity": "...",
    "temperature": "...",
    "notes": "..."
  }}
]

TEXT:
{text[:4000]}
"""

    return call_llm(prompt)