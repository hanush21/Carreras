import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar variables del archivo .env
load_dotenv()

try:
    mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "carreras_db")
    )
    if mydb.is_connected():
        print("Conexión exitosa a la base de datos")
except Error as e:
    print(f"Error al conectar a la base de datos: {e}")