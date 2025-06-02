# components/login.py
import streamlit as st

def show_login():
    col1, col2, col3 = st.columns([3, 6, 3])
    
    with col2:
        st.title("CivicGuardian")
        st.subheader("\"One platform to report, understand and monitor justice in your city.\"")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_type = st.radio("Login as:", ["User", "Admin"])

        if st.button("Login"):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.is_admin = login_type == "Admin"
            st.rerun()

