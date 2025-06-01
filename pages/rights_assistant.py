# pages/rights_assistant.py
import streamlit as st
from components import footer

def show():
    st.header("🛡️ Rights Assistant")
    lang = st.selectbox("Language", ["English", "Filipino"])
    query = st.text_area("Ask a legal question")
    if st.button("Ask Gemini"):
        st.success("Gemini says: You have the right to... (AI reply placeholder)")
    footer.show()
