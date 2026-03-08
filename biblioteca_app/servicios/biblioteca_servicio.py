from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Clase de servicio que concentra toda la lógica del negocio.

    Responsabilidades:
    - Gestionar catálogo de libros disponibles.
    - Gestionar usuarios registrados.
    - Gestionar préstamos y devoluciones.
    - Realizar búsquedas.

    Decisiones de diseño importantes:
    - libros_disponibles se almacena en un diccionario:
      clave = ISBN, valor = objeto Libro
      Esto cumple el requisito del enunciado y además permite búsquedas rápidas por ISBN.

    - ids_usuarios se almacena en un set:
      sirve para garantizar unicidad de IDs de usuario, cumpliendo el requisito.

    - usuarios se guarda en un diccionario adicional:
      clave = id_usuario, valor = objeto Usuario
      El set garantiza unicidad y el diccionario permite acceder rápidamente al usuario.
    """

    def __init__(self):
        self._libros_disponibles = {}   # {isbn: Libro}
        self._usuarios = {}             # {id_usuario: Usuario}
        self._ids_usuarios = set()      # {id_usuario}

    # =========================
    # MÉTODOS DE LIBROS
    # =========================

    def anadir_libro(self, titulo, autor, categoria, isbn):
        """
        Añade un libro al catálogo si su ISBN no existe todavía.
        Devuelve una tupla (exito, mensaje).
        """
        if isbn in self._libros_disponibles:
            return False, "Ya existe un libro con ese ISBN."

        libro = Libro(titulo, autor, categoria, isbn)
        self._libros_disponibles[isbn] = libro
        return True, "Libro añadido correctamente."

    def quitar_libro(self, isbn):
        """
        Elimina un libro del catálogo si existe.
        Solo se pueden quitar libros que estén actualmente disponibles.
        Si el libro estuviera prestado, no aparecería en libros_disponibles.
        """
        if isbn not in self._libros_disponibles:
            return False, "No se puede quitar: el libro no está disponible o no existe."

        del self._libros_disponibles[isbn]
        return True, "Libro quitado correctamente."

    def listar_libros_disponibles(self):
        """
        Devuelve una lista con todos los libros disponibles.
        """
        return list(self._libros_disponibles.values())

    # =========================
    # MÉTODOS DE USUARIOS
    # =========================

    def registrar_usuario(self, nombre, id_usuario):
        """
        Registra un usuario si su ID no existe.
        Se usa el set para controlar unicidad de IDs.
        """
        if id_usuario in self._ids_usuarios:
            return False, "Ya existe un usuario con ese ID."

        usuario = Usuario(nombre, id_usuario)
        self._usuarios[id_usuario] = usuario
        self._ids_usuarios.add(id_usuario)
        return True, "Usuario registrado correctamente."

    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario si existe y no tiene libros prestados.
        Esto evita inconsistencias en el sistema.
        """
        if id_usuario not in self._usuarios:
            return False, "El usuario no existe."

        usuario = self._usuarios[id_usuario]

        if len(usuario.libros_prestados) > 0:
            return False, "No se puede dar de baja: el usuario tiene libros prestados."

        del self._usuarios[id_usuario]
        self._ids_usuarios.remove(id_usuario)
        return True, "Usuario dado de baja correctamente."

    def obtener_usuario(self, id_usuario):
        """
        Devuelve el objeto Usuario si existe, o None si no existe.
        """
        return self._usuarios.get(id_usuario)

    # =========================
    # PRÉSTAMOS Y DEVOLUCIONES
    # =========================

    def prestar_libro(self, id_usuario, isbn):
        """
        Presta un libro a un usuario si:
        - el usuario existe
        - el libro está disponible
        """
        if id_usuario not in self._usuarios:
            return False, "El usuario no existe."

        if isbn not in self._libros_disponibles:
            return False, "El libro no está disponible o no existe."

        usuario = self._usuarios[id_usuario]
        libro = self._libros_disponibles.pop(isbn)

        # Se añade el libro a la lista del usuario
        usuario.agregar_libro_prestado(libro)

        return True, f"Préstamo realizado: '{libro.titulo}' prestado a {usuario.nombre}."

    def devolver_libro(self, id_usuario, isbn):
        """
        Devuelve un libro prestado por un usuario al catálogo de disponibles.
        """
        if id_usuario not in self._usuarios:
            return False, "El usuario no existe."

        usuario = self._usuarios[id_usuario]

        # Buscar el libro dentro de la lista de libros prestados del usuario
        libro_a_devolver = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_a_devolver = libro
                break

        if libro_a_devolver is None:
            return False, "Ese usuario no tiene prestado un libro con ese ISBN."

        # Se quita de la lista del usuario y se devuelve al catálogo
        usuario.quitar_libro_prestado(isbn)
        self._libros_disponibles[isbn] = libro_a_devolver

        return True, f"Libro devuelto correctamente: '{libro_a_devolver.titulo}'."

    # =========================
    # BÚSQUEDAS
    # =========================

    def buscar_por_titulo(self, titulo):
        """
        Busca libros por título.
        Se buscan coincidencias parciales sin distinguir mayúsculas/minúsculas.
        Busca tanto en disponibles como en prestados.
        """
        resultados = []

        # Buscar en disponibles
        for libro in self._libros_disponibles.values():
            if titulo.lower() in libro.titulo.lower():
                resultados.append(libro)

        # Buscar en prestados
        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if titulo.lower() in libro.titulo.lower():
                    resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.
        """
        resultados = []

        for libro in self._libros_disponibles.values():
            if autor.lower() in libro.autor.lower():
                resultados.append(libro)

        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if autor.lower() in libro.autor.lower():
                    resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria):
        """
        Busca libros por categoría.
        """
        resultados = []

        for libro in self._libros_disponibles.values():
            if categoria.lower() in libro.categoria.lower():
                resultados.append(libro)

        for usuario in self._usuarios.values():
            for libro in usuario.libros_prestados:
                if categoria.lower() in libro.categoria.lower():
                    resultados.append(libro)

        return resultados

    # =========================
    # CONSULTAS
    # =========================

    def listar_libros_prestados_usuario(self, id_usuario):
        """
        Devuelve la lista de libros prestados de un usuario.
        """
        if id_usuario not in self._usuarios:
            return None

        return self._usuarios[id_usuario].libros_prestados

    def listar_usuarios(self):
        """
        Devuelve una lista con todos los usuarios registrados.
        """
        return list(self._usuarios.values())