import streamlit as st
import math
from PIL import Image

def show():
    # st.title("About CivicGuardian")

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

    # --- Vision & Mission Section (Justified & Centered) ---
    st.markdown(
        """
        <style>
        .indented-paragraph {
            text-indent: 2em;
            padding-left: 1em;
            margin-bottom: 1em;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Mission & Vision section ---
    st.markdown("<h3 style='text-align:center;'>Mission and Vision</h3>", unsafe_allow_html=True)

    # 👇 You must define col2 before using it!
    col1, col2, col3 = st.columns([3, 6, 3])

    with col2:
        st.markdown(
            """
            <div style='text-align:justify; font-size:20px;'>
                <strong>CivicGuardian</strong><br><br>
                <p class='indented-paragraph'>“One platform to report, understand and monitor justice in your city.”</p>
                <p class='indented-paragraph'>A high‐fidelity web app combining anonymous reporting + AI rights assistant + legal case transparency + institutional accountability dashboard.</p>
                <p class='indented-paragraph'>Citizens can report abuse, get legal assistance, and track how institutions respond—all powered by AI and wrapped in a clean, interactive UI.</p>
                <strong>This website aims to be a solution to the following SDG:</strong><br><br>
                <p class='indented-paragraph'><strong>SDG 11</strong> focuses on making cities inclusive, safe, resilient, and sustainable, emphasizing urban planning and management for better living conditions.</p>
                <p class='indented-paragraph'><strong>SDG 16</strong> prioritizes peace, justice, and strong institutions, aiming to promote peaceful and inclusive societies and ensure access to justice for all.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # --- Core Features Section (Justified & Centered) ---
    st.markdown("<h3 style='text-align:center;'>Core Features</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([3, 6, 3])
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
                    &emsp;• Track public cases (e.g. from public legal datasets or simulated JSON)<br>
                    &emsp;• Gemini‐generated summaries: “Case backlog in Quezon City is growing. Avg. resolution time: 287 days.”</li><br>
                <li><strong>Institution Scorecard</strong><br>
                    &emsp;• Transparency scores for courts, barangays, LGUs<br>
                    &emsp;• User feedback/ratings from resolved cases<br>
                    &emsp;• AI detects patterns of delay, corruption risks (mocked if no real data)</li><br>
            </ul>
            <br>
            <strong>Coming Soon (Optional Features):</strong><br>
            &emsp;• PWA offline mode<br>
            &emsp;• Email notifications to NGOs/Government units<br>
            &emsp;• Public API for open‐data advocacy groups<br>
            &emsp;• Reputation system for verified submissions
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("---")

    # --- Meet the Team Section (1 Row, 4 Columns) ---
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
            "img_path": "assets/alron.jpg"
        },
        {
            "name": "Yhasmen Nogales",
            "email": "sample@example.com",
            "role": "Project Manager",
            "socials": {
                "LinkedIn": "https://www.linkedin.com/in/sample-member/"
            },
            "img_path": "assets/placeholder.jpg"
        }
    ]

    st.markdown(
        """
        <style>
        .circle-img {
            width: 100%;
            aspect-ratio: 1 / 1;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #ccc;
            margin-bottom: 10px;
        }
        .member-box {
            text-align: center;
            padding: 1rem;
        }
        .member-box h4,
        .member-box p,
        .member-box a {
            margin: 0.3rem 0;
            text-align: center !important;
            display: block;
        }
        .social-links {
            margin-top: 0.5rem;
        }
        .social-links a {
            margin: 0 0.3rem;
            color: #003366;
            font-weight: bold;
            text-decoration: none;
            font-size: 14px;
        }
        .social-links a:hover {
            text-decoration: underline;
        }
        </style>

        """,
        unsafe_allow_html=True,
    )

    cols_per_row = 4
    rows = math.ceil(len(members) / cols_per_row)

    for i in range(rows):
        row_members = members[i*cols_per_row:(i+1)*cols_per_row]
        cols = st.columns(len(row_members))
        for col, m in zip(cols, row_members):
            with col:
                st.markdown("<div class='member-box'>", unsafe_allow_html=True)
                st.markdown(f"<img src='{m['img_path']}' class='circle-img' />", unsafe_allow_html=True)
                st.markdown(f"<h4>{m['name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p><em>{m['role']}</em></p>", unsafe_allow_html=True)
                st.markdown(f"<a href='mailto:{m['email']}'>{m['email']}</a>", unsafe_allow_html=True)
                st.markdown("<div class='social-links'>", unsafe_allow_html=True)
                for platform, link in m["socials"].items():
                    st.markdown(f"<a href='{link}' target='_blank'>{platform}</a>", unsafe_allow_html=True)
                st.markdown("</div></div>", unsafe_allow_html=True)
