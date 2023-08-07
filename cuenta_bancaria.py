
#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron {cantidad} en la cuenta.")

#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron {cantidad} de la cuenta.")
        else:
            print("No se pudo realizar el retiro debido a fondos insuficientes.")

#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2%: {cuota}")

#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
    def mostrar_detalles(self):
        print("Detalles de la cuenta bancaria:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance actual: {self.balance}")

# Uso
numero_cuenta = "123456789"
propietarios = ["Juan Pérez", "María Gómez"]
balance_inicial = 1000.0

cuenta = CuentaBancaria(numero_cuenta, propietarios, balance_inicial)
cuenta.mostrar_detalles()

cuenta.depositar(500)
cuenta.mostrar_detalles()

cuenta.retirar(300)
cuenta.mostrar_detalles()

cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()
