class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            return True
        else:
            return False

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        return cuota

    def mostrar_detalles(self):
        print(" Número de la cuenta: ", self.numero_cuenta)
        print(" Propietarios: ", self.propietarios)
        print(" Balance: ", self.balance)


cuenta1 = CuentaBancaria("4272-2825-7877-3399", [" Tomás López ", " Angela Vasquez "], 250000 )
cuenta1.mostrar_detalles()
