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
        list_of_names = ['Fred', 'Bob', 'Jim']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()

finally:
    # close the conenction, regardless of whether above was succesful
    connection.close()
