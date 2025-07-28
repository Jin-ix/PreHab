import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model, encoders, and scaler
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, encoders, scaler

model, encoders, scaler = load_model()

st.set_page_config(page_title="PreHab - Injury Risk Predictor", layout="centered")
st.title("🏥 PreHab - Injury Risk Predictor for Football Players")

# User input fields - change fields based on your dataset
st.subheader("Enter Player Data")

# Example fields (you must update this based on your dataset's features)
input_data = {
    "Age": st.slider("Age", 15, 45, 25),
    "BMI": st.slider("BMI", 15.0, 35.0, 22.5),
    "Minutes_Played": st.slider("Minutes Played", 0, 10000, 2000),
    "Previous_Injuries": st.selectbox("Previous Injuries", ["None", "Mild", "Moderate", "Severe"]),
    "Position": st.selectbox("Position", ["Forward", "Midfielder", "Defender", "Goalkeeper"]),
    "Training_Load": st.slider("Training Load (units)", 0, 100, 50),
    "Sleep_Hours": st.slider("Average Sleep (hrs)", 0.0, 12.0, 7.0),
    "Heart_Rate": st.slider("Average Heart Rate", 50, 200, 75),
}

input_df = pd.DataFrame([input_data])

# Encode categorical columns
for col in input_df.columns:
    if col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

# Scale numeric data
scaled_input = scaler.transform(input_df)

# Predict button
if st.button("Predict Injury Risk"):
    prediction = model.predict(scaled_input)[0]
    st.success(f"🏅 Predicted Injury Risk: **{prediction}**")
