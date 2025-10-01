import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

print(mydb)