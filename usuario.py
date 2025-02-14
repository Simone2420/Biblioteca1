class Usuario:
    def __init__(self, nombre, identificacion, tipo):
        self.__nombre = nombre  
        self.__identificacion = identificacion
        self._tipo = tipo
        self.__cantidad_libros_a_prestar = 0  
        self._libros_prestados = [] 
        self._limite_libros = 0

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_identificacion(self):
        return self.__identificacion

    def obtener_tipo(self):
        return self._tipo

    def obtener_libros_prestados(self):
        return self._libros_prestados
    def obtener_cantidad_libros_a_prestar(self):
        return self.__cantidad_libros_a_prestar
    def establecer_cantidad_libros_a_prestar(self, nueva_cantidad_libros_a_prestar):
        self.__cantidad_libros_a_prestar = nueva_cantidad_libros_a_prestar
    def obtener_limite_libros(self):
        return self._limite_libros
    # Método para mostrar información del usuario
    def mostrar_informacion(self):
        print(f"Nombre: {self.obtener_nombre()}")
        print(f"ID: {self.obtener_identificacion()}")
        print(f"Tipo: {self.obtener_tipo()}")
        print(f"Libros Prestados: {[libro.titulo for libro in self._libros_prestados]}")

    # Método para prestar un libro
    def prestar_libro(self, libro):
        if libro.disponible:
            self._libros_prestados.append(libro)
            libro.prestar()
            print(f"Libro '{libro.titulo}' prestado exitosamente.")
        else: #como meter una excepcion
            print(f"El libro '{libro.titulo}' no está disponible.")
    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            print(f"Libro '{libro.titulo}' devuelto exitosamente.")
            self._libros_prestados.remove(libro)
        else: 
            print(f"El libro '{libro.titulo}' no fue prestado a este usuario.")
    def __str__(self):
        return f"{self.obtener_nombre()} es {self.obtener_tipo()}"
    def __repr__(self):
        return f"{self.obtener_nombre()} es {self.obtener_tipo()}"
class Estudiante(Usuario):
    def __init__(self, nombre, identificacion, matricula):
        super().__init__(nombre, identificacion, tipo="estudiante")
        self._matricula = matricula
        self._limite_libros = 5  

    def obtener_matricula(self):
        return self._matricula


class Docente(Usuario):
    def __init__(self, nombre, identificacion, id_profesional):
        super().__init__(nombre, identificacion, tipo="docente")
        self.__id_profesional = id_profesional
        self._limite_libros = 7 

    def obtener_id_profesional(self):
        return self.__id_profesional
