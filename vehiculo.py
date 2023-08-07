
#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.


class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
#Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#A la clase del punto anterior, defínale los siguientes métodos:
#Un método mostrar que imprima por consola las coordenadas del punto

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

#Un método mover que cambie las coordenadas del punto
    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y
        
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calcular_distancia(self, otro_punto):
        distancia = ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5
        return distancia

#Uso
vehiculo = Vehículo(200, 5000)
print(f"Velocidad máxima del vehículo: {vehiculo.velocidad_maxima}")
print(f"Kilometraje del vehículo: {vehiculo.kilometraje}")

punto1 = Punto(2, 3)
punto2 = Punto(5, 7)
punto1.mostrar()
punto2.mostrar()

nuevo_x = 8
nuevo_y = 10
punto1.mover(nuevo_x, nuevo_y)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print(f"Distancia entre los puntos: {distancia}")
