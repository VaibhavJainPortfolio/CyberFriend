# agents/scam_detector.py

from openai import OpenAI as OpenAIClient
import anthropic

def check_scam(text: str, model_provider: str, api_key: str) -> str:
    """
    Detects scams using either OpenAI or Claude API.
    """

    prompt = f"""
You are a cybersecurity expert AI. Analyze the following message and determine if it could be a phishing attempt or a scam.

Message:
\"\"\"{text}\"\"\"

Please answer in the following structured format:

- Is this message suspicious? (Yes/No/Maybe)
- Reason for your answer (highlight any suspicious patterns)
- Warning signs, if any (like urgency, reward claims, unknown sender, etc.)

Respond clearly and concisely.
"""

    try:
        if model_provider == "OpenAI":
            client = OpenAIClient(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=300
            )
            return response.choices[0].message.content.strip()

        elif model_provider == "Claude":
            client = anthropic.Anthropic(api_key=api_key)
            response = client.messages.create(
                model="claude-3-haiku-20240307",  # ✅ Most accessible model
                max_tokens=500,
                temperature=0.3,
                system="You are a cybersecurity expert AI.",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()

        else:
            return "❌ Unsupported model provider."

    except Exception as e:
        return f"❌ Error analyzing scam: {e}"