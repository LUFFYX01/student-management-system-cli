from db_connection import get_connection
from validation import validate_marks


# ------------------------------
# Add Marks
# ------------------------------
def add_marks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))
        subject = input("Enter Subject: ")

        marks = int(input("Enter Marks Obtained: "))
        if not validate_marks(marks):
            print("Entered Marks is not valid.")
            return

        query = """
        INSERT INTO marks (student_id, subject, marks_obtained)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (student_id, subject, marks))
        conn.commit()

        print("Marks added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ------------------------------
# View Marks
# ------------------------------
def view_marks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))

        query = "SELECT subject, marks_obtained FROM marks WHERE student_id = %s"
        cursor.execute(query, (student_id,))

        records = cursor.fetchall()

        print("\nMarks:")
        for row in records:
            print(f"Subject: {row[0]} | Marks: {row[1]}")

        if not records:
            print("No marks found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ------------------------------
# Update Marks
# ------------------------------
def update_marks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))
        subject = input("Enter Subject: ")
        
        new_marks = int(input("Enter New Marks: "))
        if not validate_marks(new_marks):
            print("Entered marks is not valid.")
            return

        query = """
        UPDATE marks
        SET marks_obtained = %s
        WHERE student_id = %s AND subject = %s
        """

        cursor.execute(query, (new_marks, student_id, subject))
        conn.commit()

        if cursor.rowcount > 0:
            print("Marks updated successfully!")
        else:
            print("Record not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ------------------------------
# Calculate Average Marks
# ------------------------------
def calculate_average():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))

        query = "SELECT AVG(marks_obtained) FROM marks WHERE student_id = %s"
        cursor.execute(query, (student_id,))

        result = cursor.fetchone()

        if result[0] is not None:
            print("Average Marks:", round(result[0], 2))
        else:
            print("No marks available.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()