from db_connection import get_connection


# Add attendance
def add_attendance():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))
        total_classes = int(input("Enter Total Classes: "))
        attended_classes = int(input("Enter Attended Classes: "))

        query = """
        INSERT INTO attendance (student_id, total_classes, attended_classes)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (student_id, total_classes, attended_classes))
        conn.commit()

        print("Attendance record added successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# View attendance
def view_attendance():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT s.student_id, s.name, a.total_classes, a.attended_classes
        FROM attendance a
        JOIN students s
        ON a.student_id = s.student_id
        """

        cursor.execute(query)
        records = cursor.fetchall()

        print("\n===== ATTENDANCE RECORDS =====")

        for row in records:
            percentage = (row[3] / row[2]) * 100 if row[2] != 0 else 0

            print(f"""
                  Student ID : {row[0]}
                  Name       : {row[1]}
                  Total      : {row[2]}
                  Attended   : {row[3]}
                  Attendance : {percentage:.2f} %
                  ---------------------------
                  """)

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# Update attendance
def update_attendance():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))
        total = int(input("Enter New Total Classes: "))
        attended = int(input("Enter New Attended Classes: "))

        query = """
        UPDATE attendance
        SET total_classes = %s, attended_classes = %s
        WHERE student_id = %s
        """

        cursor.execute(query, (total, attended, student_id))
        conn.commit()

        print("Attendance updated successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()