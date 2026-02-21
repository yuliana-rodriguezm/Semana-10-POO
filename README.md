# Inventario - Tienda de Maquillaje

Este proyecto es un sistema de gestión de inventarios desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y una arquitectura modular con modelos y servicios.

Permite gestionar productos cosméticos como maquillaje y skincare mediante un menú interactivo en consola y un archivo inventario_service.txt en el que se van almacenando los productos
agregados en consola.

### Manejo de archivos en Python
El sistema utiliza archivos de texto para almacenar el inventario, implementando la función `open()` en conjunto con el administrador de contexto `with`.  
El uso de `with` permite garantizar el cierre automático del archivo, evitando pérdidas de datos y fugas de recursos.

Se emplean los modos:
- `w` para sobrescribir el archivo con los datos actualizados.
- `r` para leer los productos almacenados al iniciar el programa.

### Manejo de excepciones
Se implementaron bloques `try-except` para capturar errores comunes como:
- `FileNotFoundError`, cuando el archivo no existe.
- `PermissionError`, cuando no hay permisos de escritura.
- `ValueError`, cuando el usuario ingresa datos incorrectos.

### Funcionamiento del código
- Abrir la carpeta del proyecto en Visual Studio Code o PyCharm
- Ejecutar el archivo principal:
```bash
python main.py
