# Pain Level Detection Using Biosignals

A Machine Learning project that predicts pain levels using physiological biosensor data through an interactive Streamlit web application.

---

## 📌 Project Overview

Pain assessment is an important part of healthcare but is often based on a patient's self-reported pain level. This project explores how Machine Learning can be used to predict pain levels from physiological biosensor data.

The application provides a simple and interactive interface built with Streamlit, allowing users to enter biosensor values and receive an instant pain level prediction.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, and deployment.

---

## 🚀 Features

- Predict pain levels using physiological biosensor data
- Interactive Streamlit web application
- User-friendly interface
- Data preprocessing and feature scaling
- Instant prediction results
- End-to-end Machine Learning workflow

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Matplotlib

---

## 📊 Dataset Features

The model uses physiological parameters such as:

- Heart Rate (HR)
- Blood Oxygen Saturation (SpO₂)
- Skin Temperature
- Galvanic Skin Response (GSR)
- Respiratory Rate
- Blood Volume Pulse (BVP)
- Age
- Gender

> **Note:** The exact features may vary depending on the dataset used for training.

---

## 🧠 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Scaling
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Streamlit Application
   │
   ▼
Pain Level Prediction
```

---

## 📂 Project Structure

```text
Pain-Level-Detection-Using-Biosignals/
│
├── database/
│   ├── crud.py                 # Database CRUD operations
│   ├── database.py             # Database connection
│   └── init_db.py              # Database initialization
│
├── ml/
│   ├── predict.py              # Prediction logic
│   ├── Project-1.ipynb         # Model training notebook
│   ├── rf_model.pkl            # Trained Random Forest model
│   └── scaler.pkl              # Feature scaler
│
├── pages/
│   ├── Dashboard.py            # Dashboard page
│   ├── History.py              # Prediction history
│   ├── Home.py                 # Home page
│   ├── Login.py                # Login page
│   ├── Patient.py              # Patient details page
│   └── Predict.py              # Prediction page
│
├── videos/
│   ├── home_background.mp4
│   ├── prediction_background.mp4
│   └── ...
│
├── main.py                     # Main Streamlit application
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore rules
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jayesh8115/Pain-Level-Detection-Using-Biosignals.git
```

### 2. Navigate to the project folder

```bash
cd Pain-Level-Detection-Using-Biosignals
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 📸 Application Screenshots

### Home Page

<img width="1920" height="1080" alt="Screenshot 2026-07-09 053544" src="https://github.com/user-attachments/assets/efbe1b62-4188-4954-9334-173d6eca168c" />


```
images/homepage.png
```

---

### Prediction Page

<img width="1920" height="1080" alt="Screenshot 2026-07-09 053755" src="https://github.com/user-attachments/assets/eb849c31-695a-440a-b592-ff3abed264d8" />


```
images/prediction.png
```

---

### Prediction Result

<img width="1920" height="1080" alt="Screenshot 2026-07-09 053905" src="https://github.com/user-attachments/assets/ea318fbb-3f3e-496e-a80b-2b8685f7fe39" />


```
images/result.png
```

---

## 💡 Future Improvements

- Improve prediction accuracy using advanced ML models
- Train on larger datasets
- Enhance the user interface
- Deploy the application online
- Add support for real-time biosensor data

---

## 👨‍💻 Author

**Jayesh Sawant**

B.Tech in Artificial Intelligence & Data Science

Pune Institute of Computer Technology (PICT)

GitHub: https://github.com/jayesh8115

---

## ⭐ If you found this project useful, consider giving it a star!
