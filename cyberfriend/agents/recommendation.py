# agents/recommendation.py

def get_recommendation(risk_level: str) -> str:
    """
    Based on the risk level (High, Medium, Low), return a user-friendly recommendation.
    """

    risk_level = risk_level.lower()

    if risk_level == "high":
        return (
            "🚨 **High Risk Detected**\n\n"
            "- Do NOT click any links.\n"
            "- Do NOT reply to the message.\n"
            "- Report this to your email provider or local cybercrime cell.\n"
            "- Consider blocking the sender.\n"
        )

    elif risk_level == "medium":
        return (
            "⚠️ **Moderate Risk Detected**\n\n"
            "- Be cautious.\n"
            - "Double-check the sender’s identity.\n"
            "- Avoid clicking any links until verified.\n"
        )

    elif risk_level == "low":
        return (
            "✅ **Low Risk Detected**\n\n"
            "- The message appears safe, but always stay alert.\n"
            "- If unsure, consult an expert or report for review.\n"
        )

    else:
        return (
            "❓ **Uncertain Risk Level**\n\n"
            "- Unable to determine the risk confidently.\n"
            "- Use caution and verify with a cybersecurity expert if needed.\n"
        )