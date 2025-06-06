# agents/content_analyzer.py

import re

def detect_type(text):
    """
    Detects the type of content: Link, Email, SMS, or Generic Message.
    Returns a string label.
    """

    text = text.strip().lower()

    # Check for URL or link
    url_pattern = r"(https?:\/\/[^\s]+)|(www\.[^\s]+)"
    if re.search(url_pattern, text):
        return "Link"

    # Check for email-like structure
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.search(email_pattern, text):
        return "Email"

    # Check for OTP or SMS language patterns
    sms_keywords = ["otp", "offer", "win", "click", "call", "limited", "urgent", "congratulations"]
    if len(text.split()) <= 25 and any(kw in text for kw in sms_keywords):
        return "SMS"

    # Default case
    return "Generic Message"