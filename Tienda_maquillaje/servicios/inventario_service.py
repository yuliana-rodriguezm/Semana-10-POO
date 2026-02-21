# SERVICIO: Inventario de Productos Cosméticos
# Maneja CRUD y archivos
# Permite agregar, listar, buscar, actualizar y eliminar productos del inventario
# Además, guarda y carga el inventario desde un archivo de texto para persistencia de datos
import os
from modelos.producto_cosmetico import ProductoCosmetico

class InventarioService:

    def __init__(self):
        # Ruta del archivo de inventario txt
        base_dir = os.path.dirname(__file__)
        self.ruta_archivo = os.path.join(base_dir, "..", "registros", "inventario.txt")
        
        self.productos = []
        self.asegurar_archivo()   # ASEGURA QUE EL ARCHIVO EXISTA
        self.cargar_desde_archivo()   # CARGA AUTOMÁTICA

    # ================= ARCHIVOS =================

    def asegurar_archivo(self):
        # Crea la carpeta y el archivo si no existen
        carpeta = os.path.dirname(self.ruta_archivo)
        
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                pass  # Crea un archivo vacío

    def guardar_en_archivo(self):
        #Todos los productos se guardan en el archivo txt
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()}|{p.get_nombre()}|{p.get_cantidad()}|{p.get_precio()}|{p.get_categoria()}\n"
                    f.write(linea)

            print("Inventario guardado en archivo")

        except PermissionError:
            print("ERROR: Sin permisos para escribir archivo")

    # Carga los productos desde ek archivo al iniciar el programa
    # Si el archivo no existe, se crea automáticamente
    def cargar_desde_archivo(self):
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split("|")

                    if len(datos) == 5:
                        id_p = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])
                        categoria = datos[4]

                        producto = ProductoCosmetico(id_p, nombre, cantidad, precio, categoria)
                        self.productos.append(producto)

            print("Inventario cargado desde archivo")

        except FileNotFoundError:
            print("Archivo no encontrado, se creará uno nuevo")

        except Exception as e:
            print("Error al cargar archivo:", e)

    # ================= CRUD =================

    # BUSCAR POR ID
    def buscar_por_id(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                return p
        return None

    # AGREGAR PRODUCTO
    def agregar_producto(self):
        try:
            id_p = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad en stock: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría (maquillaje/skincare/etc): ")

            if self.buscar_por_id(id_p):
                print("ERROR: ID repetido")
                return

            nuevo = ProductoCosmetico(id_p, nombre, cantidad, precio, categoria)
            self.productos.append(nuevo)
            self.guardar_en_archivo()
            print("Producto agregado y guardado en archivo")

        except ValueError:
            print("ERROR: Datos inválidos")

    # LISTAR
    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío")
            return

        print("\nINVENTARIO:")
        for p in self.productos:
            print(p)

    # BUSCAR POR NOMBRE
    def buscar_por_nombre(self, texto):
        return [p for p in self.productos if texto.lower() in p.get_nombre().lower()]

    # BUSCAR POR CATEGORÍA
    def buscar_por_categoria(self, categoria):
        return [p for p in self.productos if categoria.lower() == p.get_categoria().lower()]

    # ACTUALIZAR
    def actualizar_producto(self):
        try:
            id_p = int(input("ID del producto a actualizar: "))
            producto = self.buscar_por_id(id_p)

            if not producto:
                print("Producto no encontrado")
                return

            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_categoria = input("Nueva categoría: ")

            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            producto.set_nombre(nuevo_nombre)
            producto.set_categoria(nueva_categoria)
            
            self.guardar_en_archivo()
            print("Producto actualizado y guardado")

        except ValueError:
            print("ERROR: Datos inválidos")

    # ELIMINAR
    def eliminar_producto(self):
        try:
            id_p = int(input("ID del producto a eliminar: "))
            producto = self.buscar_por_id(id_p)

            if not producto:
                print("Producto no encontrado")
                return

            self.productos.remove(producto)
            self.guardar_en_archivo()
            print("Producto eliminado")

        except ValueError:
            print("ERROR: ID inválido")
