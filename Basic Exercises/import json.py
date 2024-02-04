import json

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Calificaciones: {self.calificaciones}"

    def a_diccionario(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'calificaciones': self.calificaciones
        }

def guardar_en_archivo(estudiantes):
    try:
        with open('estudiantes.txt', 'w') as archivo:
            for estudiante in estudiantes:
                archivo.write(json.dumps(estudiante.a_diccionario()) + '\n')
        print("Estudiantes guardados en el archivo correctamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")

def cargar_desde_archivo():
    estudiantes = []
    try:
        with open('estudiantes.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                estudiante_data = json.loads(linea)
                estudiante = Estudiante(**estudiante_data)
                estudiantes.append(estudiante)
        print("Estudiantes cargados desde el archivo correctamente.")
    except Exception as e:
        print(f"Error al cargar desde el archivo: {e}")
    return estudiantes

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    calificaciones = input("Ingrese las calificaciones del estudiante (separadas por comas): ").split(',')
    calificaciones = [float(calificacion.strip()) for calificacion in calificaciones]

    estudiante = Estudiante(nombre, edad, calificaciones)
    return estudiante

# Programa principal
lista_estudiantes = cargar_desde_archivo()

while True:
    print("\n1. Agregar Estudiante")
    print("2. Guardar en Archivo")
    print("3. Cargar desde Archivo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nuevo_estudiante = agregar_estudiante()
        lista_estudiantes.append(nuevo_estudiante)
        print(f"\n{nuevo_estudiante.obtener_informacion()} agregado correctamente.")
    elif opcion == '2':
        guardar_en_archivo(lista_estudiantes)
    elif opcion == '3':
        lista_estudiantes = cargar_desde_archivo()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente de nuevo.")

print("Programa finalizado.")
