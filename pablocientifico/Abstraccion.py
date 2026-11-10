class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


        a1 = Alumno("Ana", 9.2)
        a2 = Alumno("Luis", 5.5)

        a1.mostrar_informacion()
        a2.mostrar_informacion()