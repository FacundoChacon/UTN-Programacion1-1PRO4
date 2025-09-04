#Ejercicio 1: Bucle for para números pares
for numero in range(2, 21, 2):
    print(numero)
#¿Cómo modificarías el código para imprimir solo impares?
# Poniendo un condicional que imprima los numeros que "n % 2 != 0" o haciendo que empiece con 1 y paso 2
#¿Qué pasa si el rango fuera de 2 a 20 con paso 3?
# Se imprimen los numeros 2, 5, 8, 11, 14, 17, 20

# Ejercicio 2: Bucle while con suma acumulativa
suma = 0
while suma < 100:
    num = int(input("Ingrese un número para sumar: "))
    suma = suma + num
#¿Qué ocurre si el primer número ingresado es mayor que 100?
# El bucle no se ejecuta y no se pide ningun numero
#¿Cómo evitarías errores si el usuario ingresa texto?
# Usando un try y except para manejar el error

#Ejercicio 3: Filtrar palabras por letra inicial
palabra = ["manzana", "banana", "cereza", "durazno", "kiwi", "mango", "naranja", "anana"]
for p in palabra:
    if p.lower().startswith("a"):
        print(p)
#¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también se cuente)?
# Usando .lower() o .upper() en la lista y en la letra a comparar
#¿Qué método de strings es útil para esto?
# .lower() o .upper() y .startswith()

#Ejercicio 4: Tabla de multiplicar del 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
#¿Cómo adaptarías el código para que el usuario elija la tabla?
# Agregaria una variable con input que solicite al usuario que ingrese el numero de la tabla
# n = int(input("Ingrese el número de la tabla que desea: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
#¿Qué estructura usarías para almacenar los resultados?
# Usaria una lista con el nombre "resultados" y en cada iteracion del for iria agregando los resultados con endd()

# Ejercicio 5: Contador de vocales
frase = input("Ingrese una frase: ").lower()
for i in frase:
    frase = frase.replace(" ", "")
suma = 0
for letra in frase:
    if letra in "aeiou":
        suma += 1
print(f"La frase tiene {suma} vocales")
#¿Cómo manejarías las vocales acentuadas (á, é)?
# Agregandole "áéíóú" en el condicional del if
#¿Qué estructura de datos te ayudaría a optimizar el código?
# Usaria un range o una lista para las vocales

# Ejercicio 6: Números repetidos en una lista
nums = [1,2,5,2,3,1,5,6,4,3]
repetidos = []
for i in nums:
    if i in nums:
        if i not in repetidos:
            repetidos.append(i)
            print(f"El número {i} está repetido")
#¿Por qué es importante mantener el orden de aparición?
# Para saber el orden en el que los numeros se repitieron
#¿Cómo resolverías esto sin usar estructuras adicionales?
# Usando sets, ya que no permiten elementos repetidos

# Ejercicio 7: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#¿Por qué el orden de los condicionales es crucial aquí?
# Porque si en el caso de que sea un multiplo de 3 y 5 a la vez no se cumple el primer if, no se va a imprimir "FizzBuzz". No cumple con la consigna
#¿Cómo extenderías el juego a otros números (ej: 7 → "Bazz")?
# Agregando otro condicional elif que verifique si es multiplo de 7 y en ese caso imprima "Bazz"
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         print("FizzBuzzBazz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 7 == 0:
#         print("Bazz")
#     else:
#         print(i)

#Ejercicio 8: Frecuencia de palabras
texto = input("Ingrese un texto: ").lower()
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print(frecuencia.keys())
print(frecuencia.values())
#¿Cómo ignorarías signos de puntuación (ej: "hola," vs "hola")?
# Usando el metodo .strip() para eliminar los signos especiales
#¿Qué método de strings ayuda a separar palabras?
# .split()

#Ejercicio 9: Filtrar consonantes
palabra = input("Ingrese una palabra: ").lower()
consonantes = ""
for letra in palabra:
    if letra not in "aeiou":
        consonantes += letra
print(consonantes)
#¿Cómo manejarías las mayúsculas/minúsculas?
# Usando .lower() o .upper() en la palabra ingresada
#¿Qué estructura usarías para definir las consonantes?
# Sobreescribir la variable "consonantes" en cada iteracion del for o sumandola en una nueva variable

# Ejercicio 10: Números primos
entero = int(input("Ingrese un número entero positivo: "))
print (int(entero**0.5))
if entero > 1:
    es_primo = True
    for i in range(2, int(entero**0.5) + 1):
        if entero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {entero} es primo")
    else:
        print(f"El número {entero} no es primo")
#¿Cómo optimizarías la verificación de primos?
# Verificando solo hasta la raiz cuadrada del numero con math.sqrt() o entero**0.5
#¿Qué ventaja tiene usar range(2, int(n**0.5) + 1)?
# Porque evita que se haga una cantidad innecesaria de iteraciones haciendo mas eficiente el codigo