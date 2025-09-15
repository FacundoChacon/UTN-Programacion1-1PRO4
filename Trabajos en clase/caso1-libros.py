biblioteca = []
ejemplares = []
cero_ejemplares = []
# Se inicializan las listas y los controladores de los bulces
opciones = "s"
operaciones = 0
# Se ejecuta el menu de opciones
while opciones == "s":
    # Se muestran las opciens
    operaciones = int(input("Ingrese la operacion que desea realizar\n"
    "1. Añadir libro\n"
    "2. Añadir ejemplares\n"
    "3. Mostrar catalogo y stock\n"
    "4. Consultar disponibilidad de un título\n"
    "5. Lista de agotados\n"
    "6. Agregar un titulo\n"
    "7. Ver títulos agotados\n"
    "8. Actualizar ejemplares, préstamo o devolución (p/d):\n"
    "9. Ver catalogo\n"
    "10. Salir\n"
    ))
    
    if operaciones == 1: # Opcion para añadir libros
        cant_libros = int(input("Ingrese la cantidad de libros que quiera añadir "))
        for i in range(0, cant_libros):
            titulo = ""
            titulo = input("Ingrese el libro que quiera añadir ")
            if titulo not in biblioteca:
                biblioteca.append(titulo)
    elif operaciones == 2: # Opcion para añadir los ejemplares de dichos libros segun la cantidad de libros que hayan
        if biblioteca != []:
            for i in range(0, len(biblioteca)):
                cantidad = 0
                cantidad = int(input(f"Ingrese la cantidad de copias que va a tener el libro '{biblioteca[i]}': " ))
                ejemplares.append(cantidad)
    elif operaciones == 3: # Opcion para mostrar el catalogo y stock de libros
        print("Catalogo y stock de libros: ")
        for i in range(0,len(biblioteca)):
            print(f"Titulo: '{biblioteca[i]}' - Ejemplares: {ejemplares[i]}")
    elif operaciones == 4: # Opcion para consultar disponibilidad de un titulo y cuantos ejemplares tiene este
        buscar_libro = input("Ingrese el titulo que desea buscar: ")
        if buscar_libro in biblioteca:
            indice = biblioteca.index(buscar_libro)
            print(f"El libro '{buscar_libro}' tiene {ejemplares[indice]} ejemplares")
        else:
            print("El libro no se encuentra en el catalogo")
    elif operaciones == 5: # Opcion que muestra los titulos que estan agotados y los guardan en una lista
        print("Los titulos agotados son:")
        for i in range(0, len(ejemplares)):
            if ejemplares[i] == 0:
                cero_ejemplares.append(biblioteca[i])
                print(cero_ejemplares[i])
    elif operaciones == 6: # Opcion para agregar titulo y cantidad de un libro nuevo que se quiera añadir
        nuevo_titulo = input("Ingrese el titulo que desee agregar: ")
        if nuevo_titulo not in biblioteca:
            biblioteca.append(nuevo_titulo)
            cantidad_nuevo = int(input("Ingrese la cantidad de ejemplares que va a tener el libro: "))
            ejemplares.append(cantidad_nuevo)
        else:
            print("El titulo ya se encuentra en el catalogo")
    elif operaciones == 7: # Opcion para ver los titulos agotados
        print ("Los titulos agotados son:")
        for i in range(0, len(ejemplares)):
            if ejemplares[i] == 0:
                print(biblioteca[i])
    elif operaciones == 8: # Opcion para actualizar los ejemplares de un libro segun lo que se solicite
        accion = input("Ingrese si desea hacer un prestamo o una devolucion (p/d): ").lower()
        if accion == "p":
            titulo_prestamo = input("Ingrese el titulo que desea prestar: ")
            if titulo_prestamo in biblioteca:
                indice_prestamo = biblioteca.index(titulo_prestamo)
                if ejemplares [indice_prestamo] > 0:
                    ejemplares[indice_prestamo] -= 1
                    print(f"Prestamo realizado, quedan {ejemplares[indice_prestamo]} ejemplares de '{titulo_prestamo}'")
                else:
                    print("No hay ejemplares disponibles para prestar")
            else:
                print("El titulo no se encuentra en el catalogo")
        elif accion == "d":
            titulo_devolucion = input("Ingrese el titulo que desea devolver: ")
            if titulo_devolucion in biblioteca:
                indice_devolucion = biblioteca.index(titulo_devolucion)
                ejemplares[indice_devolucion] += 1
                print(f"Devolución realizada, ahora hay {ejemplares[indice_devolucion]} ejemplares de '{titulo_devolucion}'")
            else:
                print("El titulo no se encuentra en el catalogo")
    elif operaciones == 9: # Opcion para ver el catalogo de libros segun su titulo
        print("Catalogo de libros:")
        for i in range(0, len(biblioteca)):
            print(f"Titulo: '{biblioteca[i]}'")
    elif operaciones == 10: # Opcion para salir del programa
        print("Saliendo del programa...")
        break
    if operaciones != 10:
        print("Ingrese una opcion valida (1-10)")
    # Se pregunta si desea seguir o salir de la operacion
    opciones = input("Desea seguir o salir de la operacion? (s/n) ").lower()

