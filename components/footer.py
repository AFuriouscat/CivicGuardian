# components/footer.py
import streamlit as st

def show():
    st.markdown("""
    <div class='header-footer' style='margin-top: 3rem;'>
        <div style='display:flex;justify-content:space-between;flex-wrap:wrap;'>
            <div>
            </div>
            <div>
                <h4>Stay Connected</h4>
                <a href='https://facebook.com' target='_blank' style='color:white;display:block;'>Facebook</a>
                <a href='https://twitter.com' target='_blank' style='color:white;display:block;'>X</a>
                <a href='https://youtube.com' target='_blank' style='color:white;display:block;'>▶YouTube</a>
                <a href='https://instagram.com' target='_blank' style='color:white;display:block;'>Instagram</a>
            </div>
            <div>
                <h4>Links</h4>
                <a href='#' style='color:white;display:block;'>About Us & Legal Info</a>
                <a href='#' style='color:white;display:block;'>Contact Us</a>
                <a href='#' style='color:white;display:block;'>Privacy Policy</a>
                <a href='#' style='color:white;display:block;'>Terms of Use</a>
                <a href='#' style='color:white;display:block;'>Equal Opportunity</a>
            </div>
            <div style='text-align:right;'>
                <h4>Team Hack Pack 2025</h4>
                <a href='#' style='color:white;display:block;'>Arcos, Isiah Gabriel</a>
                <a href='#' style='color:white;display:block;'>Mendoza, Alron David</a>
                <a href='#' style='color:white;display:block;'>Nogales, Yhasmen</a>
                <a href='#' style='color:white;display:block;'>Yabut, Natasha Julia</a>
            </div>
            <div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
