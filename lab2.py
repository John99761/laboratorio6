
class animales:
    def __init__(self,edad, nombre, raza):
        self.edad = edad
        self.nombre = nombre
        self.raza = raza
     
animal1=animales("2","MAX","Labrador Retriever")
animal2=animales("1","Sadie","Boxer")
animal3=animales("5","Bailey","Bulldog Francés Retriever")

print("Animal 1:")
print("Nombre:", animal1.nombre)
print("Edad:", animal1.edad)
print("Raza:", animal1.raza)
print()

print("Animal 2:")
print("Nombre:", animal2.nombre)
print("Edad:", animal2.edad)
print("Raza:", animal2.raza)
print()

print("Animal 3:")
print("Nombre:", animal3.nombre)
print("Edad:", animal3.edad)
print("Raza:", animal3.raza)


        
