import random
jugador_gana = 0
bot_gana = 0
while jugador_gana < 3 and bot_gana < 3:
    jugada=True
    while(jugada==True):
        opcion=input("Ingrese una opcion (1: Piedra, 2: Papel, 3: Tijera): ")
        bot = random.randint(1,3)
        if opcion == "1":
            print("Elegiste Piedra")
            if bot == 1:
                print("\nEl bot eligio Piedra, es un empate")
            elif bot == 2:
                print("\nEl bot eligio Papel, perdiste")
                jugada=False
                bot_gana = bot_gana + 1
                print(f"")
            else:
                print("\nEl bot eligio Tijera, ganaste")
                jugador_gana = jugador_gana + 1
                jugada=False
                print(f"puntos Jugador: {jugador_gana} - Puntos Bot: {bot_gana}")
        elif opcion == "2":
            print("Elegiste Papel")
            if bot == 1:
                print("\nEl bot eligio Piedra, ganaste")
                jugador_gana = jugador_gana + 1
                jugada=False
                print(f"puntos Jugador: {jugador_gana} - Puntos Bot: {bot_gana}")
            elif bot == 2:
                print("\nEl bot eligio Papel, es un empate")
            else:
                print("\nEl bot eligio Tijera, perdiste")
                bot_gana = bot_gana + 1
                jugada=False
                print(f"puntos Jugador: {jugador_gana} - Puntos Bot: {bot_gana}")
        elif opcion == "3":
            print("Elegiste Tijera")
            if bot == 1:
                print("\nEl bot eligio Piedra, perdiste")
                bot_gana = bot_gana + 1
                jugada=False
                print(f"puntos Jugador: {jugador_gana} - Puntos Bot: {bot_gana}")
            elif bot == 2:
                print("\nEl bot eligio Papel, ganaste")
                jugador_gana = jugador_gana + 1
                jugada=False
                print(f"Puntos Jugador: {jugador_gana} - Puntos Bot: {bot_gana}")
            else:
                print("\nEl bot eligio Tijera, es un empate")
    if jugador_gana == 3:
        print("\nFelicitaciones, ganaste el juego!")
    elif bot_gana == 3:
        print("\nEl bot gano el juego, mejor suerte la proxima vez!")
