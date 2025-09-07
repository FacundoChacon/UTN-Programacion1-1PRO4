import random
from statistics import mean, median, mode
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(f"{i}\n")

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
num = input("Ingrese un número entero: ")
print(f"El número {num} tiene {len(num)} dígitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = 0
if num1 > num2:
    num1, num2 = num2, num1
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num1 + 1, num2):
        suma += i
print(f"La suma de los números entre {num1} y {num2} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
suma = 0
while True:
    num = int(input("Ingrese un número entero (0 para finalizar): "))
    if num == 0:
        break
    suma += num
print(f"La suma total es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
numero_aleatorio = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Ingrese el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_aleatorio:
        break
print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range(0, 101):
    if i % 2 == 0:
        print(f"{i}\n")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
num = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print(f"La suma de los números entre 0 y {num} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        print("El número es cero")
print(f"Números pares: {pares}\nNúmeros impares: {impares}\nNúmeros negativos: {negativos}\nNúmeros positivos: {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
media = 0
for i in range(100):
    num = float(input("Ingrese un número entero: "))
    media += num
media = media / 100
print(f"La media de los números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = input("Ingrese un número entero: ")
for i in range(len(num),0,-1):
    print(f"{num[i-1]}", end="")

