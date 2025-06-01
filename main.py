import streamlit as st
from components import login, footer, profile
from pages import dashboard, rights_assistant, report_center, scorecard, about
# We'll create new pages for about and contact later or just add st.markdown for now

st.set_page_config(page_title="CivicGuardian", layout="wide")

# Session State Setup
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.is_admin = False
    st.session_state.username = ""
    st.session_state.active_tab = "about"  # default tab

# --- Full width container override CSS with adjustable padding ---
st.markdown("""
<style>
:root {
    --header-footer-padding-left: 4rem;
    --header-footer-padding-right: 4rem;
}

/* Override Streamlit default container width and padding */
.css-1d391kg {
    max-width: 100vw !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    margin-left: 0rem !important;
    margin-right: 0rem !important;
}

/* Header and Footer with dynamic paddings */
.header-footer {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    background-color: #003366;
    padding-left: var(--header-footer-padding-left);
    padding-right: var(--header-footer-padding-right);
    padding-top: 1rem;
    padding-bottom: 1rem;
    color: white;
    box-sizing: border-box;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(f"""
    <div class='header-footer'>
        <div style='display:flex;justify-content:space-between;align-items:center;'>
            <div style='font-size:1.5rem;font-weight:bold;'>CivicGuardian</div>
            <div>
                {"👤 " + st.session_state.username if st.session_state.authenticated else "🔐 Guest"}
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------
# Tab Buttons (No Page Reload)
# -----------------------------
num_tabs = 6 + int(st.session_state.is_admin) + 1 + 3
button_width = 120  # px width per button
widths = [button_width] * num_tabs
tab_cols = st.columns(widths, gap="small")

tab_labels = ["ABOUT", "REPORT", "ASSISTANT", "DASHBOARD", "SCORECARD", "CONTACT US"]
if st.session_state.is_admin:
    tab_labels.append("Admin Panel")

for i, label in enumerate(tab_labels):
    with tab_cols[i]:
        if st.button(label, key=f"tab_{label}"):
            mapping = {
                "DASHBOARD": "dashboard",
                "REPORT": "report",
                "ASSISTANT": "rights",
                "SCORECARD": "scorecard",
                "ABOUT": "about",
                "CONTACT US": "contact",
                "Admin Panel": "admin",
            }
            st.session_state.active_tab = mapping[label]

# Profile/Login button
with tab_cols[-1]:
    profile_label = "👤 Profile" if st.session_state.authenticated else "🔐 LOGIN"
    if st.button(profile_label, key="tab_profile"):
        st.session_state.active_tab = "profile"

# -----------------------------
# Page Routing
# -----------------------------
tab = st.session_state.active_tab
if tab == "dashboard":
    dashboard.show()
elif tab == "report":
    report_center.show()
elif tab == "rights" or tab == "assistant":
    rights_assistant.show()
elif tab == "scorecard":
    scorecard.show()
elif tab == "about":
    about.show()
elif tab == "contact":
    st.markdown("<h1>Contact Us</h1><p>Put your Contact page content here.</p>", unsafe_allow_html=True)
elif tab == "admin" and st.session_state.is_admin:
    admin_panel.show()
elif tab == "profile":
    if not st.session_state.authenticated:
        login.show_login()
    else:
        profile.show()

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
    <div class='header-footer' style='margin-top: 3rem;'>
        <div style='display:flex;justify-content:space-between;flex-wrap:wrap;'>
            <div>
            </div>
            <div>
                <h4>Stay Connected</h4>
                <a href='https://facebook.com' target='_blank' style='margin-right:10px;'>📘</a>
                <a href='https://twitter.com' target='_blank' style='margin-right:10px;'>🐦</a>
                <a href='https://youtube.com' target='_blank' style='margin-right:10px;'>▶️</a>
                <a href='https://instagram.com' target='_blank'>📸</a>
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
                <p>By: Hack Pack 2025</p>
            </div>
            <div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
