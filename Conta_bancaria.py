class Persona():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,num_cuenta,balance):
        super().__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return (f"Cliente {self.nombre} {self.apellido} con No. Cuenta: {self.num_cuenta} "
                f"tiene un balance de: {self.balance}")

    def depositar(self,monto_depositar):
        self.balance+= monto_depositar
        print(f"Saldo disponible: {self.balance}")

    def retirar(self,monto_retirar):
        monto_retirar = float(monto_retirar)
        if monto_retirar > self.balance:
            print(f"Balance insuficiente!!!")
        else:
            self.balance -= monto_retirar
            print(f"Saldo disponible: {self.balance}")

def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    num_cuenta = input("No. de Cuenta: ")
    balance = int(input("Balance: "))

    cliente = Cliente(nombre,apellido,num_cuenta,balance)
    return cliente

def inicio():
    cliente = crear_cliente()

    while True:
        opcion = int(input("""
        [1] Ingresar Saldo
        [2] Retirar Saldo
        [0] Salir
        """))
        if opcion == 1:
            monto_depositar = int(input("Monto a depositar: "))
            cliente.depositar(monto_depositar)
            #print(cliente)

        elif opcion == 2:
            monto_sacar = int(input("Monto a sacar: "))
            cliente.retirar(monto_sacar)
            #print(cliente)
        else:
            break

inicio()



