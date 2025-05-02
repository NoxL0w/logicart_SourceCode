from .db_connection import get_db_connection

def register_user(user):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO user_registration (UserID, Username, Password, AccountType, Email,
                                       ContactNum, TelephoneNum, FirstName, LastName,
                                       CompanyName, Owner)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        user['UserID'], user['Username'], user['Password'], user['AccountType'],
        user['Email'], user['ContactNum'], user['TelephoneNum'], user['FirstName'],
        user['LastName'], user['CompanyName'], user['Owner']
    )
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_registration WHERE UserID = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
