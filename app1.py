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

st.markdown("Enter the player's health and training data below to predict their risk of injury.")

# Define input fields (replace/add fields based on your actual dataset)
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

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical columns
for col in input_df.columns:
    if col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

# Reorder columns to match what scaler/model expects
if hasattr(scaler, 'feature_names_in_'):
    try:
        input_df = input_df[scaler.feature_names_in_]
    except KeyError as e:
        st.error(f"Feature mismatch: {e}")
        st.stop()

# Scale the input
try:
    scaled_input = scaler.transform(input_df)
except Exception as e:
    st.error(f"Scaling error: {e}")
    st.stop()

# Predict on button click
if st.button("Predict Injury Risk"):
    try:
        prediction = model.predict(scaled_input)[0]
        st.success(f"🏅 Predicted Injury Risk: **{prediction}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
