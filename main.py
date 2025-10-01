from app.model import Carreras, Carrera

def print_menu():
    print("\nSeleccione una opción:")
    print("1. Agregar nueva carrera")
    print("2. Ver todas las carreras")
    print("3. Actualizar carrera")
    print("4. Eliminar carrera")
    print("0. Salir")

dao = Carreras()
opcion = "-1"

while opcion != "0":
    print_menu()
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre de la carrera: ")
        while True:
            duracion = input("Ingrese la duración de la carrera (en años): ")
            if duracion.isdigit():
                duracion = int(duracion)
                break
            else:
                print("Por favor, ingrese un número válido para la duración.")
        descripcion = input("Ingrese una descripción de la carrera: ")
        nueva_carrera = Carrera(nombre=nombre, duracion=duracion, descripcion=descripcion)
        dao.agregar_carrera(nueva_carrera)
        print("Carrera agregada con éxito.")
    elif opcion == "2":
        carreras = dao.ver_carreras()
        for carrera in carreras:
            print(carrera)
    elif opcion == "3":
        carreras = dao.ver_carreras()
        for carrera in carreras:
            print(carrera)
        id_carrera = input("Ingrese el ID de la carrera a actualizar: ")
        if not id_carrera.isdigit():
            print("ID inválido.")
            continue
        id_carrera = int(id_carrera)
        carrera_seleccionada = None
        for carrera in carreras:
            if carrera.id == id_carrera:
                carrera_seleccionada = carrera
                break
        if carrera_seleccionada:
            nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            duracion = input("Nueva duración (dejar vacío para no cambiar): ")
            descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
            if nombre:
                carrera_seleccionada.nombre = nombre
            if duracion:
                if duracion.isdigit():
                    carrera_seleccionada.duracion = int(duracion)
                else:
                    print("Duración inválida, no se actualiza.")
            if descripcion:
                carrera_seleccionada.descripcion = descripcion
            dao.actualizar_carrera(carrera_seleccionada)
            print("Carrera actualizada con éxito.")
        else:
            print("ID no encontrado.")
    elif opcion == "4":
        carreras = dao.ver_carreras()
        for carrera in carreras:
            print(carrera)
        id_carrera = input("Ingrese el ID de la carrera a eliminar: ")
        if not id_carrera.isdigit():
            print("ID inválido.")
            continue
        id_carrera = int(id_carrera)
        dao.eliminar_carrera(id_carrera)
        print("Carrera eliminada con éxito.")
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida. Intente nuevamente.")
