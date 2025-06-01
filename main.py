# main.py
import streamlit as st
from components import login, footer, profile
from pages import dashboard, rights_assistant, report_center, scorecard, admin_panel

# -----------------------------
# Session State Setup
# -----------------------------
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.is_admin = False
    st.session_state.username = ""

# -----------------------------
# App Entry
# -----------------------------
if not st.session_state.authenticated:
    login.show_login()
else:
    st.sidebar.title("CivicGuardian Navigation")
    tab = st.sidebar.radio("Go to:", ["Dashboard", "Rights Assistant", "Report Center", "Institution Scorecard"] + (["Admin Panel"] if st.session_state.is_admin else []))

    with st.container():
        st.markdown(
            f"<div style='text-align: right'><a href='#profile-tab'>👤 Profile</a></div>",
            unsafe_allow_html=True
        )

    if tab == "Dashboard":
        dashboard.show()
    elif tab == "Rights Assistant":
        rights_assistant.show()
    elif tab == "Report Center":
        report_center.show()
    elif tab == "Institution Scorecard":
        scorecard.show()
    elif tab == "Admin Panel":
        admin_panel.show()

    if st.query_params.get("tab") == "profile-tab":
        profile.show()
