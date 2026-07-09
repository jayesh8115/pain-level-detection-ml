from database import connect_db

# -------------------------------
# Create Tables
# -------------------------------

def create_tables():

    conn = connect_db()

    if conn is None:
        return

    cursor = conn.cursor()

    # -------------------------------
    # Users Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100),
        password VARCHAR(255)
    )
    """)

    # -------------------------------
    # Patients Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        patient_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        gender VARCHAR(20),
        phone VARCHAR(20),
        weight FLOAT,
        height FLOAT,
        medical_history TEXT
    )
    """)

    # -------------------------------
    # Predictions Table
    # -------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    patient_id INT NOT NULL,

    pain_level VARCHAR(20) NOT NULL,

    confidence FLOAT NOT NULL,

    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id)
    ON DELETE CASCADE
    )
    """)

    conn.commit()

    print("✅ All Tables Created Successfully")

    cursor.close()
    conn.close()


# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    create_tables()