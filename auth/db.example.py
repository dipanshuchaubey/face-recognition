import mysql.connector

def databaseConnection():

    mydb = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        database=""
    )

    return mydb



