from db_connection import get_connection
import csv


def student_report():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID: "))

        # Student + Course info
        query = """
        SELECT s.name, s.age, s.gender, c.course_name
        FROM students s
        LEFT JOIN courses c ON s.course_id = c.course_id
        WHERE s.student_id = %s
        """

        cursor.execute(query, (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        print("\n===== STUDENT REPORT =====")
        print(f"Name   : {student[0]}")
        print(f"Age    : {student[1]}")
        print(f"Gender : {student[2]}")
        print(f"Course : {student[3]}")

        # Marks
        cursor.execute(
            "SELECT subject, marks_obtained FROM marks WHERE student_id=%s",
            (student_id,)
        )
        marks = cursor.fetchall()

        print("\n--- Marks ---")
        total = 0

        for m in marks:
            print(f"{m[0]} : {m[1]}")
            total += m[1]

        if marks:
            avg = total / len(marks)
            print(f"Average Marks: {avg:.2f}")
        else:
            print("No marks available.")

        # Attendance
        cursor.execute(
            "SELECT total_classes, attended_classes FROM attendance WHERE student_id=%s",
            (student_id,)
        )

        attendance = cursor.fetchone()

        if attendance:
            percentage = (attendance[1] / attendance[0]) * 100
            print("\n--- Attendance ---")
            print(f"Total Classes   : {attendance[0]}")
            print(f"Attended        : {attendance[1]}")
            print(f"Attendance %    : {percentage:.2f}%")

            if percentage < 75:
                print("⚠ Warning: Attendance below 75%")

        else:
            print("\nNo attendance record.")
        
        filename = f"student_report_{student_id}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", student_id])
            writer.writerow(["Name", student[0]])
            writer.writerow(["Age", student[1]])
            writer.writerow(["Gender", student[2]])
            writer.writerow(["Course", student[3]])
            writer.writerow([])
            
            writer.writerow(["Subject", "Marks"])
            
            for m in marks:
                writer.writerow([m[0], m[1]])
            
        print(f"\nReport exported to {filename}")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()