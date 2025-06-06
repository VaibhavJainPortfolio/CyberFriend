# app.py

import streamlit as st
from agents.content_analyzer import detect_type
from agents.scam_detector import check_scam, detect_language
from agents.risk_scorer import score_risk
from agents.recommendation import get_recommendation

# Set page config
st.set_page_config(page_title="CyberFriend - Scam Detector", layout="centered")
st.title("🛡️ CyberFriend: Scam Detector & Advisor")

st.markdown("Enter a suspicious message, choose your AI provider, and let our agents analyze it intelligently.")

# Provider + API Key input
model_provider = st.selectbox("🤖 Choose AI Model Provider", ["OpenAI", "Claude"])
api_key = st.text_input("🔑 Enter your API Key (never stored)", type="password")

# Input area
user_input = st.text_area("📝 Paste the suspicious message or link below", height=200)

# Analyze
if st.button("🔎 Analyze"):
    if not user_input.strip() or not api_key:
        st.warning("Please enter both the message and your API key.")
    else:
        with st.spinner("Analyzing with Cyber Agents..."):

            # Detect message type and language
            content_type = detect_type(user_input)
            language = detect_language(user_input)

            # Scam analysis
            scam_analysis = check_scam(user_input, model_provider=model_provider, api_key=api_key)

            # Score it
            risk = score_risk(scam_analysis)
            risk_score = risk["score"]
            risk_level = risk["level"]

            # Recommendation (in user's language)
            advice = get_recommendation(risk_level, language)

        # Display Results
        st.success("✅ Analysis Complete!")

        st.subheader("📄 Detected Info")
        st.markdown(f"- **Type:** `{content_type}`")
        st.markdown(f"- **Language:** `{language}`")

        st.subheader("🧠 Scam Analysis")
        st.markdown(scam_analysis)

        st.subheader("📊 Risk Score")
        st.markdown(f"**Level:** `{risk_level}` — **Score:** `{risk_score}%`")

        st.subheader("🧭 Recommendation")
        st.markdown(advice)

# Footer
st.markdown("---")
st.markdown("🚀 Built with ❤️ by **Neuratantra AI** | Vaibhav Jain")