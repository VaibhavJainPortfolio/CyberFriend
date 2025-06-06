import re

def detect_type(text):
    text = text.strip().lower()
    url_pattern = r"(https?:\/\/[^\s]+)|(www\.[^\s]+)"
    if re.search(url_pattern, text):
        return "Link"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.search(email_pattern, text):
        return "Email"
    sms_keywords = ["otp", "offer", "win", "click", "call", "limited", "urgent", "congratulations"]
    if len(text.split()) <= 25 and any(kw in text for kw in sms_keywords):
        return "SMS"
    return "Generic Message"