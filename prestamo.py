from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, usuario, libro):
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = datetime.now()
        self._fecha_devolucion = None

    # Método para registrar la devolución
    def registrar_devolucion(self):
        self._fecha_devolucion = datetime.now()

    # Método para mostrar información del préstamo
    def mostrar_informacion(self):
        print(f"Usuario: {self._usuario.obtener_nombre()}")
        print(f"Libro: {self._libro.obtener_titulo()}")
        print(f"Fecha de Préstamo: {self._fecha_prestamo.strftime('%Y-%m-%d')}")
        if self._fecha_devolucion:
            print(f"Fecha de Devolución: {self._fecha_devolucion.strftime('%Y-%m-%d')}")
        else:
            print("Aún no ha sido devuelto.")