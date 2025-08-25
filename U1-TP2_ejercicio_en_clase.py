print("Ejercicio 1:" )
print(f"Ingrese el monto total de la cuenta: ")
monto = float(input())

propina10 = monto * 0.10
propina15 = monto * 0.15
cuenta_final = monto + propina10
cuenta_final15 = monto + propina15
print(f"monto = {monto}")
print(f"propina sugerida(10%) = {propina10}")
print(f"total a pagar = {cuenta_final}")
print(f"propina sugerida(15%) = {propina15}")
print(f"total a pagar = {cuenta_final15}")