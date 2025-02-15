from excepciones import *
from biblioteca import Biblioteca
def solo_letras_y_espacios(cadena):
    return all(caracter.isalpha() or caracter.isspace() for caracter in cadena)
class Menu:
    def __init__(self,biblioteca):
        self.biblioteca = biblioteca
    def menu_registro(self,coleccion):
        while True:
            print("Registro")
            print("¿Esta seguro de registrar usuario?")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción: "))
            match opcion:
                case 1:
                    tipo_usuario = input("¿El usuario es docente o estudiante?: ")
                    if tipo_usuario.lower() == "docente":
                        try:
                            nombre_docente = input("Ingrese el nombre del docente: ")
                            if not solo_letras_y_espacios(nombre_docente):
                                raise DatosInvalidos("Nombre inválido.")
                        except DatosInvalidos as e:
                            print(f"Error: {e}.")
                            print("Volviendo al menu de registro...")
                            self.menu_registro(coleccion)
                        try:
                            identificacion_docente = int(input("Ingrese la identificación del docente: "))
                        except ValueError as e:
                            print(f"Error la identificacion debe ser numerica")
                            print("Volviendo al menu de registro...")
                            self.menu_registro(coleccion)
                        try:
                            id_profesional_docente = int(input("Ingrese el ID profesional del docente (numero entre 10000 y 99999): "))
                            if id_profesional_docente < 10000 or id_profesional_docente > 99999:
                                raise DatosInvalidos("ID profesional inválido.")
                        except DatosInvalidos as e:
                            print(f"Error: {e}.")
                            print("Volviendo al menu de registro...")
                            self.menu_registro(coleccion)
                        coleccion.registrar_docente(nombre_docente, identificacion_docente, id_profesional_docente)
                    elif tipo_usuario.lower() == "estudiante":
                        try:
                            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
                            if not solo_letras_y_espacios(nombre_estudiante):
                                raise DatosInvalidos("Nombre inválido.")
                        except DatosInvalidos as e:
                            print(f"Error: {e}.")
                            print("Volviendo al menu de registro...")
                            self.menu_registro(coleccion)
                        try:
                            identificacion_estudiante = int(input("Ingrese la identificación del estudiante: "))
                        except ValueError as e:
                            print(f"Error la identificacion debe ser numerica")
                            print("Volviendo al menu de registro...")
                            self.menu_registro(coleccion)
                        try:
                            numero_matricula_estudiante = int(input("Ingrese el número de matricula del estudiante (numero entre 10000 y 99999): "))
                            if numero_matricula_estudiante < 10000 or numero_matricula_estudiante > 99999:
                                raise DatosInvalidos("Número de matricula inválido.")
                        except DatosInvalidos as e:
                            print(f"Error: {e}.")
                            print("Volviendo al menu principal...")
                            self.menu_principal(coleccion)
                        coleccion.registrar_estudiante(nombre_estudiante, identificacion_estudiante, numero_matricula_estudiante)
                case 2:
                    self.menu_principal(coleccion)
                case _:
                    print("Opcion invalida.")
    def menu_ver_usuarios(self,coleccion):
        while True:
            print("Ver Usuarios")
            print("¿Desea ver estudiantes y docentes registrados?")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción: "))
            match opcion:
                case 1:
                    print("\nEstudiantes:")
                    for estudiante in coleccion.estudiantes:
                        print(f"Nombre: {estudiante.obtener_nombre()}, Identificación: {estudiante.obtener_identificacion()}, Número de Matricula: {estudiante.obtener_matricula()}")
                    print("\nDocentes:")
                    for docente in coleccion.docentes:
                        print(f"Nombre: {docente.obtener_nombre()}, Identificación: {docente.obtener_identificacion()}, ID Profesional: {docente.obtener_id_profesional()}")
                    input("Presione cualquier tecla para volver al menu principal.")
                    self.menu_principal(coleccion)
                case 2:
                    self.menu_principal(coleccion)
                case _:
                    print("Opcion invalida.")
    def menu_ingreso_usuario(self, coleccion):
        while True:
            print("Ingreso usuario")
            print("¿Desea ingresar algún usuario?")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
            match opcion:
                case 1:
                    tipo_usuario = input("¿El usuario es docente o estudiante?: ")
                    if tipo_usuario.lower() == "docente":
                        try:
                            docente_identificacion_validar = int(input("Ingrese el número de su identificación: "))
                            docente_id_profesional_validar = int(input("Ingrese el número de id profesional del docente:"))
                            docente_encontrado = None
                            for docente in coleccion.docentes:
                                if (docente.obtener_identificacion() == docente_identificacion_validar) and ((docente.obtener_id_profesional() == docente_id_profesional_validar)):
                                    docente_encontrado = docente
                                    break
                            if docente_encontrado:
                                print(f"Bienvenido, {docente_encontrado.obtener_nombre()}.")
                                self.menu_usuario(coleccion, docente_encontrado)
                            else:
                                print("Error: No se encontró un docente con esa identificación.")
                        except ValueError:
                            print("Error: La identificación debe ser un número.")
                    elif tipo_usuario.lower() == "estudiante":
                        try:
                            estudiante_identificacion_validar = int(input("Ingrese el número de su identificación: "))
                            estudiante_matricula_validar = int(input("Ingrese el numero de matricula del estudiante: "))
                            # Buscar el estudiante en la lista de estudiantes
                            estudiante_encontrado = None
                            for estudiante in coleccion.estudiantes:
                                if (estudiante.obtener_identificacion() == estudiante_identificacion_validar)and\
                                    (estudiante.obtener_matricula() == estudiante_matricula_validar):
                                    estudiante_encontrado = estudiante
                                    break
                            if estudiante_encontrado:
                                print(f"Bienvenido, {estudiante_encontrado.obtener_nombre()}.")
                                self.menu_usuario(coleccion, estudiante_encontrado)
                            else:
                                print("Error: No se encontró un estudiante con esa identificación.")
                        except ValueError:
                            print("Error: La identificación debe ser un número.")
                    else:
                        print("Error: Tipo de usuario no válido.")
                case 2:
                    print("Volviendo al menú principal.")
                    self.menu_principal(coleccion)
                case _:
                    print("Opción inválida. Intente de nuevo.")
    def menu_usuario(self,coleccion,usuario):
        while True:
            print(f"Bienvenido {usuario.obtener_tipo()} {usuario.obtener_nombre()}")
            print("1.) Ver libros disponibles.")
            print("2.) Pedir prestado libros.")
            print("3.) Devolver libros.")
            print("4.) Ver estadisticas (libros prestados)")
            print("5.) Cerrar sesión")
            opcion = int(input("Selecciona una opción: "))
            match opcion:
                case 1:
                    self.ver_libros_disponibles(coleccion)
                case 2:
                    self.menu_prestar_libro_a_usuario(usuario,self.biblioteca,coleccion)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case _:
                    pass
    def ver_libros_disponibles(self,coleccion):
        while True:
            print("Ver libros disponibles")
            print("¿Desea ver los libros disponibles?: ")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
            match opcion:
                case 1:
                    print("\Libros disponibles:")
                    for libro in coleccion.libros:
                        print(f"Libro {libro.obtener_titulo()} / Autor {libro.obtener_autor()} /Año publicación: {libro.obtener_ano_publicacion()}")
                    input("Presione cualquier tecla para volver al menu principal.")
                    self.menu_principal(coleccion)
                case 2:
                    break
                case _:
                    print("Opción inválida. Intente de nuevo.")
    def menu_prestar_libro_a_usuario(self,usuario,biblioteca,coleccion):
        while True:
            print("Prestar Libro (s)")
            print("¿Desea pedir prestados los libros?: ")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
            match opcion:
                case 1:
                    libros_a_prestar = []
                    numero_libros = int(input(f"¿Cuantos libros va solicitar prestado limite de {usuario.obtener_limite_libros()}?: "))
                    if numero_libros <= usuario.obtener_limite_libros():
                        biblioteca.mostrar_libros_disponibles()
                        lista_libros_disponibles_aux = coleccion.libros
                        
                        for i in range(numero_libros):
                            libro_prestado = input(f"Ingrese el nombre del libro número {i+1}: ")
                            libro_encontrado = None
                            for libro in lista_libros_disponibles_aux:
                                if libro.obtener_titulo().lower() == libro_prestado.lower():
                                    libro_encontrado = libro
                                    break
                            if libro_encontrado:
                                if libro_encontrado.obtener_esta_disponible():
                                    libros_a_prestar.append(libro_encontrado)
                                    indice_libro = lista_libros_disponibles_aux.index(libro_encontrado)
                                    lista_libros_disponibles_aux.pop(indice_libro)
                                    print(f"Libro '{libro_encontrado.obtener_titulo()}' agregado para préstamo.")
                                else:
                                    print(f"Error: El libro '{libro_encontrado.obtener_titulo()}' no está disponible.")
                            else:
                                print(f"Error: El libro '{libro_prestado}' no existe en la biblioteca.")
                    prestamos = self.biblioteca.prestar_libros(usuario,libros_a_prestar)
                    for p in prestamos:
                        p.mostrar_informacion()
                case 2:
                    break
                case _:
                    print("Opción inválida. Intente de nuevo.")
    
    def menu_principal(self,coleccion):
        while True:
            print("\nBienvenido a la Biblioteca de la Universidad de Cundinamarca\n")
            print("1.) Registrar usuario.")
            print("2.) Ver usuarios registrados.")
            print("3.) Ingresar usuario")
            print("4.) Ver libros disponibles.")
            print("5.) Salir del programa.")
            opcion = int(input("Selecciona una opción: "))
            match opcion:
                case 1:
                    self.menu_registro(coleccion)
                case 2:
                    self.menu_ver_usuarios(coleccion)
                case 3:
                    self.menu_ingreso_usuario(coleccion)
                case 4:
                    self.ver_libros_disponibles(coleccion)
                case 5:
                    pass
                case _:
                    pass
    
