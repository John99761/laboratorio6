
class Forma:
    def calcular_area(self):
        pass


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 7)

print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Área del triángulo: {triangulo.calcular_area()}")




