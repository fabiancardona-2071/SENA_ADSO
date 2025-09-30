class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print(f"hola mi nombre es {self.nombre}y tengo {self.edad} años")
#crear objetos de la clase persona
persona1=Persona("maria",30)
persona2=Persona("jose",25)

persona1.saludar()
persona2.saludar()