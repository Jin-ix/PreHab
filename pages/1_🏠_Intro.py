import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="PreHab - Welcome", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #0A4D68;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #34495E;
        margin-bottom: 50px;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.image("assets/logo.png", width=180)
st.markdown('<div class="title">Welcome to PreHab</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Injury Risk Predictor & Virtual Rehab Assistant</div>', unsafe_allow_html=True)

if st.button("🚀 Start Now"):
    switch_page("2_🔐_Login_or_Register")

st.markdown('<div class="footer">© 2025 PreHab · Built with ❤️ for Sports Science</div>', unsafe_allow_html=True)
