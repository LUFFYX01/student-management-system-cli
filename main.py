from auth import login
from student import add_student, view_students, update_student, delete_student, search_student
from marks import add_marks, view_marks, update_marks, calculate_average
from attendance import add_attendance, view_attendance, update_attendance
from report import student_report
from analytics import system_dashboard
import logging


logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# from auth import register_admin
# register_admin()

def menu():
    while (True):
        
        print("\n" + "="*40)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("="*40)

        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Add Marks")
        print("7. View Marks")
        print("8. Update Marks")
        print("9. Calculate Average")
        print("10. Add Attendance")
        print("11. View Attendance")
        print("12. Update Attendance")
        print("13. Student Report")
        print("14. System Dashboard")
        print("15. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            add_marks()
        elif choice == "7":
            view_marks()
        elif choice == "8":
            update_marks()
        elif choice == "9":
            calculate_average()
        elif choice == "10":
            add_attendance()
        elif choice == "11":
            view_attendance()
        elif choice == "12":
            update_attendance()
        elif choice == "13":
            student_report()
        elif choice == "14":
            system_dashboard()
        elif choice == "15":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Try again.")

if login():
     menu()
else:
    print("❌ Access Denied")
