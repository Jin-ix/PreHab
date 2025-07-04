import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Report & Graphs", layout="centered")
st.title("📄 Injury Risk Report")

coach = st.session_state.get("coach", None)
if not coach:
    st.warning("Please login first.")
    st.stop()

csv_path = f"data/{coach}_history.csv"
if not os.path.exists(csv_path):
    st.info("No records found.")
    st.stop()

df = pd.read_csv(csv_path)

st.subheader("📂 Raw Data")
st.dataframe(df)

st.subheader("📊 Risk Level Distribution")
fig, ax = plt.subplots()
df["Risk"].value_counts().plot(kind='bar', color="#3498db", ax=ax)
ax.set_ylabel("Count")
ax.set_title("Injury Risk Distribution")
st.pyplot(fig)

st.download_button("📥 Download Report as CSV", df.to_csv(index=False), "PreHab_Report.csv", "text/csv")
