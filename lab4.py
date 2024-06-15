
class Empleado:
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
    
    
    
    def mostral_salario(self):
        print(f"El salario de {self.nombre} es: {self.salario}")


Empleado1= Empleado ("Antonio",25000)
Empleado2 = Empleado ("Maria",15000)

Empleado1.mostral_salario()
Empleado2.mostral_salario()