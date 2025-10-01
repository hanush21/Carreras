from app.model import Carreras

def print_menu():
    print("\nSeleccione una opción:")
    print("1. Agregar nueva carrera")
    print("2. Ver todas las carreras")
    print("3. Actualizar carrera")
    print("4. Eliminar carrera")
    print("0. Salir")

opcion = "-1"

while(opcion != "0"):
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
        nueva_carrera = Carreras(nombre, duracion, descripcion)
        print("Carrera agregada con éxito.")
    elif opcion == "2":
        carreras = Carreras.ver_carreras()
        for carrera in carreras:
            print(f"ID: {carrera[0]}, Nombre: {carrera[1]}, Duración: {carrera[2]} años, Descripción: {carrera[3]}")
    elif opcion == "3":
        carreras = Carreras.ver_carreras()
        for carrera in carreras:
            print(f"ID: {carrera[0]}, Nombre: {carrera[1]}, Duración: {carrera[2]} años, Descripción: {carrera[3]}")
        id_carrera = int(input("Ingrese el ID de la carrera a actualizar: "))
        nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
        while True:
            duracion = input("Ingrese la duración de la carrera (en años): ")
            if duracion.isdigit():
                duracion = int(duracion)
                break
            else:
                print("Por favor, ingrese un número válido para la duración.")
        descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
        carrera_seleccionada = None
        for carrera in carreras:
            if carrera[0] == id_carrera:
                carrera_seleccionada = Carreras(carrera[1], carrera[2], carrera[3])
                carrera_seleccionada._Carreras__id = id_carrera  # Asignar el ID manualmente
                break
        if carrera_seleccionada:
            carrera_seleccionada.actualizar_carrera(
                nombre if nombre else None,
                int(duracion) if duracion else None,
                descripcion if descripcion else None
            )
            print("Carrera actualizada con éxito.")
        else:
            print("ID no encontrado.")
            
    elif opcion == "4":
        carreras = Carreras.ver_carreras()
        for carrera in carreras:
            print(f"ID: {carrera[0]}, Nombre: {carrera[1]}, Duración: {carrera[2]} años, Descripción: {carrera[3]}")
        id_carrera = int(input("Ingrese el ID de la carrera a eliminar: "))
        carrera_seleccionada = None
        for carrera in carreras:
            if carrera[0] == id_carrera:
                carrera_seleccionada = Carreras(carrera[1], carrera[2], carrera[3])
                carrera_seleccionada._Carreras__id = id_carrera  # Asignar el ID manualmente
                break
        if carrera_seleccionada:
            carrera_seleccionada.eliminar_carrera()
            print("Carrera eliminada con éxito.")
        else:
            print("ID no encontrado.")
    
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida. Intente nuevamente.")
        