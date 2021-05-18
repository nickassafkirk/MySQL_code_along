import os
import pymysql


# Get username from workspace
username = os.getenv("user_name")


# connect to the database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the conenction, regardless of whether above was succesful
    connection.close()
