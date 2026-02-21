# MODELO: ProductoCosmetico
# Representa un producto cosmético del inventario

class ProductoCosmetico:

    # CONSTRUCTOR
    def __init__(self, id_producto, nombre, cantidad, precio, categoria):
        self.__id_producto = id_producto    #identificador único del producto
        self.__nombre = nombre              #nombre del producto
        self.__cantidad = cantidad          #cantidad disponible en stock
        self.__precio = precio              #precio del producto
        self.__categoria = categoria        #categoría (maquillaje, skincare)

    # GETTERS
    #Permite acceder a los atributos privados del producto
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def get_categoria(self):
        return self.__categoria

    # SETTERS
    # Permite modificar los atributos privados del producto de manera controlada
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("Cantidad no válida")

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("Precio inválido")

    def set_categoria(self, categoria):
        self.__categoria = categoria

    # Método para representar el producto como una cadena de texto
    def __str__(self):
        return f"[{self.__id_producto}] {self.__nombre} | Stock: {self.__cantidad} | Precio: ${self.__precio:.2f} | Categoría: {self.__categoria}"
