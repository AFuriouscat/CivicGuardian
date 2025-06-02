import streamlit as st

st.set_page_config(page_title="CivicGuardian", layout="wide")

# Removes the Side Tab
st.markdown("""
    <style>
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    /* Hide sidebar toggle button (hamburger icon) */
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Other Imports
from components import login, footer, profile
from custom_pages import dashboard, rights_assistant, report_center, scorecard, about
from streamlit_option_menu import option_menu

# We'll create new pages for about and contact later or just add st.markdown for now

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
        <div style='display:flex;justify-content:space-between;flex-wrap:wrap;align-items:center;gap:1rem;'>
            <div>
            </div>
            <div style='font-size:1.5rem;font-weight:bold;'>CivicGuardian</div>
            <div>
            </div>
            <div>
            </div>
            <div>
            </div>
            <div>
                {"👤 " + st.session_state.username if st.session_state.authenticated else "🔐 Guest"}
            </div>
            <div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------
# Horizontal
# -----------------------------

from streamlit_option_menu import option_menu

# Build menu items based on user state
menu_labels = ["ABOUT", "REPORT", "ASSISTANT", "DASHBOARD", "SCORECARD", "CONTACT US"]
menu_icons = ["info-circle", "file-earmark-text", "shield-lock", "speedometer", "bar-chart", "envelope"]

if st.session_state.is_admin:
    menu_labels.append("Admin Panel")
    menu_icons.append("tools")

# Add login/profile button at end
profile_label = "👤 Profile" if st.session_state.authenticated else "🔐 LOGIN"
menu_labels.append(profile_label)
menu_icons.append("person-circle")

# Show horizontal menu
selected_menu = option_menu(
    menu_title=None,
    options=menu_labels,
    icons=menu_icons,
    orientation="horizontal",
    default_index=0
)

# Map labels to internal tab keys
label_to_tab_key = {
    "DASHBOARD": "dashboard",
    "REPORT": "report",
    "ASSISTANT": "rights",
    "SCORECARD": "scorecard",
    "ABOUT": "about",
    "CONTACT US": "contact",
    "Admin Panel": "admin",
    "👤 Profile": "profile",
    "🔐 LOGIN": "profile",
}

# Update active tab in session state
st.session_state.active_tab = label_to_tab_key.get(selected_menu, "about")

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
footer.show()




