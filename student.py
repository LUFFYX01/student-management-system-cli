from db_connection import get_connection
from validation import validate_email, validate_phone, validate_age
import logging

# =======================================
# CREATE - Add Student
# =======================================

def add_student():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        name = input("Enter Name: ")
        
        age = int(input("Enter Age: "))
        if not validate_age(age):
            print("Invalid age")
            return
        
        gender = input("Enter Gender(Male/Female/Other): ")

        email = input("Enter Email(abc@gmail.com): ")
        if not validate_email(email):
            print("Invalid email format")
            return
        
        phone = input("Enter Phone Number: ")
        if not validate_phone(phone):
            print("Phone Number must be 10 digits")
            return
        
        address = input("Enter Address: ")
        year = int(input("Enter Year: "))

        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        print("\nAvailable Courses:")
        for c in courses:
            print(f"{c[0]} - {c[1]}")

        course_id = int(input("Enter Course ID: "))

        query = """ INSERT INTO students 
        (name , age , gender , email , phone , address , year , course_id)
        Values (%s , %s , %s ,%s , %s ,%s , %s , %s)"""

        cursor.execute(query, (name, age, gender, email, phone, address, year, course_id))
        conn.commit()

        logging.info(f"Student added: {name}")

        print("😁 Student added successfully!")

    except Exception as e:
        print("😢 Error: ", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    

# =========================================
# READ - VIEW ALL STUDENTS 
# =========================================

def view_students():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        SELECT s.student_id, s.name, s.age, s.gender, s.email,
               s.phone, s.address, s.year, c.course_name
        FROM students s
        LEFT JOIN courses c
        ON s.course_id = c.course_id
        """

        cursor.execute(query)
        records = cursor.fetchall()

        if not records:
            print("No students found.")
            return

        print("\n===== STUDENT LIST =====\n")

        for row in records:
            print(f"""
                  Student ID : {row[0]}
                  Name       : {row[1]}
                  Age        : {row[2]}
                  Gender     : {row[3]}
                  Email      : {row[4]}
                  Phone      : {row[5]}
                  Address    : {row[6]}
                  Year       : {row[7]}
                  Course     : {row[8]}
                  --------------------------------------
                  """)

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# =========================================
# UPDATE - update Student Email & Phone
# =========================================

def update_student():
    try:
        conn = get_connection()
        cursor = conn.connection()

        student_id = int(input("Enter Student ID to update: "))
        new_email = input("Enter New Email: ")
        new_phone = input("Enter New Phone Number: ")

        query = """Update students SET email = %s , phone = %s WHERE student_id = %s"""

        cursor.execute(query,(new_email , new_phone , student_id))
        conn.commit()

        logging.info(f"Student updated with ID: {student_id}")

        if cursor.rowcount > 0:
            print("😁 Student updated successfully!")
        else:
            print("😢 No student found with that ID.")

    except Exception as e:
        print("😢 Error: ",e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# ================================================
# DELETE - Remove Student 
# ================================================

def delete_student():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        student_id = int(input("Enter Student ID to delete: "))
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()

        logging.info(f"Student deleted with ID: {student_id}")

        if cursor.rowcount > 0:
            print("😁 Student deleted successfully!")
        else:
            print("😢 No student found with that ID.")
    
    except Exception as e:
        print("😢 Error: ", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


# ==========================================
# SEARCH - Search by Name
# ==========================================

def search_student():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        keyword = input("Enter name to search: ")

        query = "SELECT * FROM students WHERE name LIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))

        results = cursor.fetchall()

        print("\n------ Search Results ------")
        for row in results:
            print(row)

        if not results:
            print("⚠ No matching students found.")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()