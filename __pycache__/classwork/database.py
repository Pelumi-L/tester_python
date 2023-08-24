import mysql.connector
db_name = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'university_db'
)
cursor = db_name.cursor()
if(cursor):
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS `API_CONTENT`(
                    `Country` VARCHAR(50),
                    `Domains` VARCHAR(50),
                    `Alpha_two_code` VARCHAR(50),
                    `State_province` VARCHAR(50),
                    `Web_pages` VARCHAR(50),
                    `Name` VARCHAR(50)
                    );
    """)
    print("Table created.")
else: 
    print("Not created.")