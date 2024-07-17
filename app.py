import streamlit as st
from base64 import b64encode

def web_portfolio():
    # page configs 
    st.set_page_config(page_title = "Said's Portfolio",page_icon="⭐")
    # Set the page title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Anna Nahorna</span>👋
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

    # Get Profile Image
    with open("pic.png", "rb") as img_file:
        img = "data:image/png;base64," + b64encode(img_file.read()).decode()

    # Reading Profile
    with open("Profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()


    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    # <div class="box">
    # <img src="{img}" alt="Abhisheak Saraswat" style="width: 300px; height: 200px;">
    # </div>
    # </div>
    # """, 
    # unsafe_allow_html=True)
    # Add animation on the DP
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{
    transform: rotate(0deg);
    }}
    50% {{
    transform: rotate(5deg);
    }}
    }}
    .box img {{
    width: 300px;
    height: 200px;
    border-radius: 50%;
    animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
    <div class="box">
    <img src="{img}">
    </div>
    </div>
    """, 
    unsafe_allow_html=True)

# Set the title
    st.write(f"""
             <div class=
             "subtitle" style="text-align: center;">Data Scientist and GenAI Developer</div>""",
              unsafe_allow_html=True)
# Add Social Icons
    social_icons_data = {
    "Kaggle": ["https://www.kaggle.com/saidhem", "https://www.kaggle.com/static/images/site-logo.svg"],
    "LinkedIn": ["https://www.linkedin.com/in/said-h-1956b0161/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    "GitHub": ["https://github.com/shirdarec", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    }

    social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 25px;'></a>"
    for platform in social_icons_data
]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About Me Section
    st.subheader("About Me")

    st.markdown("""
    - I'm a musician. I play guitar, piano, drums, bass, i can also sing and play many other instruments.
    - I write songs, poems and essays.
    - I can fix mistakes in your essay or other text files.
    - In my free time i like to make power workouts and draw pictures.
    - I also make tattoos as a hobby, some graphic stuff etc.
    """)

    st.write("##")

    # Download CV button
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Your_name_cv.pdf", mime="application/pdf",)
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderfull Day!!! 🌟</div>""", unsafe_allow_html=True)


if __name__ == "__main__":
    web_portfolio()
