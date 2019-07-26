import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
def insertPythonVaribleInTable(userId, userName, joinDate, age):
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='python_db',
                             user='pynative',
                             password='pynative@#29')
        cursor = connection.cursor(prepared=True)
        sql_insert_query = """ INSERT INTO `python_users`
                      (`id`, `name`, `birth_date`, `age`) VALUES (%s,%s,%s,%s)"""
        insert_tuple = (userId, userName, joinDate, age)
        result  = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print ("Record inserted successfully into python_users table")
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
insertPythonVaribleInTable(11, "Ault", "2018-07-14", 34)
insertPythonVaribleInTable(12, "Mackee", "2017-03-28", 30)