import streamlit as st
from pages import dashboard, rights_assistant, report_center, scorecard, admin_panel

def show():
    cards = [
        {"title": "📢 Report an Incident", "button": "Go to Report", "key": "go_report", "page_func": report_center.show},
        {"title": "🤖 AI Assistant", "button": "Ask Assistant", "key": "go_rights", "page_func": rights_assistant.show},
        {"title": "📊 Justice Dashboard", "button": "View Dashboard", "key": "go_dashboard", "page_func": dashboard.show},
        {"title": "🏛 Institution Scorecard", "button": "View Scorecard", "key": "go_scorecard", "page_func": scorecard.show},
    ]

    # Initialize session state for navigation
    if "current_page" not in st.session_state:
        st.session_state.current_page = "about"

    # Navigation rendering
    if st.session_state.current_page != "about":
        for card in cards:
            if card["key"] == st.session_state.current_page:
                # Add a "Back to About" button
                if st.button("⬅️ Back to About", key="back_to_about"):
                    st.session_state.current_page = "about"
                    st.rerun()

                # Call the selected page's function
                card["page_func"]()
                return

    # Styles for About page
    st.markdown("""
        <style>
        .hero {
            background-color: #003366;
            color: white;
            padding: 2rem;
            border-radius: 1rem;
            text-align: center;
            font-size: 2rem;
            margin: 2rem 5rem;
        }
        .card {
            background-color: #f2f2f2;
            border-radius: 1rem;
            padding: 2rem;
            text-align: center;
            height: 250px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card-title {
            font-size: 1.25rem;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hero banner
    st.markdown("<div class='hero'>One platform to report, understand and monitor justice in your city.</div>", unsafe_allow_html=True)

    # 4-column layout of cards
    cols = st.columns(4)
    for col, card in zip(cols, cards):
        with col:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='card-title'>{card['title']}</div>", unsafe_allow_html=True)
            if st.button(card["button"], key=card["key"]):
                st.session_state.current_page = card["key"]
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
