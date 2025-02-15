from excepciones import *
from datetime import datetime, timedelta
from prestamo import Prestamo
class Biblioteca:
    def __init__(self,usuarios,libros_disponibles):
        self.usuarios = usuarios
        self.libros_disponibles = libros_disponibles
        self.lista_prestamos = []
    def mostrar_libros_disponibles(self):
        for libro in self.libros_disponibles:
            print(libro)
    def prestar_libros(self,usuario,libros):
        libros_a_prestar = libros
        try:
            prestamos = []
            if usuario in self.usuarios:
                if len(libros_a_prestar) + usuario.obtener_cantidad_libros_a_prestar() > usuario.obtener_limite_libros():
                    raise LimitePrestamosExcedido("El usuario excede su límite de préstamos")
                for libro in self.libros_disponibles:
                    if libro.obtener_esta_disponible() != True:
                        raise LibroNoDisponible(f"El libro {libro} no está disponible")
                numero_libros_prestar = 0
                for libro in libros_a_prestar:
                    usuario.prestar_libro(libro)
                    prestamo = Prestamo(usuario, libro)
                    self.lista_prestamos.append(prestamo)
                    prestamos.append(prestamo)
                numero_libros_prestar += len(libros_a_prestar)
                usuario.establecer_cantidad_libros_a_prestar(numero_libros_prestar)
                usuario.establecer_limite_libros(usuario.obtener_cantidad_libros_a_prestar()-numero_libros_prestar) # Actualizar contador
                return prestamos
            else:
                raise UsuarioNoRegistrado()
        except (UsuarioNoRegistrado, LimitePrestamosExcedido) as e:
            print(f"Error: {e}")
            
        except LibroNoDisponible as e:
            for prestamo in prestamos:
                libro.establecer_estado(True)
                self.prestamos_activos.remove(prestamo)
            print(f"Error: {e}")
            
        
    def devolver_libros(self, usuario):
        try:
            if len(usuario.obtener_libros_prestados()) == 0:
                raise NoHayLibrosParaDevolver(f"El usuario {usuario} no tiene libros para devolver")
            else:
                for prestamo in self.lista_prestamos():
                    prestamo.registrar_devolucion()
                for libro_duevuelto in usuario.obtener_libros_prestados():
                    usuario.devolver_libro(libro_duevuelto)
        except NoHayLibrosParaDevolver as e:
            print(f"Error: {e}")
            print("Volviendo al menu principal")
        except Exception as e:
            print(f"Error {e}")
            print("Volviendo al menu principal")