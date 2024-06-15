
class vehiculo:
    def __init__(self,marca, modelo, color, placa):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.placa=placa

        
    
    def descripcion(self):
        print(f'Modelo: {self.modelo}, Placa: {self.placa}')

auto1=vehiculo("BMW","E46","Rojo","AR25164")
auto2=vehiculo("NISSAN","GTR","Negro","RD456215")
auto3=vehiculo("HONDA","CIVID","Azul","NY546595")

auto1.descripcion()
auto2.descripcion()
auto3.descripcion()


    

        