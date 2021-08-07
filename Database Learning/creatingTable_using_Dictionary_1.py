import mysql.connector
from mysql.connector import errorcode


DB_Name = 'employees'

Table = {}
Table['employees'] = (
    "CREATE TABLE `employees` ("
    "`emp_no` INT(11) NOT NULL AUTO_INCREMENT,"
    "`birth_date` VARCHAR(15) NOT NULL,"
    "`first_name` VARCHAR(15) NOT NULL,"
    "`last_name` VARCHAR(15) NOT NULL,"
    "`gender` enum('F', 'M') NOT NULL,"
    "`hire_date` DATE NOT NULL,"
    " PRIMARY KEY (`emp_no`)"
    ") ENGINE = InnoDB"
)
# Table['employees'] = (
#     "CREATE TABLE `employees` ("
#     "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `birth_date` date NOT NULL,"
#     "  `first_name` varchar(14) NOT NULL,"
#     "  `last_name` varchar(16) NOT NULL,"
#     "  `gender` enum('M','F') NOT NULL,"
#     "  `hire_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`)"
#     ") ENGINE=InnoDB")



def createDatabase():
    myConnection = mysql.connector.connect(
        user = 'root',
        password = 'admin2968',
        host = 'localhost'
    )
    myCursor = myConnection.cursor()
    try:
        myCursor.execute(f"USE {DB_Name}")
        myCursor.execute(Table['employees'])
    except mysql.connector.Error as err:
        myCursor.execute(f"CREATE DATABASE {DB_Name}")
        print("Database now exist!")
    


try:
    myConnection = mysql.connector.connect(
        user = 'root',
        password = 'admin2968',
        host = 'localhost',
        database = 'NULL'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access deny for using wrong password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist!")
        createDatabase()
    else:
        print(err)




