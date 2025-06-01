# pages/admin_panel.py
import streamlit as st
from components import footer

def show():
    st.header("🔐 Admin Panel")
    st.write("Manage reports, flagged submissions, system logs")
    st.dataframe({
        "Case ID": [101, 102],
        "Status": ["Open", "Under Review"],
        "Flagged": ["No", "Yes"]
    })
    st.button("Export CSV")
   