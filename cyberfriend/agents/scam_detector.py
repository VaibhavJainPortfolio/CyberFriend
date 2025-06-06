# agents/scam_detector.py

from openai import OpenAI as OpenAIClient
import anthropic
from langdetect import detect

def detect_language(text):
    try:
        lang = detect(text)
        return "Hindi" if lang == "hi" else "English"
    except:
        return "Unknown"

def build_prompt(text, language):
    if language == "Hindi":
        return f"""
आप एक साइबर सुरक्षा विशेषज्ञ एआई हैं। नीचे दिए गए संदेश का विश्लेषण करें और इस सटीक प्रारूप में उत्तर दें:

- संदिग्ध है?: हाँ / नहीं / शायद
- कारण:
- चेतावनी संकेत:

संदेश:
\"\"\"{text}\"\"\"

⚠️ कृपया स्वरूप को न बदलें। उत्तर स्पष्ट और संक्षिप्त हो।
"""
    else:
        return f"""
You are a cybersecurity expert AI. Analyze the message below and respond in this exact format:

- Suspicious?: Yes / No / Maybe
- Reason:
- Warning signs:

Message:
\"\"\"{text}\"\"\"

⚠️ Do not skip or modify the format. Respond clearly and briefly.
"""

def check_scam(text: str, model_provider: str, api_key: str) -> str:
    try:
        language = detect_language(text)
        prompt = build_prompt(text, language)

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
                model="claude-3-haiku-20240307",
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