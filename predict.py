"""
predict.py

Loads the trained Random Forest model
and predicts pain level.
"""

import pickle
import numpy as np
import os

# ============================================
# Current Folder
# ============================================

BASE_DIR = os.path.dirname(__file__)

# ============================================
# Load Model
# ============================================

model_path = os.path.join(BASE_DIR, "rf_model.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

with open(scaler_path, "rb") as file:
    scaler = pickle.load(file)

# ============================================
# Prediction Function
# ============================================

def predict_pain(
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
):
    """
    Predict pain level using trained model.
    """

    features = np.array([[
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
    ]])

    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    label_map = {
        0: "High",
        1: "Low",
        2: "Medium"
    }

    pain_level = label_map[prediction]

    return pain_level, probability