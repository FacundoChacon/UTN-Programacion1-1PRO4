corrimiento=int(input("Ingrese el corrimiento: "))
mensaje_encriptado=""
abc_minuscula = "abcdefghijklmnñopqrstuvwxyz"
abc_mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for i in range(0,5):
    entrada=input("Ingrese el mensaje a encriptar: ")
    for letra in entrada:
        if letra in abc_minuscula:
            nueva_letra = abc_minuscula[(abc_minuscula.index(letra) + corrimiento) %27]
            mensaje_encriptado += nueva_letra
        elif letra in abc_mayuscula:
            nueva_letra = abc_mayuscula[(abc_mayuscula.index(letra) + corrimiento) %27]
            mensaje_encriptado = nueva_letra
        else:
            mensaje_encriptado = letra
    print(mensaje_encriptado)
    mensaje_encriptado = ""