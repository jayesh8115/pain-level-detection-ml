import streamlit as st
import pandas as pd

from database.crud import get_prediction_history

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(

    page_title="Prediction History",

    page_icon="📜",

    layout="wide"

)

# --------------------------------------------------------
# Title
# --------------------------------------------------------

st.title("📜 Prediction History")

st.write(
    "View all previous pain predictions."
)

st.divider()

# --------------------------------------------------------
# Load History
# --------------------------------------------------------

history = get_prediction_history()

# --------------------------------------------------------
# Display History
# --------------------------------------------------------

if len(history) == 0:

    st.info("No Prediction History Available.")

else:

    df = pd.DataFrame(history)

    df = df.rename(columns={

        "prediction_id":"Prediction ID",

        "patient_id":"Patient ID",

        "name":"Patient Name",

        "gender":"Gender",

        "age":"Age",

        "pain_level":"Pain Level",

        "confidence":"Confidence",

        "prediction_date":"Prediction Date"

    })

    df["Confidence"] = (

        df["Confidence"]*100

    ).round(2)

    df["Confidence"] = (

        df["Confidence"]

        .astype(str)

        + "%"

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )

# --------------------------------------------------------
# Statistics
# --------------------------------------------------------

st.divider()

st.subheader("Prediction Statistics")

total_predictions = len(history)

high = len(

    [

        x

        for x in history

        if x["pain_level"]=="High"

    ]

)

medium = len(

    [

        x

        for x in history

        if x["pain_level"]=="Medium"

    ]

)

low = len(

    [

        x

        for x in history

        if x["pain_level"]=="Low"

    ]

)

c1,c2,c3,c4 = st.columns(4)

c1.metric(

    "Total",

    total_predictions

)

c2.metric(

    "High",

    high

)

c3.metric(

    "Medium",

    medium

)

c4.metric(

    "Low",

    low

)


st.divider()

# --------------------------------------------------------
# Navigation
# --------------------------------------------------------

c1,c2,c3 = st.columns(3)

with c1:

    if st.button("🏠 Home"):

        st.switch_page("pages/Home.py")

with c2:

    if st.button("📊 Dashboard"):

        st.switch_page("app/Dashboard.py")

with c3:

    if st.button("🩺 Predict"):

        st.switch_page("app/Predict.py")