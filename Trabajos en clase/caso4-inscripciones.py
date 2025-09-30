clases = []
cupos = []
continuar = True
while continuar:
    opcion = int(input("Ingrese una opcion \n"
                    "1.	Ingresar lista de clases \n"
                    "2.	Ingresar cupos por clase \n"
                    "3.	Mostrar clases con cupos \n"
                    "4.	Consultar cupo de una clase \n"
                    "5.	Listar clases sin cupo \n"
                    "6.	Actualizar cupos (inscribir/baja) \n"
                    "7.	Salir \n"))
    match opcion:
        case 1:
            cantidad_clases = int(input("Ingrese la cantidad de clases que va a agregar al gimnasio: "))
            for i in range(0, cantidad_clases):
                nombre_clase = input("Ingrese la clase que desee: ").lower()
                if nombre_clase != "":
                    if nombre_clase not in clases:
                        clases.append(nombre_clase)
                        cupos[i] == 0
                    else:
                        print(f"La clase '{nombre_clase}' ya esta registrada")
                else:
                    print(f"No tiene nombre la clase")
        case 2:
            if len(clases) > 0:
                for i in range(0, len(clases)):
                    cupo_clase = int(input(f"Ingrese el cupo de la clase {clases[i]}: "))
                    if cupo_clase >= 0:
                        cupos.insert(i, cupo_clase)
                    else:
                        print("No se pueden ingresar numeros negativos")
        case 3:
            if len(clases) > 0:
                for i in range(0, len(clases)):
                    print(f"Clase: {clases[i]}")
                    print(f"Cupos disponibles: {cupos[i]}")
        case 4:
            if len(clases) > 0:
                buscar_clase = input("Ingrese el nombre de la clase que quiera saber los cupos: ")
                if buscar_clase in clases:
                    print(f"A la clase '{buscar_clase}' le quedan {cupos[clases.index(buscar_clase)]}")
        case 5:
            if len(clases) > 0:
                for i in range(0, len(clases)):
                    if cupos[i] == 0:
                        print(f"La clase '{clases[i]}' tiene 0 cupos")
        case 6:
            if len(clases) > 0:
                clase_a_operar = input("Ingrese la clase con la que desee operar: ").strip(",.- ").lower()
                if clase_a_operar in clases:
                    operacion = input("Se va a inscribir o bajar de la clase? (i/b): ").lower()
                    if operacion == "i":
                        resta = cupos[clases.index(clase_a_operar)] - 1
                        cupos[clases.index(clase_a_operar)] = resta
                        print(f"La clase '{clase_a_operar}' tiene {cupos[clases.index(clase_a_operar)]} cupos")
                    elif operacion == "d":
                        suma = cupos[clases.index(clase_a_operar)] + 1
                        cupos[clases.index(clase_a_operar)] = suma
                        print(f"La clase '{clase_a_operar}' tiene {cupos[clases.index(clase_a_operar)]} cupos")
                    else:
                        print("Operacion no valida")
        case 7:
            continuar = False
        case _:
            print("No se reconoce la opcion, porfavor ingrese una de las opciones dadas")