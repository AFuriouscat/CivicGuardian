# main.py
import streamlit as st
from components import login, footer, profile
from pages import dashboard, rights_assistant, report_center, scorecard, admin_panel

st.set_page_config(page_title="CivicGuardian", layout="wide")

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
    # -----------------------------
    # Header
    # -----------------------------
    with st.container():
        st.markdown("""
            <div style='background-color:#003366;padding:1rem;'>
                <div style='display:flex;justify-content:space-between;align-items:center;'>
                    <div style='color:white;font-size:1.5rem;font-weight:bold;'>CivicGuardian</div>
                    <div style='color:white;'>👤 {}</div>
                </div>
            </div>
            <div style='background-color:#00bcd4;padding:0.5rem;'>
                <a href='?tab=dashboard' style='margin-right:20px;color:white;text-decoration:none;'>Dashboard</a>
                <a href='?tab=rights' style='margin-right:20px;color:white;text-decoration:none;'>Rights Assistant</a>
                <a href='?tab=report' style='margin-right:20px;color:white;text-decoration:none;'>Report Center</a>
                <a href='?tab=scorecard' style='margin-right:20px;color:white;text-decoration:none;'>Institution Scorecard</a>
                {}  
            </div>
        """.format(
            st.session_state.username,
            "<a href='?tab=admin' style='color:white;text-decoration:none;'>Admin Panel</a>" if st.session_state.is_admin else ""
        ), unsafe_allow_html=True)

    # -----------------------------
    # Main Page Routing
    # -----------------------------
    tab = st.query_params.get("tab", "dashboard")

    with st.container():
        if tab == "dashboard":
            dashboard.show()
        elif tab == "rights":
            rights_assistant.show()
        elif tab == "report":
            report_center.show()
        elif tab == "scorecard":
            scorecard.show()
        elif tab == "admin" and st.session_state.is_admin:
            admin_panel.show()
        elif tab == "profile-tab":
            profile.show()

    # -----------------------------
    # Footer
    # -----------------------------
    st.markdown("""
        <div style='background-color:#003366;padding:2rem;margin-top:3rem;color:white;'>
            <div style='display:flex;justify-content:space-between;flex-wrap:wrap;'>
                <div>
                    <h4>Stay Connected</h4>
                    <a href='https://facebook.com' target='_blank' style='margin-right:10px;'>📘</a>
                    <a href='https://twitter.com' target='_blank' style='margin-right:10px;'>🐦</a>
                    <a href='https://youtube.com' target='_blank' style='margin-right:10px;'>▶️</a>
                    <a href='https://instagram.com' target='_blank'>📸</a>
                </div>
                <div>
                    <h4>Links</h4>
                    <a href='#' style='color:white;display:block;'>About Us & Legal Info</a>
                    <a href='#' style='color:white;display:block;'>Contact Us</a>
                    <a href='#' style='color:white;display:block;'>Privacy Policy</a>
                    <a href='#' style='color:white;display:block;'>Terms of Use</a>
                    <a href='#' style='color:white;display:block;'>Equal Opportunity</a>
                </div>
                <div style='text-align:right;'>
                    <p>By: Hack Pack 2025</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
