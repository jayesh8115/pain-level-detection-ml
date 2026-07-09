import mysql.connector

# -------------------------------
# Database Connection Function
# -------------------------------

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jayesh811",   # Replace with your MySQL password
            database="pain_detection_db"
        )

        print("✅ Database Connected Successfully")
        return connection

    except mysql.connector.Error as err:
        print("❌ Database Connection Failed")
        print(err)
        return None


# -------------------------------
# Test Connection
# -------------------------------

if __name__ == "__main__":
    conn = connect_db()

    if conn:
        conn.close()
        print("🔒 Connection Closed")