import streamlit as st
import math
from PIL import Image

def show():
    # --- Banner Image ---
    banner_path = "assets/banner-about-page.jpeg"
    try:
        banner_img = Image.open(banner_path)
        w, h = banner_img.size
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

    # --- Section: About CivicGuardian ---
    st.markdown(
        """
        <div style="margin: 1rem 0; text-align: center;">
        <div style="background-color: #1169c0; color: white; padding: 2rem; border-radius: 1rem; width: 30%; margin: auto;">
            <span style="font-size: 2rem; font-weight: bold;">
            About CivicGuardian
            </span>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # --- Mission & Vision section ---
    st.markdown("<h3 style='text-align:center;'>Mission and Vision</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 6, 3])
    with col2:
        st.markdown(
            """
            <div style='text-align:justify; font-size:20px;'>
                <strong>CivicGuardian</strong><br><br>
                <p style='text-indent:2em;'>“One platform to report, understand and monitor justice in your city.”</p>
                <p style='text-indent:2em;'>A high‐fidelity web app combining anonymous reporting + AI rights assistant + legal case transparency + institutional accountability dashboard.</p>
                <p style='text-indent:2em;'>Citizens can report abuse, get legal assistance, and track how institutions respond—all powered by AI and wrapped in a clean, interactive UI.</p>
                <strong>This website aims to be a solution to the following SDG:</strong><br><br>
                <p style='text-indent:2em;'><strong>SDG 11</strong> focuses on making cities inclusive, safe, resilient, and sustainable.</p>
                <p style='text-indent:2em;'><strong>SDG 16</strong> prioritizes peace, justice, and strong institutions.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # --- Core Features Section ---
    st.markdown("<h3 style='text-align:center;'>Core Features</h3>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div style='text-align:justify; font-size:18px;'>
            <ul style='list-style-type:none; padding-left:0;'>
                <li><strong>Report Center</strong><br>
                    &emsp;• Anonymous or logged‐in incident report<br>
                    &emsp;• Text + photo upload<br>
                    &emsp;• Gemini 2.0 classifies the type of violation<br>
                    &emsp;• Auto‐suggests relevant law & next step</li><br>
                <li><strong>Rights Assistant (Gemini AI Chat)</strong><br>
                    &emsp;• Ask: “What are my rights if I was harassed in public?”<br>
                    &emsp;• Gemini explains laws in plain language<br>
                    &emsp;• Available in Filipino + English</li><br>
                <li><strong>Justice Dashboard</strong><br>
                    &emsp;• Interactive charts: number of reports per region, type, status<br>
                    &emsp;• Track public cases<br>
                    &emsp;• Gemini‐generated summaries</li><br>
                <li><strong>Institution Scorecard</strong><br>
                    &emsp;• Transparency scores for courts, barangays, LGUs<br>
                    &emsp;• User feedback/ratings<br>
                    &emsp;• AI detects delay/corruption risks</li><br>
            </ul>
            <br>
            <strong>Coming Soon:</strong><br>
            &emsp;• PWA offline mode<br>
            &emsp;• Email alerts to NGOs/LGUs<br>
            &emsp;• Public API for advocacy groups<br>
            &emsp;• Reputation system for verified submissions
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("---")

    # --- Meet the Team Section ---
    st.markdown("<h3 style='text-align:center;'>Meet the Team</h3>", unsafe_allow_html=True)

    members = [
        {
            "name": "Isiah Gabriel A. Arcos",
            "email": "isiahgabrielarcos04@gmail.com",
            "role": "Software Developer",
            "socials": {
                "Facebook": "https://www.facebook.com/isiahgabriel.arcos",
                "LinkedIn": "https://www.linkedin.com/in/isiah-gabriel-arcos-416148338/",
                "Instagram": "https://www.instagram.com/justafuriouscat/"
            },
            "img_path": "assets/Arcos.jpg"
        },
        {
            "name": "Natasha Julia S. Yabut",
            "email": "ailujyabut@gmail.com",
            "role": "UI/UX Designer",
            "socials": {
                "Facebook": "https://www.facebook.com/n.julia.s.yabut/",
                "LinkedIn": "https://www.linkedin.com/in/n-julia-s-yabut/"
            },
            "img_path": "assets/Yabut.jpg"
        },
        {
            "name": "Alron David V. Mendoza",
            "email": "alrondavidmendoza@gmail.com",
            "role": "Marketing Specialist",
            "socials": {
                "Facebook": "https://www.facebook.com/alrownie",
                "LinkedIn": "https://www.linkedin.com/in/alron-david-mendoza-427220297/",
                "Instagram": "https://www.instagram.com/alrownie/"
            },
            "img_path": "assets/Mendoza.jpg"
        },
        {
            "name": "Yhasmen Nogales",
            "email": "yhasmennogales04@gmail.com",
            "role": "Project Manager",
            "socials": {
                "Facebook": "https://www.facebook.com/yhasmen.nogales.2024",
                "LinkedIn": "https://www.linkedin.com/in/yhasmen-nogales/"
            },
            "img_path": "assets/Nogales.jpg"
        }
    ]

    cols_per_row = 4
    rows = math.ceil(len(members) / cols_per_row)

    for i in range(rows):
        row_members = members[i * cols_per_row:(i + 1) * cols_per_row]
        cols = st.columns(len(row_members))
        for col, m in zip(cols, row_members):
            with col:
                try:
                    img = Image.open(m["img_path"])
                    w, h = img.size
                    desired_ratio = 1  # 1:1 aspect ratio
                    if h / w > desired_ratio:
                        new_height = int(w * desired_ratio)
                        top = (h - new_height) // 2
                        bottom = top + new_height
                        left = 0
                        right = w
                    else:
                        new_width = int(h / desired_ratio)
                        left = (w - new_width) // 2
                        right = left + new_width
                        top = 0
                        bottom = h
                    cropped = img.crop((left, top, right, bottom))
                    st.image(cropped, use_container_width=True)
                except:
                    st.warning(f"Image not found: {m['img_path']}")
                st.markdown(f"<h2 style='font-size:1.75rem; text-align:center;'>{m['name']}</h2>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align:center; font-weight:normal;'>{m['role']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h5 style='text-align:center;'><a href='mailto:{m['email']}' style='text-decoration:none;'>Email</a></h5>", unsafe_allow_html=True)

                for platform, url in m["socials"].items():
                    st.markdown(f"<h5 style='text-align:center;'><a href='{url}' target='_blank' style='text-decoration:none;'>{platform}</a></h5>", unsafe_allow_html=True)