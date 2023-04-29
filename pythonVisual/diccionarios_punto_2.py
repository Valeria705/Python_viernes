# punto N° 2
def agregar_producto(diccionario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    descripcion = input("Ingrese la descripción del producto: ")
    diccionario[nombre] = {"Precio": precio, "Descripción": descripcion}
    print("Producto agregado con éxito.")

def imprimir_productos(diccionario):
    print("PRODUCTOS")
    print("Nombre\tPrecio\tDescripción")
    for nombre, datos in diccionario.items():
        print(f"{nombre}\t{datos['Precio']}\t{datos['Descripción']}")


nombre_diccionario = input("Ingrese el nombre del diccionario: ")

diccionario_productos = {}

while True:
    print("\nMENU")
    print("1. Agregar producto")
    print("2. Imprimir productos")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_producto(diccionario_productos)
    elif opcion == "2":
        imprimir_productos(diccionario_productos)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")

print(f"El diccionario de productos {nombre_diccionario} ha sido cerrado.")
