especialidades = []
cupos = []
opciones = True
while opciones:
    operacion = int(input("Ingrese la operacion que desea realizar\n" \
    "1.	Ingresar lista de especialidades\n" \
    "2. 2.	Ingresar lista de cupos disponibles por especialidad\n" \
    "3.	Mostrar agenda\n" \
    "4.	Consultar cupos de una especialidad\n" \
    "5.	Listar especialidades sin cupos\n" \
    "6.	Actualizar cupos, reservar o cancelar (r/c) \n"
    "7. Salir\n"))
    match operacion:
        case 1:
            cantidad_especialidades = int(input("Ingrese cuantas especialidades desea añadir:"))
            for i in range(0, cantidad_especialidades):
                especialidad = input("Ingrese la especialidad que desea añadir:")
                if especialidad not in especialidades:
                    especialidades.append(especialidad)
                else:
                    print("La especialidad ya se encuentra en la lista")
        case 2:
            if especialidades != []:
                cupos.clear()
                for i in range(0, len(especialidades)):
                    cantidad_cupos = int(input(f"Ingrese la cantidad de cupos que va a tener la especialidad '{especialidades[i]}': "))
                    cupos.append(cantidad_cupos)
            else:
                print("No hay especialidades en la lista")
        case 3:
            print("Agenda de especialidades y cupos:")
            for i in range(0, len(especialidades)):
                print(f"Especialidades: '{especialidades[i]}'")
                print(f"Cupos: '{cupos[i]}'")
        case 4:
            buscar_especialidad = input("Ingrese la especialidad a la que quiera ver los cupos disponibles")
            if buscar_especialidad in especialidades:
                print(f"La cantidad de cupos de '{buscar_especialidad}' es de {cupos[especialidades.index(buscar_especialidad)]}")
        case 5:
            if 0 in cupos:
                for i in range(0, len(especialidades)):
                    if cupos[i] == 0:
                        print(f"La especialidad {especialidades[i]} tiene 0 cupos")
            else:
                    print("No hay especialidades sin cupos")
        case 6:
            especialidad = input("Ingrese la especialidad que desee actualizar el cupo: ")
            if especialidad in especialidades:
                solicitud = input("Desea reservar o cancelar un cupo? (r,c)").lower()
                if solicitud == "r":
                    indice = especialidades.index(especialidad)
                    if cupos[indice] > 0:
                        resta = cupos[indice] - 1
                        cupos[indice] = resta
                    else:
                        print("No hay cupos disponibles para reservar")
                elif solicitud == "c":
                    suma = cupos[especialidades.index(especialidad)] + 1
                    cupos[especialidades.index(especialidad)] = suma
            else:
                print("No se encontro dicha especialidad")
        case 7:
            opciones = False





