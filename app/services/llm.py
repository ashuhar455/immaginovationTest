import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a skincare assistant.

Rules:
- Only answer from given context
- If unsure, say you don't know
- Return strict JSON:
{
  "routine": [],
  "products": [],
  "warnings": []
}
"""

def generate_response(question: str, context: str) -> str:
    prompt = f"""
Context:
{context}

User Question:
{question}
"""

    response = client.chat.completions.create(
        model=os.getenv("OPEN_AI_MODEL"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
