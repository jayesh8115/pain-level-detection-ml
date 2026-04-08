import streamlit as st
import numpy as np
import pandas as pd
import pickle

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

# ── Load Models ─────────────────────────────────────────────
@st.cache_resource
def load_models():
    with open("rf_model.pkl", "rb") as f:
        rf_model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return rf_model, scaler

rf_model, scaler = load_models()

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

# ── Input Section ──────────────────────────────────────────
st.subheader("📊 Physiological Signals")

col1, col2 = st.columns(2)

with col1:
    hr   = st.slider("Heart Rate (bpm)", 50.0, 110.0, 79.0, 0.1)
    bvp  = st.slider("Blood Volume Pulse", 40.0, 130.0, 87.0, 0.1)
    eda  = st.slider("EDA (µS)", 0.05, 9.86, 2.89, 0.01)
    temp = st.slider("Temperature (°C)", 30.25, 38.0, 34.51, 0.01)

with col2:
    acc_x = st.slider("Accelerometer X", -1.25, 1.14, 0.0, 0.01)
    acc_y = st.slider("Accelerometer Y", -1.03, 1.17, 0.0, 0.01)
    acc_z = st.slider("Accelerometer Z", -1.21, 1.10, 0.01, 0.01)

st.divider()

# ── Feature Engineering ────────────────────────────────────
acc_mag = np.sqrt(acc_x**2 + acc_y**2 + acc_z**2)

st.subheader("📈 Rolling Features")

col3, col4 = st.columns(2)

with col3:
    eda_mean = st.number_input("EDA Mean", value=round(eda, 4))
    eda_std  = st.number_input("EDA Std", value=0.30)

with col4:
    hr_mean = st.number_input("HR Mean", value=round(hr, 3))
    hr_std  = st.number_input("HR Std", value=2.79)

st.divider()

# ── Prediction ─────────────────────────────────────────────
if st.button("🚀 Predict Pain Level", use_container_width=True):

    features = np.array([[acc_x, acc_y, acc_z, eda, bvp, hr, temp,
                          acc_mag, eda_mean, eda_std, hr_mean, hr_std]])

    features_scaled = scaler.transform(features)
    pred = rf_model.predict(features_scaled)[0]
    proba = rf_model.predict_proba(features_scaled)[0]

    label_map = {0: "High", 1: "Low", 2: "Medium"}
    predicted_label = label_map[pred]

    info = get_pain_info(predicted_label)

    st.success("Prediction Complete ✅")

    # Result Display
    st.markdown(f"""
    <div style="text-align:center;">
        <h2>{info['emoji']} {predicted_label} Pain</h2>
        <p style="color:{info['color']}; font-size:18px;">
        {info['desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Probability Bar
    st.subheader("📊 Prediction Confidence")

    labels = ["High", "Low", "Medium"]
    for i, lbl in enumerate(labels):
        st.progress(float(proba[i]), text=f"{lbl}: {proba[i]*100:.1f}%")

    # Data Table
    prob_df = pd.DataFrame({
        "Pain Level": labels,
        "Probability (%)": [f"{p*100:.1f}" for p in proba]
    })
    st.dataframe(prob_df, use_container_width=True)

    st.metric("Accelerometer Magnitude", f"{acc_mag:.4f}")

    

# ── Footer ─────────────────────────────────────────────────
st.divider()
st.caption("Model: Random Forest | Accuracy: 96.5% | Dataset: 96,000 samples")