# pages/rights_assistant.py
import streamlit as st
from components import footer
from utils.gemini_helper import get_legal_answer

def show():
    st.header("🛡️ Rights Assistant")
    lang = st.selectbox("Language", ["English", "Filipino"])
    query = st.text_area("Ask a legal question")

    if st.button("Ask Gemini"):
        if not query.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Gemini is analyzing your question..."):
                response = get_legal_answer(query)
                st.success(f"Gemini says:\n\n{response}")
    footer.show()
