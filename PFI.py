# Menu interactivo

listaProductos=[]

def agregar_producto():

    dic_producto={}

    nombre=input("Nombre producto: ")
    cantidad=int(input("Cantidad: "))

    dic_producto[nombre]=cantidad

    listaProductos.append(dic_producto)


def mostrar_producto():

    for elemento in listaProductos:
        for key, value in elemento.items():
            print(f"Nombre: {key}\n Cantidad: {value}")


print("¡BIENVENIDO USUARIO!\n\n")

print("SELECCIONE LA OPCION QUE DESEE UTILIZAR: " +
      "1- AGREGAR UN PRODUCTO " +
      "2 - MOSTRAR UN PRODUCTO " +
      "3 - ELIMINAR UN PRODUCTO " +
      "4 - EDITAR UN PRODUCTO " +
      "5 - SALIR")

opcion = int(input("Inserte una opción: "))

while opcion != 5:

    if opcion == 1:
        agregar_producto()
        print("\nProducto agregado con éxito\n\n")
    elif opcion == 2:
        mostrar_producto()
    elif opcion == 5:
        break
    else:
        print("\n¡Selecciona una opción correcta!\n")
    opcion = int(input("\n\nInserte una opción: "))
    