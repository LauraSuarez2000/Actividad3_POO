#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto 
#Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:
    PINTAS = ("Corazones", "Diamantes", "Tréboles", "Picas")

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# uso
valor_carta = "As"
pinta_carta = Carta.PINTAS[0]  # Corazones
carta = Carta(valor_carta, pinta_carta)

print(f"Valor de la carta: {carta.valor}")
print(f"Pinta de la carta: {carta.pinta}")
