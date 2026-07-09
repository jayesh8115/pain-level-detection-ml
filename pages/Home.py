import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Pain Level Detection System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#f7f9fc;
}

.title{
    text-align:center;
    color:#0E4D92;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:20px;
}

.card{
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🩺 Navigation")

st.sidebar.success("Select a page")

st.sidebar.info("""
Pain Level Detection System

Version : 1.0

Developed using

• Streamlit

• FastAPI

• Random Forest

• MySQL
""")

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<h1 class='title'>AI Pain Level Detection System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Predict Pain Level using Physiological Sensor Data</p>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Welcome Section
# -----------------------------
col1, col2 = st.columns([2,1])

with col1:

    st.subheader(" System Overview")

    with open("videos/13808077-hd_1920_1080_25fps.mp4", "rb") as video:
        st.video(video.read())

with col2:

    st.info("""
### Machine Learning Model

Model Used

Random Forest Classifier

Accuracy

96.5%

Features

✔ Heart Rate

✔ EDA

✔ Temperature

✔ Blood Volume Pulse

✔ Accelerometer
""")

st.divider()

# -----------------------------
# Features
# -----------------------------
st.subheader("System Modules")

c1,c2,c3 = st.columns(3)

with c1:

    st.success("""
👤 Patient Management

• Register Patient

• Search Patient

• Update Details

• Delete Record
""")

with c2:

    st.warning("""
🤖 AI Prediction

• Predict Pain

• Upload CSV

• Confidence Score

• Explain Prediction
""")

with c3:

    st.info("""
📊 Analytics

• Dashboard

• History

• Reports

• Statistics
""")

st.divider()

# -----------------------------
# Pain Scale
# -----------------------------
st.subheader("Pain Severity Levels")

pain_table = {
    "Pain Level":["Low","Medium","High"],
    "Pain Score":["1-3","4-6","7-10"],
    "Severity":["Mild","Moderate","Severe"]
}

st.table(pain_table)

st.divider()

# # -----------------------------
# # About
# # -----------------------------
# with st.expander("About this Project"):

#     st.write("""

# This project is developed for real-world healthcare applications.

# Technologies Used

# • Python

# • Streamlit

# • FastAPI

# • Scikit-learn

# • MySQL

# • SHAP Explainability

# • Plotly

# • ReportLab

# • Docker

# """)

# -----------------------------
# Footer
# -----------------------------
st.markdown(
"""
<div class="footer">

Developed by Jayesh Sawant

AI Pain Level Detection System

© 2026

</div>
""",
unsafe_allow_html=True
)