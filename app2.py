import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model, encoders, and scaler
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

st.set_page_config(page_title="PreHab Injury Predictor", layout="centered")
st.title("⚽ PreHab - Injury Risk Predictor")

st.markdown("Provide the player's training and health data:")

# Collect input matching dataset columns
player_name = st.selectbox("Player Name", ["Player1", "Player2", "Player3"])  # Dummy values, replace with real ones
period_name = st.selectbox("Training Period", ["Pre-season", "In-season", "Post-season"])
position_name = st.selectbox("Position", ["Forward", "Midfielder", "Defender", "Goalkeeper"])

total_load = st.number_input("Total Player Load", min_value=0.0, value=500.0)
load_per_min = st.number_input("Player Load Per Minute", min_value=0.0, value=3.5)
max_hr = st.number_input("Maximum Heart Rate", min_value=40, max_value=220, value=180)
min_hr = st.number_input("Minimum Heart Rate", min_value=30, max_value=150, value=60)
avg_hr = st.number_input("Average Heart Rate", min_value=40, max_value=200, value=120)

# Create input DataFrame
input_df = pd.DataFrame([{
    'Player.Name': player_name,
    'Period.Name': period_name,
    'Position.Name': position_name,
    'Total.Player.Load': total_load,
    'Player.Load.Per.Minute': load_per_min,
    'Maximum.Heart.Rate': max_hr,
    'Minimum.Heart.Rate': min_hr,
    'Avg.Heart.Rate': avg_hr
}])

# Encode categorical columns
for col in input_df.columns:
    if col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

# Ensure correct column order
try:
    input_df = input_df[scaler.feature_names_in_]
except Exception as e:
    st.error(f"❌ Feature alignment error: {e}")
    st.stop()

# Scale input
try:
    scaled_input = scaler.transform(input_df)
except Exception as e:
    st.error(f"❌ Scaling error: {e}")
    st.stop()

# Predict
if st.button("Predict Injury Risk"):
    try:
        prediction = model.predict(scaled_input)[0]
        st.success(f"✅ Predicted Injury Risk: **{prediction}**")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
