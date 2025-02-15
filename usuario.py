class Usuario:
    nombre = ""
    identificacion = 0
    tipo = ""
    cantidad_libros_a_prestar = 0
    libros_prestado = []
    limite_libros =0
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
    def establecer_limite_libros(self,nuevo_limite):
        self._limite_libros = nuevo_limite
    # Método para mostrar información del usuario
    def mostrar_informacion(self):
        print(f"\nNombre: {self.obtener_nombre()}")
        print(f"ID: {self.obtener_identificacion()}")
        print(f"Tipo: {self.obtener_tipo()}")
        print(f"Libros Prestados: {[libro.obtener_titulo() for libro in self._libros_prestados]}")

    # Método para prestar un libro
    def prestar_libro(self, libro):
        if libro.obtener_esta_disponible():
            self._libros_prestados.append(libro)
            libro.prestar()
            print(f"Libro '{libro.obtener_titulo()}' prestado exitosamente.")
        else: 
            print(f"El libro '{libro.obtener_titulo()}' no está disponible.")
    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            print(f"Libro '{libro.obtener_titulo()}' devuelto exitosamente.")
            self._libros_prestados.remove(libro)
        else: 
            print(f"El libro '{libro.obtener_titulo()}' no fue prestado a este usuario.")
    def __str__(self):
        return f"{self.obtener_nombre()} es {self.obtener_tipo()}"
    def __repr__(self):
        return f"{self.obtener_nombre()} es {self.obtener_tipo()}"
class Estudiante(Usuario):
    matricula = 0
    def __init__(self, nombre, identificacion, matricula):
        super().__init__(nombre, identificacion, tipo="estudiante")
        self._matricula = matricula
        self._limite_libros = 5  

    def obtener_matricula(self):
        return self._matricula

    def mostrar_informacion(self):
        print(f"\nNombre: {self.obtener_nombre()}")
        print(f"ID: {self.obtener_identificacion()}")
        print(f"Número matricula: {self.obtener_matricula()}")
        print(f"Tipo: {self.obtener_tipo()}")
        print(f"Libros Prestados: {[libro.obtener_titulo() for libro in self._libros_prestados]}")
class Docente(Usuario):
    id_profesional = 0
    def __init__(self, nombre, identificacion, id_profesional):
        super().__init__(nombre, identificacion, tipo="docente")
        self.__id_profesional = id_profesional
        self._limite_libros = 7 

    def obtener_id_profesional(self):
        return self.__id_profesional
    def mostrar_informacion(self):
        print(f"\nNombre: {self.obtener_nombre()}")
        print(f"ID: {self.obtener_identificacion()}")
        print(f"Id profesional: {self.obtener_id_profesional()}")
        print(f"Tipo: {self.obtener_tipo()}")
        print(f"Libros Prestados: {[libro.obtener_titulo() for libro in self._libros_prestados]}")
