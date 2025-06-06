# agents/recommendation.py

def get_recommendation(risk_level: str, language: str = "English") -> str:
    risk_level = risk_level.lower()
    language = language.lower()

    if language == "hindi":
        if risk_level == "high":
            return (
                "🚨 **उच्च जोखिम की चेतावनी**\n\n"
                "- किसी भी लिंक पर क्लिक न करें।\n"
                "- संदेश का उत्तर न दें।\n"
                "- इसे अपने ईमेल प्रदाता या स्थानीय साइबर अपराध सेल को रिपोर्ट करें।\n"
                "- प्रेषक को ब्लॉक करने पर विचार करें।"
            )
        elif risk_level == "medium":
            return (
                "⚠️ **मध्यम जोखिम**\n\n"
                "- सावधान रहें।\n"
                "- प्रेषक की पहचान की पुष्टि करें।\n"
                "- किसी लिंक पर क्लिक करने से पहले जांच लें।"
            )
        elif risk_level == "low":
            return (
                "✅ **कम जोखिम**\n\n"
                "- संदेश सामान्य लगता है, लेकिन सतर्क रहें।\n"
                "- यदि संदेह हो तो किसी विशेषज्ञ से सलाह लें।"
            )
        else:
            return (
                "❓ **अनिश्चित जोखिम स्तर**\n\n"
                "- जोखिम स्तर को स्पष्ट रूप से निर्धारित नहीं किया जा सका।\n"
                "- सावधानी बरतें और ज़रूरत पड़ने पर विशेषज्ञ की मदद लें।"
            )

    # English fallback
    if risk_level == "high":
        return (
            "🚨 **High Risk Detected**\n\n"
            "- Do NOT click any links.\n"
            "- Do NOT reply to the message.\n"
            "- Report this to your email provider or local cybercrime cell.\n"
            "- Consider blocking the sender."
        )
    elif risk_level == "medium":
        return (
            "⚠️ **Moderate Risk Detected**\n\n"
            "- Be cautious.\n"
            "- Double-check the sender’s identity.\n"
            "- Avoid clicking any links until verified."
        )
    elif risk_level == "low":
        return (
            "✅ **Low Risk Detected**\n\n"
            "- The message appears safe, but always stay alert.\n"
            "- If unsure, consult an expert or report for review."
        )
    else:
        return (
            "❓ **Uncertain Risk Level**\n\n"
            "- Unable to determine the risk confidently.\n"
            "- Use caution and verify with a cybersecurity expert if needed."
        )