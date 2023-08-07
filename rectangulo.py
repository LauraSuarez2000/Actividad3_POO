
#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. 

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, punto_superior_izquierdo, punto_inferior_derecho):
        self.punto_superior_izquierdo = punto_superior_izquierdo
        self.punto_inferior_derecho = punto_inferior_derecho
#Agregue métodos a la clase Rectángulo para calcular su perímetro,

    def calcular_perímetro(self):
        base = abs(self.punto_inferior_derecho.x - self.punto_superior_izquierdo.x)
        altura = abs(self.punto_inferior_derecho.y - self.punto_superior_izquierdo.y)
        return 2 * (base + altura)
    
# calcular su área 
    def calcular_área(self):
        base = abs(self.punto_inferior_derecho.x - self.punto_superior_izquierdo.x)
        altura = abs(self.punto_inferior_derecho.y - self.punto_superior_izquierdo.y)
        return base * altura
    
#indicar si el rectángulo es un cuadrado.
    def es_cuadrado(self):
        base = abs(self.punto_inferior_derecho.x - self.punto_superior_izquierdo.x)
        altura = abs(self.punto_inferior_derecho.y - self.punto_superior_izquierdo.y)
        return base == altura


punto_superior_izquierdo = Punto(2, 5)
punto_inferior_derecho = Punto(8, 2)
rectangulo = Rectángulo(punto_superior_izquierdo, punto_inferior_derecho)

perímetro = rectangulo.calcular_perímetro()
print(f"Perímetro del rectángulo: {perímetro}")

área = rectangulo.calcular_área()
print(f"Área del rectángulo: {área}")

if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado.")
else:
    print("El rectángulo no es un cuadrado.")
