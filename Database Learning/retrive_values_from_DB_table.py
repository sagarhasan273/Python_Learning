import mysql.connector
from mysql.connector import errorcode


try:
    myConnection = mysql.connector.connect(
        user = 'root',
        password = 'admin2968',
        host = 'localhost',
        database = 'mydatabase2'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access deny for using wrong password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist!")
    else:
        print(err)

myCursor = myConnection.cursor()


def check(find_by_id):
    sql = "SELECT * FROM demo_table WHERE id = '{}'".format(find_by_id)
    myCursor.execute(sql)
    myResult = myCursor.fetchall()
    print(myResult)
    pass

find_by_id = int(input("Find by id and give id: "))

check(find_by_id)
