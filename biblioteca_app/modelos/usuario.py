class Usuario:
    """
    Modelo que representa a un usuario registrado en la biblioteca.

    Diseño:
    - El enunciado exige una lista para almacenar los libros prestados.
    - Se guarda una lista de objetos Libro en _libros_prestados.
    - Se aplica encapsulamiento con atributos privados y propiedades.
    """

    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario

        # Lista requerida por el enunciado
        self._libros_prestados = []

    @property
    def nombre(self):
        """Devuelve el nombre del usuario."""
        return self._nombre

    @property
    def id_usuario(self):
        """Devuelve el ID único del usuario."""
        return self._id_usuario

    @property
    def libros_prestados(self):
        """
        Devuelve la lista de libros prestados.

        Nota:
        Se devuelve la referencia directa porque en este ejercicio se trabaja
        de forma controlada desde el servicio. En proyectos más grandes,
        podría devolverse una copia para reforzar encapsulamiento.
        """
        return self._libros_prestados

    def agregar_libro_prestado(self, libro):
        """Añade un libro a la lista de préstamos del usuario."""
        self._libros_prestados.append(libro)

    def quitar_libro_prestado(self, isbn):
        """
        Elimina de la lista del usuario el libro cuyo ISBN coincida.
        Devuelve True si lo encontró y eliminó, False si no existía.
        """
        for libro in self._libros_prestados:
            if libro.isbn == isbn:
                self._libros_prestados.remove(libro)
                return True
        return False

    def __str__(self):
        """
        Representación legible del usuario para mostrar en consola.
        """
        return f"ID: {self._id_usuario} | Nombre: {self._nombre}"