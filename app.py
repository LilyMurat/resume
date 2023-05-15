from pathlib import Path

import streamlit as st
from PIL import Image

# --- Path Setting ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "Picture1.png"

# --- Content Settings ---
Page_Title = "Digital Resume | Lale Mulati"
Page_Icon = "😊"
Name = "Lale Mulati"
Description = """
Junior Data Analyst, Python Developer 
"""
Email = "LaleMulati@gmail.com"
Social_Media = {
    "LinkedIn": "",
    "GitHub": "https://github.com/LilyMurat",
    "YouTube": "https://www.youtube.com/channel/UCts45yKmLXu2w_wt62ilxYg"
}
Projects = {
    "📈 Google Data Analytics _ Cyclistics Analytics Project": "",
    "💻 Data Science _ Breast Cancer Predicting Project": "",
    "🤖 Machine Learning _ Customer Service ChatBot Project": ""
}

# --- specify the content ---
st.set_page_config(page_title=Page_Title, page_icon=Page_Icon)

# st.title("Hello World!")

# --- load css, PDF, & profile picture

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- image section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label=" 📥	Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", Email)

# --- social links ---
st.write("#")
cols = st.columns(len(Social_Media))
for index, (platform, link) in enumerate(Social_Media.items()):
    cols[index].write(f"[{platform}]({link})")

# --- experience ---
st.write()
st.subheader("Experience & Qualifications")
st.write(
    """
- 4 years experience of computer programming and analyst
- Strong hands on project experience and knowledge of Data Analyst with Python and R
- Good understanding of statistical and Machine Learning problems 
- Excellent data visualization experience with Tableau and PowerBi
    """
)

# --- skills ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- Programming: Python, R, HTML, CSS, SQL
- Data Visualization: Tableau, PowerBi, MS Excel, Google Spreadsheet
- Modeling: Machine learning & Data Science algorithms for classification and regression problems
- Databases: Postgres, MongoDB, MySQL
    """
)

# --- work history ---
st.write("#")
st.subheader("Work History")

# --- job 1 ---
st.write("Store Associate | Fruiteao")
st.write("May/2017 - Present")
st.write(
    """
  At Fruiteao, my main job is to help customers, 
  whether it be making bubble tea, ringing up & bagging their in-store purchases, 
  or taking their orders via online, phone, or in-person, and keeping the store stocked and tidy. 
  I will sometimes work in the back, making tapioca pearls for the bubble tea. 
  I have also used my artistic abilities to make in-store promotional images, 
  and my artwork has been on the stores official Instagram page.  
    """
)

# --- Projects Experience ---
st.write("#")
st.subheader("Project Experience")
for project, link in Projects.items():
    st.write(f"[{project}]({link})")
