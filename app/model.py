from app.config import mydb

class Carreras:
    def __init__(self, nombre, duracion, descripcion):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__descripcion = descripcion
        self.agregar_carrera()

    def agregar_carrera(self):
        cursor = mydb.cursor()
        sql = "INSERT INTO carreras (nombre, duracion, descripcion) VALUES (%s, %s, %s)"
        values = (self.__nombre, self.__duracion, self.__descripcion)
        cursor.execute(sql, values)
        self.__id = cursor.lastrowid
        mydb.commit()

    def ver_carreras():
        cursor = mydb.cursor()
        sql = "SELECT * FROM carreras"
        cursor.execute(sql)
        return cursor.fetchall()