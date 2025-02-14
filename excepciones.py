# Definición de excepciones personalizadas
class LimitePrestamosExcedido(Exception):
    """Excepción lanzada cuando un usuario excede su límite de préstamos."""
    def __init__(self, mensaje="El usuario ha excedido su límite de préstamos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class LibroNoDisponible(Exception):
    """Excepción lanzada cuando un libro no está disponible para préstamo."""
    def __init__(self, mensaje="El libro no está disponible"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class DatosInvalidos(Exception):
    """Excepción lanzada cuando los datos ingresados son inválidos."""
    def __init__(self, mensaje="Los datos ingresados son inválidos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class NoHayLibrosParaDevolver(Exception):
    """Excepcion lanzada cuando el usuario no tiene libros para devolver."""
    def __init__(self, mensaje="El usuario no tiene libros para devolver"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
class UsuarioNoRegistrado(Exception):
    """Excepcion lanzada cuando el usuario no aparece registrado en la bibloteca"""
    def __init__(self, mensaje="El usuario no está registrado"):
        self.mensaje
        super().__init__(self.mensaje)