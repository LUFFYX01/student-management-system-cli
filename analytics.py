from db_connection import get_connection


def system_dashboard():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Total students
        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]

        # Average marks
        cursor.execute("SELECT AVG(marks_obtained) FROM marks")
        avg_marks = cursor.fetchone()[0]

        # Students below 75% attendance
        query = """
        SELECT COUNT(*)
        FROM attendance
        WHERE (attended_classes / total_classes) * 100 < 75
        """

        cursor.execute(query)
        low_attendance = cursor.fetchone()[0]

        # Top performer
        query = """
        SELECT s.name, AVG(m.marks_obtained) as avg_score
        FROM marks m
        JOIN students s ON m.student_id = s.student_id
        GROUP BY m.student_id
        ORDER BY avg_score DESC
        LIMIT 1
        """

        cursor.execute(query)
        top_student = cursor.fetchone()

        print("\n===== SYSTEM DASHBOARD =====\n")

        print("Total Students           :", total_students)
        print("Average Marks            :", round(avg_marks, 2) if avg_marks else 0)
        print("Students Below 75% Att.  :", low_attendance)

        if top_student:
            print(f"Top Performer            : {top_student[0]} ({round(top_student[1],2)})")

        print("\n============================\n")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()