import mysql.connector
from mysql.connector import errorcode


try:
    mydb = mysql.connector.connect(
        user = 'root',
        password = 'admin2968',
        host = 'localhost',
        database = 'mydatabase2'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
        print("MySQL Connection error for invalide user name!")
    elif err.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
        print("MySQL Connection error for invalide password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist!")
    elif err.errno == errorcode.ER_BAD_HOST_ERROR:
        print("Host doesn't exist!")
    else:
        print(err)

myCursor = mydb.cursor()
sql = "INSERT INTO demo_table (name, address) VALUES (%s, %s)"
val = [
    ('sagar', 'rajendropur'),
    ('hasan', 'gazipur'),
    ('mitul', 'toggi'),
    ('rabid', 'rastay')
]

myCursor.executemany(sql, val)
# [print(*x) for x in myCursor.fetchall()]
mydb.commit()

