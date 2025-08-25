print(f"TP 1 1PROG4")

#punto 1
print("Hola Mundo")

#punto 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#punto 3    
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su ciudad de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#punto 4    
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio
print(f"El área del círculo es: {area} y su perímetro es: {perimetro}")

#punto 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas.")

#punto 6
numero_tabla = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero_tabla}:")
print(f"{numero_tabla} x 1 = {numero_tabla * 1}")
print(f"{numero_tabla} x 2 = {numero_tabla * 2}")
print(f"{numero_tabla} x 3 = {numero_tabla * 3}")
print(f"{numero_tabla} x 4 = {numero_tabla * 4}")
print(f"{numero_tabla} x 5 = {numero_tabla * 5}")
print(f"{numero_tabla} x 6 = {numero_tabla * 6}")
print(f"{numero_tabla} x 7 = {numero_tabla * 7}")
print(f"{numero_tabla} x 8 = {numero_tabla * 8}")
print(f"{numero_tabla} x 9 = {numero_tabla * 9}")
print(f"{numero_tabla} x 10 = {numero_tabla * 10}")

#punto 7
print(f"Ingrese dos numeros distintos al cero para calcular su suma, resta, multiplicación y división.")
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")

#punto 8    
print(f"Ingrese su altura en metros y su peso en kilogramos para calcular su IMC.")
imc_altura = float(input("Ingrese su altura en metros: "))
imc_peso = float(input("Ingrese su peso en kilogramos: "))
imc = imc_peso / (imc_altura ** 2)
print(f"Su IMC es: {imc}")

#punto 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5 * celsius) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#punto 10
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres números es: {promedio}")