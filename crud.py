from database.database import connect_db


# ============================================
# Add New Patient
# ============================================

def add_patient(name, age, gender, phone, weight, height, medical_history):

    conn = connect_db()

    if conn is None:
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO patients
    (name, age, gender, phone, weight, height, medical_history)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        name,
        age,
        gender,
        phone,
        weight,
        height,
        medical_history
    )

    cursor.execute(query, values)

    conn.commit()

    print("✅ Patient Added Successfully")

    cursor.close()
    conn.close()


# ============================================
# View All Patients
# ============================================

def get_all_patients():

    conn = connect_db()

    if conn is None:
        return []

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")

    patients = cursor.fetchall()

    cursor.close()
    conn.close()

    return patients


# ============================================
# Search Patient
# ============================================

def search_patient(patient_id):

    conn = connect_db()

    if conn is None:
        return None

    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM patients WHERE patient_id=%s"

    cursor.execute(query, (patient_id,))

    patient = cursor.fetchone()

    cursor.close()
    conn.close()

    return patient


# ============================================
# Delete Patient
# ============================================

def delete_patient(patient_id):

    conn = connect_db()

    if conn is None:
        return

    cursor = conn.cursor()

    query = "DELETE FROM patients WHERE patient_id=%s"

    cursor.execute(query, (patient_id,))

    conn.commit()

    print("✅ Patient Deleted Successfully")

    cursor.close()
    conn.close()

# ============================================
# Save Prediction
# ============================================

def save_prediction(patient_id, pain_level, confidence):

    conn = connect_db()

    if conn is None:
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO predictions
    (patient_id, pain_level, confidence)
    VALUES (%s, %s, %s)
    """

    values = (
        patient_id,
        pain_level,
        confidence
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()

# ============================================
# Get Prediction History
# ============================================

def get_prediction_history():

    conn = connect_db()

    if conn is None:
        return []

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT

        pr.prediction_id,
        p.patient_id,
        p.name,
        p.gender,
        p.age,

        pr.pain_level,
        pr.confidence,
        pr.prediction_date

    FROM predictions pr

    INNER JOIN patients p

    ON pr.patient_id = p.patient_id

    ORDER BY pr.prediction_date DESC
    """

    cursor.execute(query)

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history

# ============================================
# Get Total Patients
# ============================================

def get_total_patients():

    conn = connect_db()

    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM patients")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


# ============================================
# Get Total Males
# ============================================

def get_total_males():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM patients WHERE gender='Male'"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

# ============================================
# Get Total Females
# ============================================

def get_total_females():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM patients WHERE gender='Female'"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

# ============================================
# Get Total Others
# ============================================

def get_total_others():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM patients WHERE gender='Other'"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total

# Testing the file temporarily to see if it works with the new database connection function.
# if __name__ == "__main__":

#     add_patient(
#         "Jayesh Sawant",
#         21,
#         "Male",
#         "9876543210",
#         65,
#         170,
#         "No major illness"
#     )

#     print(get_all_patients())


# Testing 
# if __name__ == "__main__":

#     save_prediction(
#         1,
#         "Medium",
#         0.96
#     )

#     print(get_prediction_history())