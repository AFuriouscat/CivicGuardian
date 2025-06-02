# pages/dashboard.py
import streamlit as st
import numpy as np
import pandas as pd

from components import footer
from PIL import Image


def show():
    st.markdown("<div style='padding-left: 5rem; padding-right: 5rem;'>", unsafe_allow_html=True)

    # Header full width
    # st.header("📊 Justice Dashboard")
    st.markdown(
        """
        <div style="margin: 1rem 0; text-align: center;">
        <div style="background-color: #1169c0; color: white; padding: 2rem; border-radius: 1rem; width: 30%; margin: auto;">
            <span style="font-size: 2rem; font-weight: bold;">
            Justice Dashboard
            </span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Columns for custom width control
    col1, col2 = st.columns([2, 1])  # 2:1 width ratio

    with col1:
        # Generate synthetic crime index data based on Numbeo's 2023 data
        np.random.seed(42)  # For reproducibility
        cities = {
            "Manila": 65.4,
            "Quezon City": 63.2,
            "Cebu": 51.9,
            "Iloilo": 41.5,
            "Makati": 38.8,
            "Davao": 27.6
        }

        data = {}
        for city, base_index in cities.items():
            # Simulate slight fluctuations around the base index
            fluctuations = np.random.normal(loc=0, scale=1.5, size=50)
            city_data = np.clip(base_index + np.cumsum(fluctuations), 0, 100)
            data[city] = city_data

        df = pd.DataFrame(data)

        # Display the line chart
        st.line_chart(df)

        # Descriptive text
        st.markdown("""
        **Crime Index Trends (2023):**  
        This line chart illustrates the simulated monthly crime index trends for selected Philippine cities in 2023. The data is based on Numbeo's Crime Index, which reflects residents' perceptions of crime levels in their cities. Higher values indicate higher perceived crime rates. While Manila and Quezon City show higher indices, cities like Davao and Makati reflect lower crime perceptions. These trends provide insights into public safety sentiments across different urban areas.
        """)
    with col2:
        # Load the image
        image = Image.open("assets/dashboard-page.jpg")

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

    st.markdown("</div>", unsafe_allow_html=True)
