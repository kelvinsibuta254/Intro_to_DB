import mysql.connector

try:

    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "alx_book_store"
        )
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS alx_book_store")
    connection.commit()
    print("connection successful")

except mysql.connector.Error as e:
    print(e)
    