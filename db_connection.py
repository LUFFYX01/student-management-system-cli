import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Prateek@001",  
            database="student_db"
        )

        if connection.is_connected():
            print("Connected to MySQL successfully")

        return connection

    except mysql.connector.Error as e:
        print("Database connection failed:", e)
        return None
