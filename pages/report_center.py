# pages/report_center.py
import streamlit as st
from components import footer

def show():
    st.header("📝 Report Center")
    st.text_input("Location")
    st.text_area("Describe the incident")
    st.file_uploader("Upload photo (optional)", type=["jpg", "png"])

    if st.button("Submit Report"):
        st.success("Report submitted anonymously. Gemini classifying...")
        st.info("Gemini: This appears to be a public harassment case. You may contact XYZ legal org.")
    footer.show()
