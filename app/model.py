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
    
    def actualizar_carrera(self, nombre=None, duracion=None, descripcion=None):
        cursor = mydb.cursor()
        updates = []
        values = []
        if nombre:
            updates.append("nombre = %s")
            values.append(nombre)
        if duracion:
            updates.append("duracion = %s")
            values.append(duracion)
        if descripcion:
            updates.append("descripcion = %s")
            values.append(descripcion)
        values.append(self.__id)
        sql = f"UPDATE carreras SET {', '.join(updates)} WHERE id = %s"
        cursor.execute(sql, values)
        mydb.commit()
        
    def eliminar_carrera(self):
        cursor = mydb.cursor()
        sql = "DELETE FROM carreras WHERE id = %s"
        values = (self.__id,)
        cursor.execute(sql, values)
        mydb.commit()