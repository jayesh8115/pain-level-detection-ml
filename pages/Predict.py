import streamlit as st
import numpy as np
import pandas as pd
from ml.predict import predict_pain
from database.crud import save_prediction, get_all_patients

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Pain Level Detector",
    page_icon="🩺",
    layout="centered"
)

# ── Custom Styling ──────────────────────────────────────────
st.markdown("""
<style>
.main {

    background-color: #5cf261;
}
h1, h2, h3 {
    text-align: center;
}
.stButton>button {
    background-color: #1D9E75;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}
.stSlider label {
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ── Helper ─────────────────────────────────────────────────
def get_pain_info(label):
    return {
        "Low":    {"emoji": "🟢", "color": "#1D9E75", "desc": "Pain scale 1–3 · Mild discomfort"},
        "Medium": {"emoji": "🟡", "color": "#EF9F27", "desc": "Pain scale 4–6 · Moderate pain"},
        "High":   {"emoji": "🔴", "color": "#E24B4A", "desc": "Pain scale 7–8 · Severe pain"},
    }.get(label, {})

# ── Header ─────────────────────────────────────────────────
st.title("🩺 Pain Level Detector")
st.markdown("AI-powered prediction using **biosensor data**")
st.divider()


# --------------------------------------------------------
# Select Patient
# --------------------------------------------------------

st.subheader("👨‍⚕️ Select Patient")

patients = get_all_patients()

if len(patients) == 0:
    st.warning("No patients found. Please register a patient first.")
    st.stop()

patient_options = {
    f"{patient['patient_id']} - {patient['name']}": patient["patient_id"]
    for patient in patients
}

selected_patient = st.selectbox(
    "Select Patient",
    list(patient_options.keys())
)

patient_id = patient_options[selected_patient]


# ── Input Section ──────────────────────────────────────────
st.subheader(" Physiological Signals")

col1, col2 = st.columns(2)

with col1:
    hr   = st.slider("Heart Rate (bpm)", 50.0, 110.0, 79.0, 0.1)
    bvp  = st.slider("Blood Volume Pulse", 40.0, 130.0, 87.0, 0.1)
    eda  = st.slider("EDA (µS)", 0.05, 9.86, 2.89, 0.01)
    temp = st.slider("Temperature (°C)", 30.25, 38.0, 34.51, 0.01)

with col2:

    st.markdown("### 🏃 Accelerometer (Advanced)")

    with st.expander("Show Accelerometer Values"):

        st.caption(
            "These values are collected from wearable sensors "
            "and are used by the Machine Learning model."
        )

        acc_x = st.slider(
            "Accelerometer X",
            min_value=-1.25,
            max_value=1.14,
            value=0.00,
            step=0.01
        )

        acc_y = st.slider(
            "Accelerometer Y",
            min_value=-1.03,
            max_value=1.17,
            value=0.00,
            step=0.01
        )

        acc_z = st.slider(
            "Accelerometer Z",
            min_value=-1.21,
            max_value=1.10,
            value=0.01,
            step=0.01
        )

st.divider()

# ── Feature Engineering ────────────────────────────────────

# Calculate Accelerometer Magnitude
acc_mag = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)

# Hidden Rolling Features
# These are generated internally for the ML model

eda_mean = eda
eda_std = 0.30

hr_mean = hr
hr_std = 2.79

# st.divider()

# ── Prediction ─────────────────────────────────────────────
if st.button("🚀 Predict Pain Level", use_container_width=True):

    # Predict Pain Level
    predicted_label, proba = predict_pain(
        acc_x,
        acc_y,
        acc_z,
        eda,
        bvp,
        hr,
        temp,
        acc_mag,
        eda_mean,
        eda_std,
        hr_mean,
        hr_std
    )

    # Save Prediction in MySQL
    save_prediction(
        patient_id,
        predicted_label,
        float(np.max(proba))
    )

    info = get_pain_info(predicted_label)

    st.success("✅ Prediction Completed & Saved Successfully")

    # -------------------------------
    # Prediction Result
    # -------------------------------
    st.markdown(f"""
    <div style="text-align:center;">
        <h2>{info['emoji']} {predicted_label} Pain</h2>
        <p style="color:{info['color']}; font-size:18px;">
            {info['desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # -------------------------------
    # Confidence Scores
    # -------------------------------
    st.subheader("📊 Prediction Confidence")

    labels = ["High", "Low", "Medium"]

    for label, probability in zip(labels, proba):

        st.progress(
            float(probability),
            text=f"{label}: {probability * 100:.2f}%"
        )

    # -------------------------------
    # Probability Table
    # -------------------------------
    probability_df = pd.DataFrame({

        "Pain Level": labels,

        "Confidence (%)": [
            round(prob * 100, 2)
            for prob in proba
        ]

    })

    st.dataframe(
        probability_df,
        use_container_width=True,
        hide_index=True
    )

    st.metric(
        "Accelerometer Magnitude",
        f"{acc_mag:.4f}"
    )

    

# ── Footer ─────────────────────────────────────────────────
st.divider()
st.caption("AI Pain Level Detection System | © 2026")





