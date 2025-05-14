import mysql.connector

def fetch_data_as_dict():

    db = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="",   
        database="logicart"               
    )

    cursor = db.cursor(dictionary=True)  

    cursor.execute("SELECT * FROM product")

    rows = cursor.fetchall()

    db.close()
    return rows

data = fetch_data_as_dict()
for item in data:
    print(item)
