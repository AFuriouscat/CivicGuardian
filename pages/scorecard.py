# pages/scorecard.py
import streamlit as st
from components import footer

def show():
    st.header("🏛️ Institution Scorecard")
    st.write("Transparency and performance overview")
    st.metric("Barangay Transparency Score", "72%")
    st.metric("Court Efficiency", "48%")
    st.metric("Resolved Cases with Feedback", "34")
    st.warning("⚠️ AI detected pattern: Delays in Barangay 143 reporting")
    footer.show()
