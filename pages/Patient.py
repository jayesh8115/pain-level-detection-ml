import streamlit as st
import pandas as pd
from database.crud import add_patient, get_all_patients, delete_patient

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Patient Management",
    page_icon="👨‍⚕️",
    layout="wide"
)

# --------------------------------------------------------
# Login Check
# --------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("Please login first.")
    st.stop()


# --------------------------------------------------------
# Title
# --------------------------------------------------------

st.title("👨‍⚕️ Patient Management System")
st.write("Register, Search, Update and Delete Patient Records")

st.divider()

# --------------------------------------------------------
# Add Patient
# --------------------------------------------------------

st.subheader("➕ Register New Patient")

with st.form("patient_form"):

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("Full Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=25
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

    with col2:

        phone = st.text_input("Phone Number")

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            value=60.0
        )

        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            value=170.0
        )

    medical_history = st.text_area(
        "Medical History"
    )

    submit = st.form_submit_button(
        "Register Patient"
    )

if submit:

    if name.strip() == "":
        st.error("Patient name cannot be empty.")

    elif len(phone) != 10 or not phone.isdigit():
        st.error("Enter a valid 10-digit phone number.")

    else:

        add_patient(
        name,
        age,
        gender,
        phone,
        weight,
        height,
        medical_history
        )

        st.success("Patient Registered Successfully!")

        st.rerun()

st.divider()

# --------------------------------------------------------
# Search Patient
# --------------------------------------------------------

st.subheader("🔍 Search Patient")

search = st.text_input("Enter Patient Name or ID")

# Get all patients from MySQL
patients = get_all_patients()


filtered = []

if search.strip() != "":

    for patient in patients:

        if (
            search.lower() in patient["name"].lower()
            or
            search.lower() in str(patient["patient_id"]).lower()
        ):

            filtered.append(patient)

else:

    filtered = patients


# --------------------------------------------------------
# Display Patients
# --------------------------------------------------------

st.subheader("📋 Registered Patients")

if len(filtered) == 0:

    st.info("No patient records found.")

else:

    df = pd.DataFrame(filtered)

    # Optional: Rename column names for better display
    df = df.rename(columns={
        "patient_id": "Patient ID",
        "name": "Name",
        "age": "Age",
        "gender": "Gender",
        "phone": "Phone",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "medical_history": "Medical History"
    })

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# --------------------------------------------------------
# Delete Patient
# --------------------------------------------------------

st.subheader("🗑 Delete Patient")

# Get all patients from MySQL
patients = get_all_patients()

if len(patients) > 0:

    ids = [
        patient["patient_id"]
        for patient in patients
    ]

    delete_id = st.selectbox(
        "Select Patient ID",
        ids
    )

    if st.button("Delete Patient"):

        delete_patient(delete_id)

        st.success("✅ Patient Deleted Successfully")

        st.rerun()

else:

    st.info("No Patients Available")

st.divider()

# --------------------------------------------------------
# Statistics
# --------------------------------------------------------

st.subheader("📊 Patient Statistics")

# Get all patients from MySQL
patients = get_all_patients()

# Calculate Statistics
total = len(patients)

male = len([
    p
    for p in patients
    if p["gender"] == "Male"
])

female = len([
    p
    for p in patients
    if p["gender"] == "Female"
])

other = len([
    p
    for p in patients
    if p["gender"] == "Other"
])

# Display Statistics
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Patients", total)

with c2:
    st.metric("Male", male)

with c3:
    st.metric("Female", female)

with c4:
    st.metric("Other", other)

st.divider()

# --------------------------------------------------------
# Navigation
# --------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    if st.button("🏠 Home"):

        st.switch_page("pages/Home.py")

with col2:

    if st.button("📊 Dashboard"):

        st.switch_page("pages/Dashboard.py")

with col3:

    if st.button("🩺 Predict Pain"):

        st.switch_page("pages/Predict.py")