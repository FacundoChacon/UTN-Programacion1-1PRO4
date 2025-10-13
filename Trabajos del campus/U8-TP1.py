#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad
with open("productos.txt", "w") as archivo:
# Se escribe cada producto en una línea del archivo
    archivo.write("Naranja,150,50\n")
    archivo.write("Uva,20,100\n")
    archivo.write("Banana,100,30\n")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open("productos.txt", "r") as archivo:
# Se lee cada línea del archivo y se procesa
    for line in archivo:
        nombre, precio, cantidad = line.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente.
with open("productos.txt", "a") as archivo:
# Se pide al usuario que ingrese un nuevo producto
    nuevo_producto = input("Ingrese un nuevo producto (nombre,precio,cantidad): ")
    archivo.write(nuevo_producto + "\n")

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.
productos = []
# Se lee el archivo y se carga cada producto en una lista de diccionarios
with open("productos.txt", "r") as archivo:
    for line in archivo:
        nombre, precio, cantidad = line.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)