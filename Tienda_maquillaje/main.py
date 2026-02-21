# SISTEMA DE INVENTARIO - TIENDA DE MAQUILLAJE

from servicios.inventario_service import InventarioService

def mostrar_menu():
    print("""
====================================
   TIENDA DE MAQUILLAJE - INVENTARIO
====================================
1. Agregar producto
2. Mostrar inventario
3. Buscar por nombre
4. Buscar por categoría
5. Actualizar producto
6. Eliminar producto
0. Salir
====================================
""")

def main():
    inventario = InventarioService()

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                inventario.agregar_producto()
            elif opcion == 2:
                inventario.listar_productos()
            elif opcion == 3:
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                for p in resultados:
                    print(p)
            elif opcion == 4:
                cat = input("Categoría: ")
                resultados = inventario.buscar_por_categoria(cat)
                for p in resultados:
                    print(p)
            elif opcion == 5:
                inventario.actualizar_producto()
            elif opcion == 6:
                inventario.eliminar_producto()
            elif opcion == 0:
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")

        except ValueError:
            print("Ingrese un número")

if __name__ == "__main__":
    main()
