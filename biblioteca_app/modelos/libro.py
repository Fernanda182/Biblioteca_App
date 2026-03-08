class Libro:
    """
    Modelo que representa un libro dentro del sistema de biblioteca.

    Diseño:
    - Almacenar título y autor como una tupla, por lo tanto
      se guarda en el atributo privado _info = (titulo, autor).
    - ISBN se usa como identificador único.
    - Se aplica encapsulamiento usando atributos privados y propiedades.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para cumplir el requisito técnico
        self._info = (titulo, autor)

        # Atributos encapsulados
        self._categoria = categoria
        self._isbn = isbn

    @property
    def titulo(self):
        """Devuelve el título del libro."""
        return self._info[0]

    @property
    def autor(self):
        """Devuelve el autor del libro."""
        return self._info[1]

    @property
    def categoria(self):
        """Devuelve la categoría del libro."""
        return self._categoria

    @property
    def isbn(self):
        """Devuelve el ISBN del libro."""
        return self._isbn

    def __str__(self):
        """
        Representación legible del libro para mostrar en consola.
        """
        return f"ISBN: {self._isbn} | Título: {self.titulo} | Autor: {self.autor} | Categoría: {self._categoria}"