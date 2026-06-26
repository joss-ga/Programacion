#sistema gestion de peliculas
listapeliculas = []

def imprimirMenu ():
    print("1. Agregar pelicula")
    print("2. Buscar Pelicula")
    print("3. Eliminar pelicula")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar peliculas")
    print("6. Salir")
    
def elegirOpcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in range(1, 7):
                return opcion
            else:
                print("Error: Ingrese una opcion entre 1 y 6.")
        except ValueError:
            print("Error: Ingrese un numero valido.")

def validarNombre():
    while True:
        nombre = input("Ingrese el nombre de la pelicula: ")
        if nombre.strip() != "":
            return nombre
        else:
            print("Error: El nombre no puede estar vacio.")

def validarduracion():
    while True:
        try:
            duracion = int(input("Ingrese la duracion de la pelicula: "))
            if duracion > 0:
                return duracion
            else:
                print("Error: La cantidad de duracion no puede ser negativa.")
        except ValueError:
            print("Error: Ingrese un numero valido.")

def validarcalificacion():
    while True:
        try:
            calificacion = float(input("Ingrese el calificacion de la pelicula (0.0 al 10.0): "))
            if 0.0 <= calificacion <= 10.0:
                return calificacion
            else:
                print("Error: El calificacion debe estar entre rangos 0.0 y 10.0.")
        except ValueError:
            print("Error: Ingrese un numero valido.")

def agregarpelicula(lista):
    nombre = validarNombre()
    duracion = validarduracion()
    calificacion = validarcalificacion()
    
    lista.append(
        {
            "nombre": nombre, 
            "duracion": duracion, 
            "calificacion": calificacion,
            "disponible": False
        }
    )
    return lista


def actualizarDisponibilidad(lista):
    for pelicula in lista:
        if pelicula["duracion"] > 0:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False
    return lista
        
def mostrarpeliculas(lista):
    actualizarDisponibilidad(lista)
    
    print("=== LISTA DE PELICULAS ===")
    for pelicula in lista:
        print("Nombre: "+pelicula["nombre"])
        print("duracion: "+str(pelicula["duracion"]))
        print("clasificacion: "+str(pelicula["calificacion"]))
        if pelicula["disponible"] == True:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN duracion")

def buscarpelicula(lista):
    nombre = validarNombre()
    for index, pelicula in enumerate(lista):
        if pelicula["nombre"] == nombre:
            return index
    return -1
    
def eliminarpelicula(lista):
    index = buscarpelicula(lista)
    if index == -1:
        print("No se encontro el pelicula.")
    else:
        del lista[index]
        print("pelicula eliminado exitosamente.")
    return lista
    


print("===Bienvenido al sistema de gestion de peliculas===")
while True:
    imprimirMenu()
    opcionElegida = elegirOpcion()
    if opcionElegida == 1:
        listapeliculas = agregarpelicula(listapeliculas)
    elif opcionElegida == 2:
        index = buscarpelicula(listapeliculas)
        if index == -1:
            print("No se encontro el pelicula.")
        else:
            print("Nombre: "+str(listapeliculas[index]["nombre"]))
            print("duracion: "+str(listapeliculas[index]["duracion"]))
            print("clasificacion: "+str(listapeliculas[index]["calificacion"]))
            if listapeliculas[index]["disponible"] == True:
                print("Estado: DISPONIBLE")
            else:
                print("Estado: SIN duracion")

    elif opcionElegida == 3:
        listapeliculas = eliminarpelicula(listapeliculas)
    elif opcionElegida == 4:
        listapeliculas = actualizarDisponibilidad(listapeliculas)
    elif opcionElegida == 5:
        if len(listapeliculas) == 0:
            print("No hay peliculas para mostrar.")
        else:
            mostrarpeliculas(listapeliculas)
    elif opcionElegida== 6:
        print("Gracias por usar el sistema. Vuelva Pronto.")
        break
