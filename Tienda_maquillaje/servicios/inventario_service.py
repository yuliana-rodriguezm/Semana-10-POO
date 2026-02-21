# SERVICIO: Inventario de Productos Cosméticos
# Maneja CRUD y archivos

from modelos.producto_cosmetico import ProductoCosmetico

class InventarioService:

    def __init__(self):
        self.productos = []
        self.archivo = "inventario_cosmeticos.txt"
        self.cargar_archivo()   # <-- CARGA AUTOMÁTICA

    # ================= ARCHIVOS =================

    # GUARDAR EN ARCHIVO
    def guardar_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    linea = f"{p.get_id()}|{p.get_nombre()}|{p.get_cantidad()}|{p.get_precio()}|{p.get_categoria()}\n"
                    f.write(linea)

            print("Inventario guardado en archivo")

        except PermissionError:
            print("ERROR: Sin permisos para escribir archivo")

    # CARGAR ARCHIVO
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
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
            self.guardar_archivo()
            print("Producto agregado y guardado en archivo")

        except ValueError:
            print("Datos inválidos")

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

            producto.set_cantidad(nueva_cantidad)
            producto.set_precio(nuevo_precio)
            self.guardar_archivo()

            print("Producto actualizado y guardado")

        except ValueError:
            print("Datos inválidos")

    # ELIMINAR
    def eliminar_producto(self):
        try:
            id_p = int(input("ID del producto a eliminar: "))
            producto = self.buscar_por_id(id_p)

            if not producto:
                print("Producto no encontrado")
                return

            self.productos.remove(producto)
            self.guardar_archivo()
            print("Producto eliminado del inventario y archivo")

        except ValueError:
            print("ID inválido")
