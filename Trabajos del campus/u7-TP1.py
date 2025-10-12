#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios. 
lista_frutas=list(precios_frutas.keys())
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
agenda={}
for i in range(5):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input("Ingrese el número del contacto: ")
    agenda[nombre]=numero
print(agenda)
consulta=input("Ingrese el nombre del contacto que desea consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"El contacto {consulta} no existe en la agenda")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase=input("Ingrese una frase: ")
palabras=frase.split()
palabras_unicas=set(palabras)
print(f"Palabras únicas: {palabras_unicas}")
contador_palabras={}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(f"Contador de palabras: {contador_palabras}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.
alumnos={}
for i in range(3):
    nombre=input("Ingrese el nombre del alumno: ")
    notas=()
    for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas += (nota,)
    alumnos[nombre]=notas
for alumno, notas in alumnos.items():
    promedio=sum(notas)/len(notas)
    print(f"El promedio de {alumno} es {promedio}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}
aprobados_ambos = parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {aprobados_ambos}")
aprobados_solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {aprobados_solo_uno}")
aprobados_al_menos_uno = parcial1 | parcial2
print(f"Estudiantes que aprobaron al menos un parcial: {aprobados_al_menos_uno}")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.
stock_productos={}
while True:
    accion = input("Acción (consultar/agregar/nuevo/salir): ").lower()
    if accion == 'salir':
        break
    producto = input("Producto: ") if accion != 'salir' else ""
    if accion == 'consultar':
        print(f"Stock de {producto}: {stock_productos.get(producto, 'No existe')}")
    elif accion == 'agregar':
        if producto in stock_productos:
            stock_productos[producto] += int(input("Unidades a agregar: "))
            print(f"Nuevo stock: {stock_productos[producto]}")
        else:
            print("No existe")
    elif accion == 'nuevo':
        if producto not in stock_productos:
            stock_productos[producto] = int(input("Unidades iniciales: "))
            print("Producto agregado")
        else:
            print("Ya existe")
    else:
        print("Acción no reconocida.")
print(stock_productos)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda_eventos = {}
while True:
    accion = input("Acción (agregar/consultar/salir): ").lower()
    if accion == "salir":
        break
    if accion == "agregar":
        dia = input("Ingrese el día: ")
        hora = input("Ingrese la hora: ")
        evento = input("Ingrese el evento: ")
        agenda_eventos[(dia, hora)] = evento
        print("Evento agregado.")
    elif accion == "consultar":
        dia = input("Ingrese el día: ")
        hora = input("Ingrese la hora: ")
        evento = agenda_eventos.get((dia, hora))
        if evento:
            print(f"Evento en {dia} a las {hora}: {evento}")
        else:
            print("No hay evento en ese día y hora.")
    else:
        print("Acción no reconocida.")
print(agenda_eventos)

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)
