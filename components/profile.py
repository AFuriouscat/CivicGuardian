# components/profile.py
import streamlit as st
from components import footer

def show():
    col1, col2, col3 = st.columns([3, 6, 3])
    
    with col2:
        st.header("Profile")
        st.write(f"Logged in as: **{st.session_state.username}**")
        st.selectbox("Preferred Language", ["English", "Filipino"])
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.session_state.is_admin = False
            st.rerun()
