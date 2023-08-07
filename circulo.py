#Cree una clase Circulo que tenga las propiedades centro y radio las cuales se inicializan con parámetros en el constructor. 

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

#Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

    def calcular_area(self):
        return 3.14159 * self.radio**2  # Usando el valor aproximado de pi

    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio  # Usando el valor aproximado de pi

    def punto_pertenece(self, punto):
        distancia_al_centro = ((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)**0.5
        return distancia_al_centro <= self.radio

# uso

centro = Punto(0, 0)
radio = 5
circulo = Circulo(centro, radio)

area = circulo.calcular_area()
print(f"Área del círculo: {area}")

perimetro = circulo.calcular_perimetro()
print(f"Perímetro del círculo: {perimetro}")

punto_a_evaluar = Punto(3, 4)
if circulo.punto_pertenece(punto_a_evaluar):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")
