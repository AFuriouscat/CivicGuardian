# pages/dashboard.py
import streamlit as st
from components import footer

def show():
    st.header("📊 Justice Dashboard")
    st.write("Interactive stats and AI summaries.")
    st.line_chart({"Quezon City": [3, 7, 8, 9], "Manila": [1, 6, 5, 8]})
    st.info("🧠 Gemini: Case backlog in Quezon City is growing. Avg. resolution time: 287 days.")
    footer.show()
