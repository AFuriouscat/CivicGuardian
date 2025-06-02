# main.py
import streamlit as st
from components import login, footer, profile
from custom_pages import report_center, rights_assistant, dashboard, scorecard, admin_panel, about
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="CivicGuardian", layout="wide")

# — Hide the default Streamlit sidebar —
st.markdown(
    """
    <style>
      [data-testid="stSidebar"] { display: none !important; }
      [data-testid="collapsedControl"] { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Session State Setup
# -----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.is_admin = False
    st.session_state.username = ""
    st.session_state.active_tab = "home"  # default tab

# --- Full-width CSS for header/footer padding ---
st.markdown(
    """
    <style>
      :root {
        --header-footer-padding-left: 4rem;
        --header-footer-padding-right: 4rem;
      }
      .css-1d391kg {
        max-width: 100vw !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin: 0 !important;
      }
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
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header (logo + user indicator)
# -----------------------------
st.markdown(
    f"""
    <div class='header-footer'>
      <div style='display:flex; justify-content:space-between; flex-wrap:wrap; align-items:center; gap:1rem;'>
        <div></div>
        <div style='font-size:1.5rem; font-weight:bold;'>CivicGuardian</div>
        <div></div>
        <div></div>
        <div></div>
        <div>
          {"👤 " + st.session_state.username if st.session_state.authenticated else "👤 Guest"}
        </div>
        <div></div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Horizontal Menu (streamlit-option-menu)
# -----------------------------
menu_labels = ["HOME", "REPORT", "ASSISTANT", "DASHBOARD", "SCORECARD", "ABOUT US"]
menu_icons  = ["house", "file-earmark-text", "shield-lock", "speedometer", "bar-chart", "envelope"]

if st.session_state.is_admin:
    menu_labels.append("Admin Panel")
    menu_icons.append("tools")

# Add Profile/Login at the end
profile_label = "👤 Profile" if st.session_state.authenticated else "LOGIN"
menu_labels.append(profile_label)
menu_icons.append("person-circle")

# Reverse mapping: tab_key → menu label
tab_to_label = {
    "home":        "HOME",
    "report":      "REPORT",
    "assistant":   "ASSISTANT",
    "dashboard":   "DASHBOARD",
    "scorecard":   "SCORECARD",
    "about_us":    "ABOUT US",
    "admin":       "Admin Panel",
    "profile":     profile_label,
}

# Compute default_index from current active_tab
try:
    default_index = menu_labels.index(tab_to_label[st.session_state.active_tab])
except KeyError:
    default_index = 0

selected_menu = option_menu(
    menu_title=None,
    options=menu_labels,
    icons=menu_icons,
    orientation="horizontal",
    default_index=default_index,
)

# Map each visible label → our internal tab key
label_to_tab_key = {
    "HOME":        "home",
    "REPORT":      "report",
    "ASSISTANT":   "assistant",
    "DASHBOARD":   "dashboard",
    "SCORECARD":   "scorecard",
    "ABOUT US":    "about_us",
    "Admin Panel": "admin",
    profile_label: "profile",
}

# Whenever the user clicks one of the horizontal menu items, update active_tab
new_tab = label_to_tab_key.get(selected_menu, "home")
if new_tab != st.session_state.active_tab:
    st.session_state.active_tab = new_tab

# -----------------------------
# Page Routing
# -----------------------------
tab = st.session_state.active_tab

if tab == "home":
    # ====== Home page content embedded here ======

    # 1) Wide banner across the top
    banner_path = "assets/banner-about-page.jpeg"  # adjust path as needed
    try:
        banner_img = Image.open(banner_path)
        w, h = banner_img.size
        # Crop to a very wide ratio, e.g. 7:1
        target_ratio = 7 / 1
        if w / h > target_ratio:
            new_w = int(h * target_ratio)
            left = (w - new_w) // 2
            right = left + new_w
            top, bottom = 0, h
        else:
            new_h = int(w / target_ratio)
            top = (h - new_h) // 2
            bottom = top + new_h
            left, right = 0, w
        banner_cropped = banner_img.crop((left, top, right, bottom))
        st.image(banner_cropped, use_container_width=True)
    except Exception:
        st.warning(f"Could not load banner image at `{banner_path}`.")

    # 2) Hero Text
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

    # 3) Four-column card section
    cards = [
        {
            "title": "Report an Incident",
            "button": "Go to Report",
            "tab_key": "report",
            "image_path": "assets/report-page.jpg",
        },
        {
            "title": "AI Assistant",
            "button": "Ask Assistant",
            "tab_key": "assistant",
            "image_path": "assets/assistant-page.jpg",
        },
        {
            "title": "Justice Dashboard",
            "button": "View Dashboard",
            "tab_key": "dashboard",
            "image_path": "assets/dashboard-page.jpg",
        },
        {
            "title": "Institution Scorecard",
            "button": "View Scorecard",
            "tab_key": "scorecard",
            "image_path": "assets/scorecard-page.jpg",
        },
    ]

    st.markdown("<div style='margin: 2rem 5rem;'>", unsafe_allow_html=True)
    cols = st.columns(4, gap="large")

    for col, card in zip(cols, cards):
        with col:
            # Load & crop each card’s image to ~4:3 ratio
            try:
                img = Image.open(card["image_path"])
                w, h = img.size
                ratio = 4 / 3
                if w / h > ratio:
                    new_w = int(h * ratio)
                    left = (w - new_w) // 2
                    right = left + new_w
                    top, bottom = 0, h
                else:
                    new_h = int(w / ratio)
                    top = (h - new_h) // 2
                    bottom = top + new_h
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

            # When clicked, set active_tab and rerun → matches the horizontal tab
            if st.button(card["button"], key=card["tab_key"]):
                st.session_state.active_tab = card["tab_key"]
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

elif tab == "report":
    report_center.show()

elif tab == "assistant":
    rights_assistant.show()

elif tab == "dashboard":
    dashboard.show()

elif tab == "scorecard":
    scorecard.show()

elif tab == "about_us":
    about.show()
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
