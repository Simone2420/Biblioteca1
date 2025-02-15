from excepciones import *
from prestamo import Prestamo

class Biblioteca:
    def __init__(self, usuarios, libros_disponibles):
        self.usuarios = usuarios
        self.libros_disponibles = libros_disponibles
        self.lista_prestamos = []

    def mostrar_libros_disponibles(self):
        for libro in self.libros_disponibles:
            print(libro)

    def prestar_libros(self, usuario, libros):
        libros_a_prestar = libros
        try:
            prestamos = []
            if usuario in self.usuarios:
                if len(libros_a_prestar) + usuario.obtener_cantidad_libros_a_prestar() > usuario.obtener_limite_libros():
                    raise LimitePrestamosExcedido("El usuario excede su límite de préstamos")
                for libro in libros_a_prestar:
                    if not libro.obtener_esta_disponible():
                        raise LibroNoDisponible(f"El libro {libro} no está disponible")
                numero_libros_prestar = 0
                for libro in libros_a_prestar:
                    usuario.prestar_libro(libro)
                    prestamo = Prestamo(usuario, libro)
                    self.lista_prestamos.append(prestamo)
                    prestamos.append(prestamo)
                    libro.establecer_estado(False)  # Marcar libro como no disponible
                numero_libros_prestar += len(libros_a_prestar)
                usuario.establecer_cantidad_libros_a_prestar(numero_libros_prestar)
                usuario.establecer_limite_libros(usuario.obtener_limite_libros() - numero_libros_prestar)  # Actualizar contador
                return prestamos
            else:
                raise UsuarioNoRegistrado()
        except (UsuarioNoRegistrado, LimitePrestamosExcedido) as e:
            print(f"Error: {e}")
        except LibroNoDisponible as e:
            for prestamo in prestamos:
                prestamo.libro.establecer_estado(True)  # Restablecer estado del libro
                self.lista_prestamos.remove(prestamo)  # Eliminar préstamo de la lista
            print(f"Error: {e}")

    def agregar_libros(self, libro):
        """Agrega un libro a la lista de libros disponibles si no está ya en la lista."""
        if libro not in self.libros_disponibles:
            self.libros_disponibles.append(libro)

    def devolver_libros(self, usuario, numero_dias):
        try:
            libros_prestados = usuario.obtener_libros_prestados()
            if len(libros_prestados) == 0:
                raise NoHayLibrosParaDevolver(f"El usuario {usuario} no tiene libros para devolver")
            
            # Crear una copia de la lista de libros prestados para evitar problemas durante la iteración
            libros_prestados_copia = libros_prestados.copy()
            
            for libro_devuelto in libros_prestados_copia:
                # Buscar el préstamo correspondiente al libro y al usuario
                for prestamo in self.lista_prestamos:
                    if prestamo.obtener_libro() == libro_devuelto and prestamo.obtener_usuario() == usuario:
                        prestamo.registrar_devolucion(numero_dias)
                        prestamo.mostrar_informacion()
                        # Restablecer el estado del libro a disponible
                        libro_devuelto.establecer_estado(True)
                        # Agregar el libro a la lista de libros disponibles si no está ya
                        self.agregar_libros(libro_devuelto)
                        # Eliminar el préstamo de la lista de préstamos activos
                        self.lista_prestamos.remove(prestamo)
                        # Devolver el libro al usuario
                        usuario.devolver_libro(libro_devuelto)
                        break
            
            # Actualizar el límite de libros del usuario
            usuario.establecer_limite_libros(usuario.obtener_limite_libros() + len(libros_prestados))
        
        except NoHayLibrosParaDevolver as e:
            print(f"Error: {e}")
            print("Volviendo al menú principal")
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Volviendo al menú principal")