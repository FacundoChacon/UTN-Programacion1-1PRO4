#punto 1
edad = input("Ingrese su edad: ")
if int(edad) >= 18:
    print("Es mayor de edad")

#punto 2    
nota = float(input("Ingrese su nota (0-10): "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#punto 3    
numero_par = int(input("Ingrese un número par: "))
if numero_par % 2 == 0:
    print(f"El número {numero_par} es par")
else:
    print(f"Ingrese un numero par")

#punto 4    
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto joven")
else:
    if edad >= 30:
        print("Adulto")

#punto 5    
contraseña = input("Ingrese la contraseña de entre 8 y 14 caracteres: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

#punto 7
frase = input("Ingrese una frase: ")
if frase[len(frase)-1] == "a" or frase[len(frase)-1] == "e" or frase[len(frase)-1] == "i" or frase[len(frase)-1] == "o" or frase[len(frase)-1] == "u":
    print(f"{frase}!")

#punto 8
nombre = input("Ingrese su nombre y una de las siguientes opciones (1,2,3): ")
opcion = int(input("1- Letras mayusculas\n2- Letras minusculas\n3- Inicial mayuscula, el resto en miusculas\n"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción incorrecta")

#punto 9    
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))
if magnitud_terremoto < 3.0:
    print("Muy leve")
elif 3.0 <= magnitud_terremoto < 4.0:
    print("Leve")
elif 4.0 <= magnitud_terremoto < 5.0:
    print("Moderado")
elif 5.0 <= magnitud_terremoto < 6.0:
    print("Fuerte")
elif 6.0 <= magnitud_terremoto < 7.0:
    print("Muy fuerte")
elif magnitud_terremoto >= 7.0:
    print("Extremo")
else:
    print("Magnitud incorrecta")

#punto 10   
hemsiferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
if hemsiferio == "N":
    if 3 <= mes <= 5:
        print("Primavera")
    elif 6 <= mes <= 8:
        print("Verano")
    elif 9 <= mes <= 11:
        print("Otoño")
    elif mes == 12 or mes == 1 or mes == 2:
        print("Invierno")
    else:
        print("Mes incorrecto")
elif hemsiferio == "S":
    if 3 <= mes <= 5:
        print("Otoño")
    elif 6 <= mes <= 8:
        print("Invierno")
    elif 9 <= mes <= 11:
        print("Primavera")
    elif mes == 12 or mes == 1 or mes == 2:
        print("Verano")
    else:
        print("Mes incorrecto")
else:
    print("Hemisferio incorrecto")
