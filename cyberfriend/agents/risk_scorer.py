# agents/risk_scorer.py

def score_risk(analysis_text: str) -> dict:
    """
    Parses the analysis text and assigns a numerical risk score and level.
    Returns a dictionary with 'score' and 'level'.
    """

    analysis_text = analysis_text.lower()

    if "yes" in analysis_text:
        score = 85
        level = "High"
    elif "maybe" in analysis_text or "possibly" in analysis_text:
        score = 50
        level = "Medium"
    elif "no" in analysis_text:
        score = 10
        level = "Low"
    else:
        score = 30
        level = "Unknown"

    return {
        "score": score,
        "level": level
    }