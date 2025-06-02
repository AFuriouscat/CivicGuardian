import streamlit as st

from PIL import Image
from components import footer

def show():
    st.header("📝 Report Center")

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.subheader("Submit an Anonymous Report")
        st.text_input("Location", key="report_location")
        st.text_area("Describe the incident", key="report_description")
        st.file_uploader("Upload photo (optional)", type=["jpg", "png"], key="report_file")

        if st.button("Submit Report", key="submit_report_btn"):
            st.success("Report submitted anonymously. Gemini classifying...")
            st.info("Gemini: This appears to be a public harassment case. You may contact XYZ legal org.")

    with right_col:
        # Load the image
        image = Image.open("assets/report-page.jpg")

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

