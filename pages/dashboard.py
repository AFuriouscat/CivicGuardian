# pages/dashboard.py
import streamlit as st
from components import footer

import streamlit as st

def show():
    st.markdown("<div style='padding-left: 5rem; padding-right: 5rem;'>", unsafe_allow_html=True)

    # Header full width
    st.header("📊 Justice Dashboard")

    # Columns for custom width control
    col1, col2 = st.columns([2, 1])  # 2:1 width ratio

    with col1:
        st.write("Interactive stats and AI summaries.")
        st.line_chart({"Quezon City": [3, 7, 8, 9], "Manila": [1, 6, 5, 8]})

    st.info("🧠 Gemini: Case backlog in Quezon City is growing. Avg. resolution time: 287 days.")

    st.markdown("</div>", unsafe_allow_html=True)
