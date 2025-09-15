biblioteca = []
ejemplares = []
cero_ejemplares = []
opciones = "s"
operaciones = 0
while opciones == "s":
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
    if operaciones == 1:
        cant_libros = int(input("Ingrese la cantidad de libros que quiera añadir "))
        for i in range(0, cant_libros):
            titulo = ""
            titulo = input("Ingrese el libro que quiera añadir ")
            if titulo not in biblioteca:
                biblioteca.append(titulo)
    elif operaciones == 2:
        if biblioteca != []:
            for i in range(0, len(biblioteca)):
                cantidad = 0
                cantidad = int(input(f"Ingrese la cantidad de copias que va a tener el libro '{biblioteca[i]}': " ))
                ejemplares.append(cantidad)
    elif operaciones == 3:
        print("Catalogo y stock de libros: ")
        for i in range(0,len(biblioteca)):
            print(f"Titulo: '{biblioteca[i]}' - Ejemplares: {ejemplares[i]}")
    elif operaciones == 4:
        buscar_libro = input("Ingrese el titulo que desea buscar: ")
        if buscar_libro in biblioteca:
            indice = biblioteca.index(buscar_libro)
            print(f"El libro '{buscar_libro}' tiene {ejemplares[indice]} ejemplares")
        else:
            print("El libro no se encuentra en el catalogo")
    elif operaciones == 5:
        print("Los titulos agotados son:")
        for i in range(0, len(ejemplares)):
            if ejemplares[i] == 0:
                cero_ejemplares.append(biblioteca[i])
                print(cero_ejemplares[i])
    elif operaciones == 6:
        nuevo_titulo = input("Ingrese el titulo que desee agregar: ")
        if nuevo_titulo not in biblioteca:
            biblioteca.append(nuevo_titulo)
            cantidad_nuevo = int(input("Ingrese la cantidad de ejemplares que va a tener el libro: "))
            ejemplares.append(cantidad_nuevo)
        else:
            print("El titulo ya se encuentra en el catalogo")
    elif operaciones == 7:
        print ("Los titulos agotados son:")
        for i in range(0, len(ejemplares)):
            if ejemplares[i] == 0:
                print(biblioteca[i])
    elif operaciones == 8:
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
    elif operaciones == 9:
        print("Catalogo de libros:")
        for i in range(0, len(biblioteca)):
            print(f"Titulo: '{biblioteca[i]}'")
    elif operaciones == 10:
        print("Saliendo del programa...")
        break
    opciones = input("Desea seguir o salir de la operacion? (s/n) ").lower()

