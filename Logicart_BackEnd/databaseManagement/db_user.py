from Logicart_BackEnd.databaseManagement import db_connection
import random
from datetime import datetime

def UserID_generator():
    # Generate a unique UserID (e.g., using UUID or auto-increment in the database)
    UserID = datetime.now().strftime("%Y%m%d") + f"{random.randint(1, 9999):04d}" # Example format
    return UserID

def authenticate_user(username, password):
    
    cursor = db_connection.db.cursor(dictionary=True)
    query = query = "SELECT * FROM user_registration WHERE Username = %s AND Password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def register_user(username, password, email, FirstName, LastName):
    cursor = db_connection.db.cursor(dictionary=True)
    query = """
        INSERT INTO `user_registration`
        (`UserID`, `Username`, `Password`, `AccountType`, `Email`, `ContactNum`, `TelephoneNum`, `FirstName`, `LastName`, `CompanyName`, `Owner`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    UserID = UserID_generator()
    AccountType = "user"
    ContactNum = "none"
    TelephoneNum = "none"
    CompanyName = "none"
    Owner = "none"

    try:
        if not all([username, password, email, FirstName, LastName]):
            raise ValueError("All fields are required.")
        cursor.execute(query, (UserID, username, password, AccountType, email, ContactNum, TelephoneNum, FirstName, LastName, CompanyName, Owner))
        db_connection.db.commit()
        return True
    except Exception as e:
        print(f"Registration error: {e}")
        db_connection.db.rollback()
        return False
    finally:
        cursor.close()