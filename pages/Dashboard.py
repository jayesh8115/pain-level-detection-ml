import streamlit as st
import pandas as pd
import plotly.express as px
from database.crud import (
    get_total_patients,
    get_total_males,
    get_total_females,
    get_total_others
)

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------------
# Login Check
# -------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("Please login first.")
    st.stop()

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("Dashboard")

st.write(
    f"Welcome **{st.session_state.username}**"
)

st.divider()

# -------------------------------------------------------
# Sample Statistics
# -------------------------------------------------------

total_patients = get_total_patients()

male = get_total_males()

female = get_total_females()

other = get_total_others()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Total Patients",
        total_patients
    )

with c2:
    st.metric(
        "👨 Male Patients",
        male
    )

with c3:
    st.metric(
        "👩 Female Patients",
        female
    )

with c4:
    st.metric(
        "🧑 Other Patients",
        other
    )

st.divider()

# -------------------------------------------------------
# Pain Distribution
# -------------------------------------------------------

st.subheader("Pain Level Distribution")

pain_df = pd.DataFrame({

    "Pain Level":[
        "Low",
        "Medium",
        "High"
    ],

    "Patients":[
        110,
        82,
        48
    ]

})

fig = px.pie(

    pain_df,

    names="Pain Level",

    values="Patients",

    hole=0.45

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Weekly Prediction Trend
# -------------------------------------------------------

st.subheader("Weekly Prediction Trend")

weekly = pd.DataFrame({

    "Day":[
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Predictions":[
        14,
        18,
        15,
        21,
        24,
        19,
        17
    ]

})

fig2 = px.line(

    weekly,

    x="Day",

    y="Predictions",

    markers=True

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# -------------------------------------------------------
# Recent Predictions
# -------------------------------------------------------

st.subheader("Recent Predictions")

history = pd.DataFrame({

    "Patient ID":[
        "P001",
        "P002",
        "P003",
        "P004",
        "P005"
    ],

    "Pain":[
        "Low",
        "Medium",
        "High",
        "Low",
        "Medium"
    ],

    "Confidence":[
        "97%",
        "94%",
        "99%",
        "95%",
        "96%"
    ]

})

st.dataframe(
    history,
    use_container_width=True
)

# -------------------------------------------------------
# Quick Actions
# -------------------------------------------------------

st.divider()

st.subheader("Quick Actions")

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("➕ Add Patient"):

        st.switch_page("pages/Patient.py")

with c2:

    if st.button("🩺 Predict Pain"):

        st.switch_page("pages/Predict.py")

with c3:

    if st.button("📄 View Reports"):

        st.switch_page("pages/Reports.py")

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.title("Navigation")

st.sidebar.success(
    "Dashboard"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.switch_page("pages/Login.py")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.divider()

st.caption(
    "Pain Level Detection System | Dashboard"
)