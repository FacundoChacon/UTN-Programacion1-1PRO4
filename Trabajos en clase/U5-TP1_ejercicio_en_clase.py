import random

# 1. Generar cartón 5x5 con números aleatorios entre 1 y 50, sin repetirse
numeros_carton = random.sample(range(1, 51), 25)
carton = [numeros_carton[i*5:(i+1)*5] for i in range(5)]

print("Cartón inicial:")
for carton_fila in carton:
    print(carton_fila)

numeros_sorteados = set()
while True:
    # 3. Sortear número al azar entre 1 y 50, uno por uno
    while True:
        numero = random.randint(1, 50)
        if numero not in numeros_sorteados:
            numeros_sorteados.add(numero)
            break
    print(f"Número sorteado: {numero}")
    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True
    if encontrado:
        print("¡El número está en el cartón! Se reemplazó por 0.")
    else:
        print("El número no aparece en el cartón.")

    print("Cartón actualizado:")
    for carton_fila in carton:
        print(carton_fila)

    for fila in carton:
        if all(num == 0 for num in fila):
            print("¡Línea!")
    if all(num == 0 for fila in carton for num in fila):
        print("¡Bingo! El cartón está completo en 0.")
        break
