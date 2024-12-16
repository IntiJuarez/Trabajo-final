import sqlite3 


#-----------------------Conexión a la base de datos-------------------------

def conexion_bbdd():

    mi_conexion = sqlite3.connect("inventario")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute(
        '''
            CREATE TABLE inventario(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) NOT NULL,
            DESCRIPCION VARCHAR(100) NOT NULL,
            CANTIDAD INTEGER NOT NULL,
            PRECIO FLOAT NOT NULL,
            CATEGORIA VARCHAR(50) NOT NULL
            )
        '''
    )

    mi_conexion.commit()

    mi_conexion.close()


#-----------------------Función para agregar un producto-------------------------
def agregar_producto():

    mi_conexion = sqlite3.connect("inventario")

    mi_cursor = mi_conexion.cursor()

    nombre = input("Ingrese el nombre del producto: ")
    
    descripcion = input("Descripción: ")

    cantidad = int(input("Cantidad: "))

    precio = float(input("Precio: "))

    categoria = input("Categoría: ")

    mi_cursor.execute("INSERT INTO inventario (nombre, descripcion, cantidad , precio, categoria) VALUES (?,?,?,?,?))", (nombre, descripcion, cantidad, precio, categoria))

    mi_conexion.commit()



#-----------------------Función para editar un producto-------------------------
def actualizar_cantidad_producto():
    
    mi_conexion = sqlite3.connect("inventario")

    mi_cursor = mi_conexion.cursor()

    try:

        #Obtengo una lista de tuplas de la tabla inventario y muestro los productos existentes
        mi_cursor.execute("SELECT ID, NOMBRE, CANTIDAD FROM inventario")
        productos = mi_cursor.fetchall()

        if not productos:
            print("No hay productos registrados.")
            return
        
        print("Lista de productos:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad actual: {producto[2]}")
        
        #Solicito ID del producto
        idProducto = int(input("Inserte el ID del producto que desea modificar: "))

        #Verificar existencia del producto
        mi_cursor.execute("SELECT CANTIDAD FROM inventario WHERE ID = ?", (idProducto))
        producto = mi_cursor.fetchone()

        if producto is None:
            print("Producto no registrado.")
            return
        
        #Solicitar nueva cantidad
        nueva_cantidad = int(int("Ingrese nueva cantidad: "))

        mi_cursor.execute("UPDATE inventario SET CANTIDAD = ? WHERE ID = ? ",
                          (nueva_cantidad, idProducto))
        
        mi_conexion.commit()
        print("Cantidad modificado exitosamente.")

    except ValueError:
        print("Error, ingresar un número válido.")

    finally:
        mi_conexion.close()



#-----------------------Función para mostrar los productos-------------------------
def mostrar_datos():

    mi_conexion = sqlite3.connect("inventario")
    mi_cursor = mi_conexion.cursor()

    try:
        #Obtengo los productos
        mi_cursor.execute("SELECT * FROM inventario")
        productos = mi_cursor.fetchall()

        if not productos:
            print("No hay productos registrados")
            return
        
        #mostrar productos:
        print("Lista de productos en el inventario:")
        print(f"{'ID':<5} {'Nombre':<15} {'Descripción':<25} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 80)

        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<15} {producto[2]:<25} {producto[3]:<10} {producto[4]:<10.2f} {producto[5]:<15}")

    except Exception as e:
        print(f"Error al mostrar los productos: {e}")
    finally:
        mi_conexion.close()


#-----------------------Función para eliminar un producto-------------------------
def eliminar_producto():

    mi_conexion = sqlite3.connect("inventario")
    mi_cursor = mi_conexion.cursor()

    try:
        mi_cursor.execute("SELECT ID, NOMBRE, CANTIDAD FROM inventario")
        productos = mi_cursor.fetchall()

        if not productos:
            print("No hay productos registrados.")
            return

        print("Lista de productos.")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad actual: {producto[2]}")

        #Solicito ID del producto
        idProducto = int(input("Inserte el ID del producto que desea modificar: "))

        #Verificar existencia del producto
        mi_cursor.execute("SELECT CANTIDAD FROM inventario WHERE ID = ?", (idProducto))
        producto = mi_cursor.fetchone()

        if producto is None:
            print("Producto no existente.")
            return
        
        mi_cursor.execute("DELETE FROM inventario WHERE ID = ?",(idProducto))
        mi_conexion.commit()
        print("Producto eliminado con éxito.")

    finally:
        mi_conexion.close()

#-----------------------Función para buscar un producto-------------------------
def buscar_producto():
    mi_conexion = sqlite3.connect("inventario")
    mi_cursor = mi_conexion.cursor()

    try:
        nombre_producto = input("Ingresar el producto que desee buscar: ")
        #Consulta para buscar producto:
        mi_cursor.execute("SELECT * FROM inventario WHERE NOMBRE LIKE ?", (f"%{nombre_producto}%",))
        productos = mi_cursor.fetchall()

        if not productos:
            print("No se han encontrado productos con el nombre ingresado.")
            return
        
        print(f"Productos que coinciden con '{nombre_producto}':")
        print(f"{'ID':<5} {'Nombre':<15} {'Descripción':<25} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 80)
        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<15} {producto[2]:<25} {producto[3]:<10} {producto[4]:<10.2f} {producto[5]:<15}")

    except Exception as e:
        print(f"Error al buscar producto: {e}")
    finally:
        mi_conexion.close()

#-----------------------Reporte de bajo stock-------------------------
def bajo_stock():
    mi_conexion = sqlite3.connect("inventario")
    mi_cursor = mi_conexion.cursor()

    try:
        limite_stock = int(input("Ingrese el límite de cantidad para generar reporte: "))
        
        mi_cursor.execute("SELECT * FROM inventario WHERE CANTIDAD <= ?", (limite_stock))
        productos = mi_cursor.fetchall()

        if not productos:
            print(f"No se ha encontrado productos con una cantidad inferior o igual a {limite_stock}.")
            return
        
        print(f"Reporte de productos con bajo stock (cantidad <= {limite_stock}):")
        print(f"{'ID':<5} {'Nombre':<15} {'Descripción':<25} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 80)
        for producto in productos:
            print(f"{producto[0]:<5} {producto[1]:<15} {producto[2]:<25} {producto[3]:<10} {producto[4]:<10.2f} {producto[5]:<15}")

    except ValueError:
        print("Ingrese un valor válido.")
    except Exception as e:
        print(f"Error al generar reporte: {e}")
    finally:
        mi_conexion.close()

