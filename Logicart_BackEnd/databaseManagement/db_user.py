from Logicart_BackEnd.databaseManagement import db_connection

def authenticate_user(username, password):
    
    cursor = db_connection.db.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    cursor.close()
    return user

def register_user(username, password, email):
    cursor = db_connection.db.cursor(dictionary=True)
    query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (username, password, email))
        db_connection.db.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        db_connection.db.rollback()
        return False
    finally:
        cursor.close()