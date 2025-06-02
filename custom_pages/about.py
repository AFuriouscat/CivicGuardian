# pages/about.py
import streamlit as st
from PIL import Image
from custom_pages import dashboard, rights_assistant, report_center, scorecard

def show():
    # --- 1) Wide banner across the top ---
    banner_path = "assets/banner-about-page.jpeg"  # Replace with your banner image
    try:
        banner_img = Image.open(banner_path)
        # Crop banner to 16:4 ratio (wide)
        w, h = banner_img.size
        target_ratio = 7 / 1  # width:height = 4:1 (adjust as needed)
        if w / h > target_ratio:
            # Too wide → crop width
            new_width = int(h * target_ratio)
            left = (w - new_width) // 2
            right = left + new_width
            top, bottom = 0, h
        else:
            # Too tall → crop height
            new_height = int(w / target_ratio)
            top = (h - new_height) // 2
            bottom = top + new_height
            left, right = 0, w

        banner_cropped = banner_img.crop((left, top, right, bottom))
        st.image(banner_cropped, use_container_width=True)
    except Exception:
        st.warning(f"Could not load banner image at `{banner_path}`.")

    # --- 2) Hero Text ---
    st.markdown(
        """
        <div style="margin:2rem 5rem; text-align:center;">
            <div style="background-color:#003366; color:white; padding:2rem; border-radius:1rem;">
                <span style="font-size:2rem; font-weight:bold;">
                    One platform to report, understand and monitor justice in your city.
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- 3) Four‐column card section, each with its own image ---
    # Define each card’s image path + title + button text + target key
    cards = [
        {
            "title": "📢 Report an Incident",
            "button": "Go to Report",
            "key": "go_report",
            "page_func": report_center.show,
            "image_path": "assets/report-page.jpg",  # Replace with your image
        },
        {
            "title": "🤖 AI Assistant",
            "button": "Ask Assistant",
            "key": "go_rights",
            "page_func": rights_assistant.show,
            "image_path": "assets/assistant-page.jpg",  # Replace with your image
        },
        {
            "title": "📊 Justice Dashboard",
            "button": "View Dashboard",
            "key": "go_dashboard",
            "page_func": dashboard.show,
            "image_path": "assets/dashboard-page.jpg",  # Replace with your image
        },
        {
            "title": "🏛 Institution Scorecard",
            "button": "View Scorecard",
            "key": "go_scorecard",
            "page_func": scorecard.show,
            "image_path": "assets/scorecard-page.jpg",  # Replace with your image
        },
    ]

    # Initialize session state for navigation if needed
    if "current_page" not in st.session_state:
        st.session_state.current_page = "about"

    # If user has already clicked a card, render that page first
    if st.session_state.current_page != "about":
        for card in cards:
            if card["key"] == st.session_state.current_page:
                if st.button("⬅️ Back to About", key="back_to_about"):
                    st.session_state.current_page = "about"
                    st.rerun()
                card["page_func"]()
                return

    # Style adjustments for spacing
    st.markdown("<div style='margin:2rem 5rem;'>", unsafe_allow_html=True)

    # Create a 4-column layout
    cols = st.columns(4, gap="large")
    for col, card in zip(cols, cards):
        with col:
            # Attempt to load + crop the card image to ~4:3 ratio
            try:
                img = Image.open(card["image_path"])
                w, h = img.size
                target_ratio = 4 / 3  # width:height = 4:3
                if w / h > target_ratio:
                    # Too wide: crop width
                    new_width = int(h * target_ratio)
                    left = (w - new_width) // 2
                    right = left + new_width
                    top, bottom = 0, h
                else:
                    # Too tall: crop height
                    new_height = int(w / target_ratio)
                    top = (h - new_height) // 2
                    bottom = top + new_height
                    left, right = 0, w

                cropped = img.crop((left, top, right, bottom))
                st.image(cropped, use_container_width=True)
            except Exception:
                st.warning(f"Could not load image at `{card['image_path']}`.")

            # Title under the image
            st.markdown(
                f"<div style='text-align:center; font-weight:bold; margin-top:1rem;'>{card['title']}</div>",
                unsafe_allow_html=True,
            )

            # Button to navigate
            if st.button(card["button"], key=card["key"]):
                st.session_state.current_page = card["key"]
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
