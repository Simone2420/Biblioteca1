class Libro:
    def __init__(self, titulo, autor, ano_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacion = ano_publicacion
        self._disponible = True  # Estado inicial: disponible

    # Métodos getters
    def obtener_titulo(self):
        return self._titulo

    def obtener_autor(self):
        return self._autor

    def obtener_ano_publicacion(self):
        return self._ano_publicacion

    def esta_disponible(self):
        return self._disponible

    # Métodos para cambiar el estado del libro
    def prestar(self):
        if self._disponible:
            self._disponible = False

    def devolver(self):
        if not self._disponible:
            self._disponible = True
    def establecer_estado(self,nuevo_estado):
        self._disponible = nuevo_estado
    def __str__(self):
        return self.obtener_titulo()
    def __repr__(self):
        return self.obtener_titulo()