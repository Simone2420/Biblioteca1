import os
from excepciones import *
from biblioteca import Biblioteca
import sys
from estilos import *
def solo_letras_y_espacios(cadena):
    return all(caracter.isalpha() or caracter.isspace() for caracter in cadena)
def limpiar_consola():
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para Linux/macOS
        os.system('clear')

class Menu:
    biblioteca = None
    def __init__(self,biblioteca):
        self.biblioteca = biblioteca
    
    def menu_registro(self,coleccion):
        while True:
            try:
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
            except (ValueError, TypeError) as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
                break
            except Exception as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
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
            try:
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
                                print("Error: La identificación o numero matricula debe ser un número.")
                            except Exception as e:
                                print(f"Error inesperado: {e}")
                                input("Presione enter para continuar ")
                                break
                        else:
                            print("Error: Tipo de usuario no válido.")
                    case 2:
                        print("Volviendo al menú principal.")
                        self.menu_principal(coleccion)
                    case _:
                        print("Opción inválida. Intente de nuevo.")
            except ValueError as e:
                print("Error: La opcion ser un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")
                input("Presione enter para continuar ")
                break
    def menu_usuario(self, coleccion, usuario):
        while True:
            limpiar_consola()
            print(f"Bienvenido {usuario.obtener_tipo()} {usuario.obtener_nombre()}")
            print("1.) Ver libros disponibles.")
            print("2.) Pedir prestado libros.")
            print("3.) Devolver libros.")
            print("4.) Ver estadísticas (libros prestados).")
            print("5.) Cerrar sesión.")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.ver_libros_disponibles(coleccion)
            elif opcion == "2":
                self.menu_prestar_libro_a_usuario(usuario, self.biblioteca, coleccion) 
            elif opcion == "3":
                self.menu_devolver_libros_por_usuario(usuario, self.biblioteca, coleccion) 
            elif opcion == "4":
                self.mostrar_estadisticas(usuario) 
            elif opcion == "5":
                self.menu_ingreso_usuario(coleccion)
            else:
                print("Opción no válida. Intenta de nuevo.")
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
                    break
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
                    try:
                        prestamos = self.biblioteca.prestar_libros(usuario,libros_a_prestar)
                        for p in prestamos:
                            p.mostrar_informacion()
                    except TypeError as e:
                        print(f"Error: {e}")
                        input("Presione enter para continuar ")
                        break
                    except Exception as e:
                        print(f"Error inesperado: {e}")
                        input("Presione enter para continuar ")
                        break
                case 2:
                    break
                case _:
                    print("Opción inválida. Intente de nuevo.")
    def menu_devolver_libros_por_usuario(self,usuario,biblioteca,coleccion):
        while True:
            print("Devolver Libros")
            print("¿Desea devolver los libros?: ")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
            match opcion:
                case 1:
                    dias_transcurridos_prestamo = int(input("Hace cuantos días solicitó prestado el libro?: "))
                    biblioteca.devolver_libros(usuario,dias_transcurridos_prestamo)
                case 2:
                    self.menu_usuario(coleccion,usuario)
                case _:
                    print("Opción inválida. Intente de nuevo.")
    def mostrar_estadisticas(self,usuario):
        while True:
            print("Ver estadisticas usuario")
            print("¿Desea ver las estadisticas del usuario?: ")
            print("1.) Si")
            print("2.) No")
            opcion = int(input("Ingrese su opción (escriba 1 o 2): "))
            match opcion:
                case 1:
                    usuario.mostrar_informacion()
                    input("Presione cualquier tecla para volver al menu principal.")
                    break
                case 2:
                    break
                case _:
                    print("Opción inválida. Intente de nuevo.")
    def mostrar_prestamos_totales(self):
        while True:
            try:
                print("Mostrar prestamos")
                print("¿Esta seguro de registrar usuario?")
                print("1.) Si")
                print("2.) No")
                opcion = int(input("Desea ver el historico de prestamos?: "))
                match opcion:
                    case 1:
                        self.biblioteca.mostrar_historico_prestamos()
                        input("Presione enter para volver: ")
                        break
                    case 2:
                        break
                    case _:
                        print("Opcion no valida...")
            except (TypeError,ValueError) as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
                break
            except Exception as e:
                print(f"Error {e}")
                input("Presione enter para volver: ")
    def menu_principal(self,coleccion):
        while True:
            print("\nBienvenido a la Biblioteca de la Universidad de Cundinamarca\n")
            print("1.) Registrar usuario.")
            print("2.) Ver usuarios registrados.")
            print("3.) Ingresar usuario")
            print("4.) Ver libros disponibles.")
            print("5.) Ver prestamos registrados.")
            print("6.) Salir del programa")
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
                    self.mostrar_prestamos_totales()
                case 6:
                    sys.exit()
                case _:
                    print("Opción inválida. Intente de nuevo.")
    
