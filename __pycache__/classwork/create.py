import mysql.connector
db_name = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)
dbcon = db_name.cursor()
if(dbcon):
    dbcon.execute("CREATE DATABASE IF NOT EXISTS `university_db`")
    print("Database created.")
else:
    print("not created.")