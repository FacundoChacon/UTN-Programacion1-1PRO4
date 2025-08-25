dia, DD_MM = input("Ingrese el día de la semana y la fecha actual (día, DD/MM): ").strip().split(",")
dia = dia.lower()
def semana_dias(dia:str):
    if dia == "lunes" or dia == "martes" or dia == "miércoles" or dia == "miercoles" or dia == "jueves" or dia == "viernes" or dia == "sábado" or dia == "sabado" or dia == "domingo":
        return True
    else:
        return False
if semana_dias(dia) == False:
    print("Error: Día de la semana inválido.")
    exit()
else:
    pass

DD, MM = DD_MM.strip().split("/")
DD = int(DD)
MM = int(MM)

if DD>=1 and DD<=31 and MM>=1 and MM<=12:
    pass
else:
    print("Error: Fecha inválida.")
    exit()
print(f"DIA: {dia} \n DD: {DD} \n MM: {MM}")

if dia == "lunes":
    print("Nivel inicial.")
    examenes = input("¿Se tomaron exámenes? (si/no): ").strip().lower()
    if examenes == "si":
        aprobados = int(input("Cantidad de alumnos aprobados: "))
        desaprobados = int(input("Cantidad de alumnos no aprobados: "))
        total = aprobados + desaprobados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            porcentaje = int(porcentaje)
            print(f"Porcentaje de aprobados: {porcentaje}%")
            
elif dia == "martes":
    print("Nivel intermedio.")
    examenes = input("¿Se tomaron exámenes? (si/no): ").strip().lower()
    if examenes == "si":
        aprobados = int(input("Cantidad de alumnos aprobados: "))
        desaprobados = int(input("Cantidad de alumnos no aprobados: "))
        total = aprobados + desaprobados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            print(f"Porcentaje de aprobados: {porcentaje}%")
            
elif dia == "miércoles" or dia == "miercoles":
    print("Nivel avanzado.")
    examenes = input("¿Se tomaron exámenes? (si/no): ").strip().lower()
    if examenes == "si":
        aprobados = int(input("Cantidad de alumnos aprobados: "))
        desaprobados = int(input("Cantidad de alumnos no aprobados: "))
        total = aprobados + desaprobados
        if total > 0:
            porcentaje = (aprobados / total) * 100
            print(f"Porcentaje de aprobados: {porcentaje}%")
            
elif dia == "jueves":
    print("Práctica hablada.")
    asistencia = int(input("Porcentaje de asistencia (0-100): ").strip())
    if asistencia>50:
        print("Asistió la mayoria.")
    else:
        print("No asistió la mayoria.")
        
elif dia == "viernes":
    print("Inglés para viajeros.")
    if (DD == 1 and MM == 1) or (DD == 1 and MM ==7):
        print("Comienzo del nuevo ciclo")
        alumnos = int(input("Cantidad de alumnos del nuevo ciclo: "))
        arancel_alumnos = (4/100) * 20000
        total_recaudado = alumnos * arancel_alumnos
        print(f"Total recaudado: ${total_recaudado}")
    else:
        print("No es comienzo de nuevo ciclo.")