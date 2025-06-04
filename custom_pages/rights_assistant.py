# pages/rights_assistant.py
import streamlit as st
from PIL import Image
from components import footer
from utils.gemini_helper import get_legal_answer_with_memory

def show():
    # st.markdown("<h2>🛡️ Rights Assistant</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="margin: 1rem 0; text-align: center;">
        <div style="background-color: #1169c0; color: white; padding: 2rem; border-radius: 1rem; width: 30%; margin: auto;">
            <span style="font-size: 2rem; font-weight: bold;">
            Rights Assistant
            </span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("#### Ask a legal question to CivGuardian Bot!")
    st.markdown(
        "<small style='color:gray;'>"
        "Disclaimer: CivGuardian Bot is powered by AI and may generate inaccurate information. "
        "Please verify with a legal professional."
        "</small>",
        unsafe_allow_html=True
    )

    left_col, right_col = st.columns([2, 1])

    with left_col:
        # Initialize session state for chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if "language" not in st.session_state:
            st.session_state.language = "English"

        st.session_state.language = st.selectbox(
            "Language", ["English", "Filipino"],
            index=["English", "Filipino"].index(st.session_state.language)
        )

        # Clear-chat button
        if st.button("Clear Chat", key="clear_chat"):
            st.session_state.chat_history = []
            st.rerun()

        # Inject CSS for scrollable chat container
        st.markdown("""
            <style>
            .chat-container {
                height: 400px;
                overflow-y: auto;
                background-color: transparent;
                padding: 1rem;
                border-radius: 10px;
                border: 1px solid #ccc;
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
            .user-msg {
                align-self: flex-end;
                background-color: #1169c0;
                color: white;
                padding: 0.75rem;
                border-radius: 12px;
                max-width: 75%;
                word-wrap: break-word;
            }
            .bot-msg {
                align-self: flex-start;
                background-color: #f0f0f0;
                color: black;
                border: 1px solid #1169c0;
                padding: 0.75rem;
                border-radius: 12px;
                max-width: 75%;
                word-wrap: break-word;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Render chat history
        chat_html = "<div class='chat-container'>"
        for msg in st.session_state.chat_history:
            css_class = "user-msg" if msg["role"] == "user" else "bot-msg"
            # chat_html += f"<div class='{css_class}'>{msg['content']}</div>"
            chat_html += f"<div class='{css_class}'>Hello. This feature is disabled for now as the github repository is available online and therefore makes the Gemini Key public which I can't allow. </div>"
        chat_html += "</div>"
        st.markdown(chat_html, unsafe_allow_html=True)

        # Input + Send on same line
        with st.form("chat_input", clear_on_submit=True):
            col1, col2 = st.columns([8, 2])
            with col1:
                user_input = st.text_input("You:", key="chat_text_input", label_visibility="collapsed")
            with col2:
                submitted = st.form_submit_button("Send")

            if submitted and user_input.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_input})

                with st.spinner("Gemini is thinking..."):
                    gemini_response = get_legal_answer_with_memory(
                        st.session_state.chat_history,
                        language=st.session_state.language
                    )
                    st.session_state.chat_history.append({"role": "assistant", "content": gemini_response})

                st.rerun()

    with right_col:
        image = Image.open("assets/assistant-page.jpg")
        width, height = image.size
        desired_ratio = 3 / 4
        if height / width > desired_ratio:
            new_height = int(width * desired_ratio)
            top = (height - new_height) // 2
            bottom = top + new_height
            left = 0
            right = width
        else:
            new_width = int(height / desired_ratio)
            left = (width - new_width) // 2
            right = left + new_width
            top = 0
            bottom = height

        cropped = image.crop((left, top, right, bottom))
        st.image(cropped, use_container_width=True)

    st.divider()
    
