subes = []
saldo = []
continuar = True
while continuar:
    opcion = int(input("Seleccione una opcion: \n" \
                "1.	Ingresar números de tarjeta \n" \
                "2.	Ingresar saldos correspondientes \n" \
                "3.	Mostrar todas las tarjetas y saldos \n" \
                "4.	Consultar saldo por número \n" \
                "5.	Listar saldos en negativo o cero \n" \
                "6.	Cargar/debitar saldo (c/d) \n" \
                "7. Salir \n"))
    match opcion:
        case 1:
            cantidad_subes = int(input("Ingrese la cantidad de tarjetas sube que desea ingresar: "))
            for i in range(0, cantidad_subes):
                tarjeta = input(f"Ingrese el numero de tarjeta (de 16 digitos enteros) para la sube nº{i}: ").strip(",. -")
                if len(tarjeta) == 16:
                    if tarjeta not in subes:
                        subes.append(tarjeta)
                    else:
                        print(f"La tarjeta {tarjeta} ya esta registrada")
                else:
                    print("La tarjeta pasa o no llega a los 16 digitos")
        case 2:
            if len(subes) > 0:
                for i in range(0, len(subes)):
                    saldo_tarjeta = float(input(f"Ingrese el saldo de la sube {subes[i]}: "))
                    saldo.append(saldo_tarjeta)
            else:
                print("No hay subes registradas")
        case 3:
            for i in range(0,len(subes)):
                print(f"Sube {i}: {subes[i]}")
                print(f"Saldo: {saldo[i]}")
        case 4:
            numero_sube = input("Ingrese el numero de sube que desee saber el saldo").strip(",. -")
            if numero_sube in subes:
                print(f"El saldo de la sube {numero_sube} es de: {saldo[subes.index(numero_sube)]}")
            else:
                print("No se encontro la sube")
        case 5:
            for i in range(0, len(subes)):
                if saldo[i] <= 0:
                    print(f"Sube: {subes[i]}")
                    print(f"Saldo: {saldo[i]}")
        case 6:
            numero_tarjeta = input("Ingrese el numero de tarjeta que desea buscar: ").strip(",. -")
            if numero_tarjeta in subes:
                operacion = input("Desea cargar o debitar la sube (c/d)").lower()
                if operacion == "c":
                    cantidad_credito = float(input("Ingrese el numero que desee sumar"))
                    suma = saldo[subes.index(numero_tarjeta)] + cantidad_credito
                    saldo[subes.index(numero_tarjeta)] = suma
                elif operacion == "d":
                    cantidad_credito = float(input("Ingrese el numero que desee restar"))
                    resta = saldo[subes.index(numero_tarjeta)] - cantidad_credito
                    saldo[subes.index(numero_tarjeta)] = resta
                else:
                    print("La operacion ingresada no es valida")
        case 7:
            continuar = False