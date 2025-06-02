# pages/scorecard.py
import streamlit as st

from PIL import Image
from components import footer

def show():
    st.markdown(
        """
        <div style="margin: 1rem 0; text-align: center;">
        <div style="background-color: #1169c0; color: white; padding: 2rem; border-radius: 1rem; width: 30%; margin: auto;">
            <span style="font-size: 2rem; font-weight: bold;">
            Institution Scorecard
            </span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.write("Transparency and performance overview")
        st.metric("Barangay Transparency Score", "72%")
        st.metric("Court Efficiency", "48%")
        st.metric("Resolved Cases with Feedback", "34")
        st.warning("⚠️ AI detected pattern: Delays in Barangay 143 reporting")

    with right_col:
        # Load the image
        image = Image.open("assets/scorecard-page.jpg")

        # Get original dimensions
        width, height = image.size

        # Desired aspect ratio: 3:2 (height:width)
        desired_ratio = 3 / 4  # height divided by width

        # Compute new crop box dimensions
        # Strategy: Fix width, compute height from ratio (height = width * 1.5)
        if height / width > desired_ratio:
            # Image is too tall — crop height
            new_height = int(width * desired_ratio)
            top = (height - new_height) // 2
            bottom = top + new_height
            left = 0
            right = width
        else:
            # Image is too wide — crop width
            new_width = int(height / desired_ratio)
            left = (width - new_width) // 2
            right = left + new_width
            top = 0
            bottom = height

        # Crop to 3:2 ratio
        cropped = image.crop((left, top, right, bottom))

        # Show in column width
        st.image(cropped, use_container_width=True)
    
    st.divider()
