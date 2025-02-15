from datetime import datetime, timedelta

class Prestamo:
    usuario = None
    libro = None
    fecha_prestamo = None
    fecha_devolucion = None 
    def __init__(self, usuario, libro):
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = datetime.now()
        self._fecha_devolucion = None
    def obtener_usuario(self):
        return self._usuario
    def obtener_libro(self):
        return self._libro
    def obtener_fecha_prestamo(self):
        return self._fecha_prestamo
    def obtener_fecha_devolucion(self):
        return self._fecha_devolucion
    # Método para registrar la devolución
    def registrar_devolucion(self,numero_dias):
        self._fecha_devolucion = self.obtener_fecha_prestamo() + timedelta(days=numero_dias)

    # Método para mostrar información del préstamo
    def mostrar_informacion(self):
        print(f"Usuario: {self._usuario.obtener_nombre()}")
        print(f"Libro: {self._libro.obtener_titulo()}")
        print(f"Fecha de Préstamo: {self._fecha_prestamo.strftime('%Y-%m-%d')}")
        if self._fecha_devolucion:
            print(f"Fecha de Devolución: {self._fecha_devolucion.strftime('%Y-%m-%d')}")
        else:
            print("Aún no ha sido devuelto.")