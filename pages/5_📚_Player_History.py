import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Player History", layout="wide")
st.title("📚 Player Risk History")

coach = st.session_state.get("coach", None)
if not coach:
    st.warning("Please login first.")
    st.stop()

csv_path = f"data/{coach}_history.csv"
if not os.path.exists(csv_path):
    st.info("No history available.")
    st.stop()

df = pd.read_csv(csv_path)

st.dataframe(df)

# Optional: Filter by player
players = df["Player"].unique().tolist()
selected = st.selectbox("Filter by Player", ["All"] + players)

if selected != "All":
    filtered_df = df[df["Player"] == selected]
    st.write(f"Showing history for: **{selected}**")
    st.dataframe(filtered_df)
