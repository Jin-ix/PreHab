import streamlit as st
from utils.prediction import predict_risk
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Risk Prediction", layout="centered")
st.title("📊 Injury Risk Prediction")

coach = st.session_state.get("coach", None)
if not coach:
    st.warning("Please login first.")
    st.stop()

st.subheader("🧍 Player Information")
player_name = st.text_input("Player Name")
position = st.selectbox("Position", ["D", "F", "GK"])

st.subheader("📈 Performance Metrics")
total_load = st.number_input("Total Player Load", min_value=0.0)
load_per_min = st.number_input("Player Load Per Minute", min_value=0.0)
max_hr = st.number_input("Max Heart Rate", min_value=0)
min_hr = st.number_input("Min Heart Rate", min_value=0)
avg_hr = st.number_input("Average Heart Rate", min_value=0.0)

if st.button("🧠 Predict Injury Risk"):
    result = predict_risk(position, total_load, load_per_min, max_hr, min_hr, avg_hr)
    st.success(f"🩺 Predicted Risk Level: **{result.upper()}**")

    # Save to CSV (simple log format)
    df = pd.DataFrame([{
        "Coach": coach,
        "Player": player_name,
        "Position": position,
        "Total Load": total_load,
        "Load/Min": load_per_min,
        "Max HR": max_hr,
        "Min HR": min_hr,
        "Avg HR": avg_hr,
        "Risk": result,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    filename = f"data/{coach}_history.csv"
    df.to_csv(filename, mode='a', index=False, header=not os.path.exists(filename))
