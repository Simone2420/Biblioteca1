from usuario import Estudiante, Docente
from libro import Libro
from prestamo import Prestamo
from biblioteca import Biblioteca
from excepciones import *
from menu import Menu
import random
import sys

nombres_docentes = ["Carlos Inti","Blass Muñoz"]
nombres_estudiantes = ["Diego Ortiz","Hediberto de las Nieves", "Alberto Fonseca"]
identificaciones = [random.randint(10000000,99999999) for _ in range(5)]
id_profesionales = [random.randint(10000,99999) for _ in range(2)]
numeros_matriculas = [random.randint(10000,99999) for _ in range(3)]
titulos_libros = [
    "Cien años de soledad",
    "Don Quijote de la Mancha",
    "La sombra del viento",
    "El amor en los tiempos del cólera",
    "Rayuela",
    "Crónica de una muerte anunciada",
    "El principito",
    "1984",
    "Ficciones",
    "La casa de los espíritus",
    "Los detectives salvajes",
    "El laberinto de la soledad",
    "Pedro Páramo",
    "El túnel",
    "La ciudad y los perros",
    "El aleph",
    "El nombre del viento",
    "El retrato de Dorian Gray",
    "Orgullo y prejuicio",
    "Crimen y castigo"
]
nombre_autores = [
    "Gabriel García Márquez",
    "Miguel de Cervantes",
    "Jorge Luis Borges",
    "Isabel Allende",
    "Mario Vargas Llosa"
]
anos_publicaciones = [random.randint(1800,2025) for _ in range(20)]
class CrearColecciones:
    def __init__(self):
        self.docentes = []
        self.estudiantes = []
        self.libros = []
    def agregar_docentes(self,nombres_docentes,identificaciones,id_profesionales,numero_docentes = 2):
        nombres_docentes_copia = nombres_docentes[:]
        identificaciones_aux = identificaciones[0:2]
        id_profesionales_copia = id_profesionales[:]
        for _ in range(numero_docentes):
            nombre_docente = nombres_docentes_copia.pop(0)
            identificacion_docente = identificaciones_aux.pop(0)
            id_profesional_docente = id_profesionales_copia.pop(0)
            self.docentes.append(Docente(nombre_docente, identificacion_docente,id_profesional_docente))
    def agregar_estudiantes(self,nombres_estudiantes,identificaciones,numeros_matriculas,numero_estudiantes=3):
        nombres_estudiante_copia = nombres_estudiantes
        identificaciones_aux = identificaciones[2:]
        numeros_matriculas_copia = numeros_matriculas[:]
        for _ in range(numero_estudiantes):
            nombre_estudiante = nombres_estudiante_copia.pop(0)
            identificacion_estudiante = identificaciones_aux.pop(0)
            numero_matricula_estudiante = numeros_matriculas_copia.pop(0)
            self.estudiantes.append(Estudiante(nombre_estudiante, identificacion_estudiante,numero_matricula_estudiante))
    def agregar_libros(self,titulos_libros,nombre_autores,anos_publicaciones,numero_libros=20):
        titulos_libros_copia = titulos_libros[:]
        for _ in range(numero_libros):
            titulo_libro = titulos_libros_copia.pop(0)
            nombre_autor = random.choice(nombre_autores)
            ano_publicacion = random.choice(anos_publicaciones)
            self.libros.append(Libro(titulo_libro,nombre_autor,ano_publicacion))

    def registrar_docente(self, nombre_docente, identificacion_docente, id_profesional_docente):
        docente = Docente(nombre_docente, identificacion_docente, id_profesional_docente)
        self.docentes.append(docente)

    def registrar_estudiante(self, nombre_estudiante, identificacion_estudiante, numero_matricula_estudiante):
        estudiante = Estudiante(nombre_estudiante, identificacion_estudiante, numero_matricula_estudiante)
        self.estudiantes.append(estudiante)

coleccion = CrearColecciones()
coleccion.agregar_docentes(nombres_docentes, identificaciones, id_profesionales)
coleccion.agregar_estudiantes(nombres_estudiantes, identificaciones, numeros_matriculas)
coleccion.agregar_libros(titulos_libros, nombre_autores, anos_publicaciones)
biblioteca = Biblioteca(coleccion.estudiantes+coleccion.docentes,coleccion.libros)
print(coleccion.docentes)
print(coleccion.estudiantes)
print(coleccion.libros)


if __name__ == '__main__':
    menu = Menu(biblioteca)
    menu.menu_principal(coleccion)