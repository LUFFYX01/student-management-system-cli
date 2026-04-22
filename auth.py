import bcrypt
from db_connection import get_connection
import logging

# ======================================
# Register Admin (Run Once)
# ======================================

def register_admin():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        username = input("Create Username: ")
        password = input("Create Passsword: ")

        # HASH PASSWORD
        hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        query = "INSERT INTO admin (username , password) VALUES(%s,%s)"
        cursor.execute(query, (username,hashed_password))
        conn.commit()

        print("😁 Admin registered successfully!")

    except Exception as e:
        print("😢 Error: ", e)

    finally:
        conn.close()

# =========================================
# LOGIN FUNCTION
# =========================================

def login():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        query = "SELECT password FROM admin WHERE username = %s"
        cursor.execute(query,(username,))
        result = cursor.fetchone()

        if(result):
            stored_password = bytes(result[0])
            print("Entered password: ",password.encode('utf-8'))
            print("stored password: ", stored_password)

            if(bcrypt.checkpw(password.encode('utf-8'),stored_password)):
                print("😁 Login Successfull!")

                logging.info(f"Login successful for user: {username}")

                return True
            
            else: 
                print("❌ Incorrect Password")

                logging.warning(f"Incorrect password attempt for user: {username}")

                return False
        
        else:
            print("😢 Username Not Found")

            logging.warning(f"Login attempt with invalid username: {username}")

            return False
    
    except Exception as e :
        logging.error(f"Login error: {e}")
        print("😢 Error: ",e)
        return False
    
    finally:
        conn.close()