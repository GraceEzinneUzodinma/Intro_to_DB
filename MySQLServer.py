import mysql.connector
try:
    mydb = mysql.connector.connect(
        host ="localhost", 
        user = "root", 
        passwd = "Amarachiezinne08",
        auth_plugin = 'mysql_native_password'
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("Failure to connect to the database")
finally:
    if mydb in locals() and mydb.is_connected():
        mydb.close()
        print("Connection closed")

