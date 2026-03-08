from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    En main.py solo colocamos la interacción con el usuario y la ejecución,
    pero NO la lógica del negocio.
    """
    print("\n" + "=" * 50)
    print(" SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL ")
    print("=" * 50)
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por título")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoría")
    print("10. Listar libros prestados a un usuario")
    print("11. Listar libros disponibles")
    print("12. Listar usuarios")
    print("0. Salir")
    print("=" * 50)


def mostrar_libros(lista_libros):
    """
    Función auxiliar para imprimir libros de forma ordenada.
    """
    if not lista_libros:
        print("No hay libros para mostrar.")
        return

    for libro in lista_libros:
        print(libro)


def mostrar_usuarios(lista_usuarios):
    """
    Función auxiliar para imprimir usuarios de forma ordenada.
    """
    if not lista_usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in lista_usuarios:
        print(usuario)


def cargar_datos_prueba(servicio):
    """
    Datos de ejemplo para demostrar el funcionamiento del sistema.
        """
    servicio.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "ISBN001")
    servicio.anadir_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "ISBN002")
    servicio.anadir_libro("1984", "George Orwell", "Distopía", "ISBN003")

    servicio.registrar_usuario("Ana", "U001")
    servicio.registrar_usuario("Carlos", "U002")


def main():
    """
    Punto de entrada del programa.

    Importante:
    - Aquí se crea el servicio.
    - Aquí se controla el menú.
    - La lógica real está delegada a BibliotecaServicio.
    """
    servicio = BibliotecaServicio()

    # Datos de ejemplo para facilitar pruebas
    cargar_datos_prueba(servicio)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- Añadir libro ---")
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            categoria = input("Categoría: ").strip()
            isbn = input("ISBN: ").strip()

            exito, mensaje = servicio.anadir_libro(titulo, autor, categoria, isbn)
            print(mensaje)

        elif opcion == "2":
            print("\n--- Quitar libro ---")
            isbn = input("ISBN del libro a quitar: ").strip()

            exito, mensaje = servicio.quitar_libro(isbn)
            print(mensaje)

        elif opcion == "3":
            print("\n--- Registrar usuario ---")
            nombre = input("Nombre del usuario: ").strip()
            id_usuario = input("ID del usuario: ").strip()

            exito, mensaje = servicio.registrar_usuario(nombre, id_usuario)
            print(mensaje)

        elif opcion == "4":
            print("\n--- Dar de baja usuario ---")
            id_usuario = input("ID del usuario: ").strip()

            exito, mensaje = servicio.dar_baja_usuario(id_usuario)
            print(mensaje)

        elif opcion == "5":
            print("\n--- Prestar libro ---")
            id_usuario = input("ID del usuario: ").strip()
            isbn = input("ISBN del libro: ").strip()

            exito, mensaje = servicio.prestar_libro(id_usuario, isbn)
            print(mensaje)

        elif opcion == "6":
            print("\n--- Devolver libro ---")
            id_usuario = input("ID del usuario: ").strip()
            isbn = input("ISBN del libro: ").strip()

            exito, mensaje = servicio.devolver_libro(id_usuario, isbn)
            print(mensaje)

        elif opcion == "7":
            print("\n--- Buscar libro por título ---")
            titulo = input("Introduce el título a buscar: ").strip()

            resultados = servicio.buscar_por_titulo(titulo)
            mostrar_libros(resultados)

        elif opcion == "8":
            print("\n--- Buscar libro por autor ---")
            autor = input("Introduce el autor a buscar: ").strip()

            resultados = servicio.buscar_por_autor(autor)
            mostrar_libros(resultados)

        elif opcion == "9":
            print("\n--- Buscar libro por categoría ---")
            categoria = input("Introduce la categoría a buscar: ").strip()

            resultados = servicio.buscar_por_categoria(categoria)
            mostrar_libros(resultados)

        elif opcion == "10":
            print("\n--- Listar libros prestados a un usuario ---")
            id_usuario = input("ID del usuario: ").strip()

            libros = servicio.listar_libros_prestados_usuario(id_usuario)

            if libros is None:
                print("El usuario no existe.")
            else:
                mostrar_libros(libros)

        elif opcion == "11":
            print("\n--- Libros disponibles ---")
            libros = servicio.listar_libros_disponibles()
            mostrar_libros(libros)

        elif opcion == "12":
            print("\n--- Usuarios registrados ---")
            usuarios = servicio.listar_usuarios()
            mostrar_usuarios(usuarios)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()