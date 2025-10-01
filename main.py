from app.model import Carreras

nuevaCarrera = Carreras("Ingenieria en Sistemas", 5, "Carrera orientada al desarrollo de software.")
print("Carrera agregada con éxito.")

print(Carreras.ver_carreras())