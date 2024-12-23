README: Sistema de Inventario en Consola

Descripción General

Este es un sistema básico de inventario desarrollado en Python, utilizando una base de datos SQLite para almacenar los productos. La aplicación se ejecuta en la consola y permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los productos, además de generar reportes de bajo stock.

Requisitos

Python 3.7 o superior

Módulo sqlite3 (incluido por defecto en Python)

Instalación

Clona este repositorio o descarga el archivo inventario.py.

Asegúrate de tener Python 3 instalado en tu sistema.

Ejecución de la Aplicación

Abre una terminal o línea de comandos.

Navega al directorio donde se encuentra el archivo inventario.py.

Ejecuta el archivo con el comando:

python inventario.py

Sigue las instrucciones en la consola para interactuar con el sistema.

Funcionalidades

1. Agregar un Producto

Permite registrar un nuevo producto en el inventario, solicitando:

Nombre

Descripción

Cantidad

Precio

Categoría

2. Mostrar Productos

Lista todos los productos registrados en el inventario, mostrando:

ID

Nombre

Descripción

Cantidad

Precio

Categoría

3. Eliminar un Producto

Elimina un producto especificado por su ID.

4. Editar Cantidad de un Producto

Permite modificar la cantidad de un producto registrado, identificándolo por su ID.

5. Buscar un Producto

Busca productos cuyo nombre coincida parcialmente con el término ingresado.

6. Generar Reporte de Bajo Stock

Genera un listado de productos cuya cantidad es menor o igual a un límite especificado por el usuario.

7. Salir

Termina la ejecución de la aplicación.

Estructura del Código

El archivo inventario.py incluye las siguientes funciones principales:

conexion_bbdd(): Crea la tabla productos si no existe.

agregar_producto(): Agrega un producto nuevo.

mostrar_datos(): Muestra todos los productos registrados.

eliminar_producto(): Elimina un producto por su ID.

actualizar_cantidad_producto(): Actualiza la cantidad de un producto.

buscar_producto(): Busca productos por nombre.

bajo_stock(): Genera un reporte de productos con cantidad baja.

main(): Controla la interacción del usuario y las opciones del menú.

Notas Adicionales

Si la base de datos ya existe, la función conexion_bbdd() no volverá a crear la tabla.

Para reiniciar la base de datos, puedes usar la función eliminar_tabla().

Mejoras Futuras

Implementar validaciones adicionales para evitar entradas incorrectas.

Agregar manejo de excepciones más detallado.

Crear un archivo de configuración para los límites de bajo stock predeterminados.

Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para más información
