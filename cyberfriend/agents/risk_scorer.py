# agents/risk_scorer.py

def score_risk(analysis_text: str) -> dict:
    text = analysis_text.lower().replace("?", "").strip()

    # Check English keywords
    if "suspicious" in text:
        if "yes" in text:
            return {"score": 85, "level": "High"}
        elif "maybe" in text:
            return {"score": 50, "level": "Medium"}
        elif "no" in text:
            return {"score": 10, "level": "Low"}

    # Check Hindi keywords
    if "संदिग्ध" in text:
        if "हाँ" in text:
            return {"score": 85, "level": "High"}
        elif "शायद" in text:
            return {"score": 50, "level": "Medium"}
        elif "नहीं" in text:
            return {"score": 10, "level": "Low"}

    # Default fallback
    return {"score": 30, "level": "Unknown"}