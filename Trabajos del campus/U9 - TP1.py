# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:      # Caso base
        return 1
    else:                     # Caso recursivo
        return n * factorial(n - 1)


def mostrar_factoriales():
    num = int(input("Ingrese un número para calcular los factoriales hasta ese valor: "))
    for i in range(1, num + 1):
        print(f"{i}! = {factorial(i)}")


# 2) Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:                 # Casos base
        return n
    else:                      # Caso recursivo
        return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci():
    n = int(input("Ingrese la posición máxima para la serie de Fibonacci: "))
    print("Serie de Fibonacci:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()


# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:          # Caso base
        return 1
    else:                       # Caso recursivo
        return base * potencia(base, exponente - 1)


def probar_potencia():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")


# 4) Conversión decimal a binario recursiva
def decimal_a_binario(n):
    if n == 0:                  # Caso base
        return ""
    else:                       # Caso recursivo
        return decimal_a_binario(n // 2) + str(n % 2)


def probar_decimal_a_binario():
    n = int(input("Ingrese un número decimal: "))
    if n == 0:
        print("Binario: 0")
    else:
        print("Binario:", decimal_a_binario(n))


# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:       # Caso base
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:                       # Caso recursivo
        return es_palindromo(palabra[1:-1])


def probar_palindromo():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")


# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:                  # Caso base
        return n
    else:                       # Caso recursivo
        return n % 10 + suma_digitos(n // 10)


def probar_suma_digitos():
    n = int(input("Ingrese un número entero positivo: "))
    print("Suma de los dígitos:", suma_digitos(n))


# 7) Contar bloques (pirámide)
def contar_bloques(n):
    if n == 1:                  # Caso base
        return 1
    else:                       # Caso recursivo
        return n + contar_bloques(n - 1)


def probar_contar_bloques():
    n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    print("Total de bloques necesarios:", contar_bloques(n))


# 8) Contar ocurrencias de un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:             # Caso base
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


def probar_contar_digito():
    numero = int(input("Ingrese un número: "))
    digito = int(input("Ingrese el dígito a contar: "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")


# ==========================================
# MENÚ PRINCIPAL PARA PROBAR LOS EJERCICIOS
# ==========================================
def menu():
    while True:
        print("\n===== PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD =====")
        print("1) Factoriales")
        print("2) Serie de Fibonacci")
        print("3) Potencia")
        print("4) Decimal a Binario")
        print("5) Palíndromo")
        print("6) Suma de dígitos")
        print("7) Contar bloques (pirámide)")
        print("8) Contar dígito en un número")
        print("9) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_factoriales()
        elif opcion == "2":
            mostrar_fibonacci()
        elif opcion == "3":
            probar_potencia()
        elif opcion == "4":
            probar_decimal_a_binario()
        elif opcion == "5":
            probar_palindromo()
        elif opcion == "6":
            probar_suma_digitos()
        elif opcion == "7":
            probar_contar_bloques()
        elif opcion == "8":
            probar_contar_digito()
        elif opcion == "9":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# EJECUCIÓN DEL MENÚ
if __name__ == "__main__":
    menu()
