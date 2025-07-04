import streamlit as st
from utils.auth import register_user, login_user
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Login / Register", layout="centered")

st.title("🔐 Coach Access")

auth_option = st.radio("Choose an action:", ["Login", "Register"])
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if auth_option == "Register":
    if st.button("📝 Register"):
        register_user(username, password)
        st.success("Registered successfully! Please log in.")
elif auth_option == "Login":
    if st.button("🔑 Login"):
        if login_user(username, password):
            st.success("Login successful!")
            st.session_state["coach"] = username
            switch_page("3_📊_Risk_Analysis")
        else:
            st.error("Invalid username or password.")
