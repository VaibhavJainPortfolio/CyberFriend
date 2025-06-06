# app.py

import streamlit as st
from agents.content_analyzer import detect_type
from agents.scam_detector import check_scam
from agents.risk_scorer import score_risk
from agents.recommendation import get_recommendation

st.set_page_config(page_title="CyberFriend - Scam Detector", layout="centered")
st.title("🛡️ CyberFriend: Scam Detector & Advisor")

st.markdown("Enter a suspicious message, choose your model provider, and let our agents assess the risk.")

# User selects provider and enters API key
model_provider = st.selectbox("Choose Model Provider", ["OpenAI", "Claude"])
api_key = st.text_input("Enter your API Key (won’t be stored)", type="password")

# User inputs message
user_input = st.text_area("🔍 Paste the suspicious content here", height=200)

# Analyze Button
if st.button("🔎 Analyze"):
    if not user_input.strip() or not api_key:
        st.warning("Please enter both a message and your API key.")
    else:
        with st.spinner("Analyzing using Cyber Agents..."):
            # 1. Detect Type
            content_type = detect_type(user_input)

            # 2. Scam Detection
            scam_analysis = check_scam(user_input, model_provider=model_provider, api_key=api_key)

            # 3. Risk Scoring
            risk = score_risk(scam_analysis)
            risk_score = risk['score']
            risk_level = risk['level']

            # 4. Recommendation
            advice = get_recommendation(risk_level)

        # Display Results
        st.success("✅ Analysis Complete!")

        st.subheader("📄 Content Type")
        st.markdown(f"**Detected Type:** `{content_type}`")

        st.subheader("🧠 Scam Analysis")
        st.markdown(scam_analysis)

        st.subheader("📊 Risk Score")
        st.markdown(f"**Level:** `{risk_level}` — **Score:** `{risk_score}%`")

        st.subheader("🧭 Recommendation")
        st.markdown(advice)