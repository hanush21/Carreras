from app.config import mydb

class Carrera:
    def __init__(self, id=None, nombre="", duracion=0, descripcion=""):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Duración: {self.duracion} años, Descripción: {self.descripcion}"

class Carreras:
    def __init__(self):
        self.db = mydb

    def agregar_carrera(self, carrera: Carrera):
        cursor = self.db.cursor()
        sql = "INSERT INTO carreras (nombre, duracion, descripcion) VALUES (%s, %s, %s)"
        values = (carrera.nombre, carrera.duracion, carrera.descripcion)
        cursor.execute(sql, values)
        carrera.id = cursor.lastrowid
        self.db.commit()
        return carrera

    def ver_carreras(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM carreras"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        carreras = []
        for fila in resultados:
            carreras.append(Carrera(id=fila[0], nombre=fila[1], duracion=fila[2], descripcion=fila[3]))
        return carreras

    def actualizar_carrera(self, carrera: Carrera):
        cursor = self.db.cursor()
        sql = "UPDATE carreras SET nombre = %s, duracion = %s, descripcion = %s WHERE idcarreras = %s"
        values = (carrera.nombre, carrera.duracion, carrera.descripcion, carrera.id)
        cursor.execute(sql, values)
        self.db.commit()

    def eliminar_carrera(self, id_carrera: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM carreras WHERE idcarreras = %s"
        cursor.execute(sql, (id_carrera,))
        self.db.commit()