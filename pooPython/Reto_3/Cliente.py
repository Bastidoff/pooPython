from Cuenta import Cuenta

class Cliente:
    def __init__(self,nombre,apellido,cedula):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        
    def crearCuenta():
        numeroCuenta=input("Ingrese el número de la cuenta: ")
        saldo=float(input("Ingrese el saldo: "))        
        ahorros=Cuenta(numeroCuenta,saldo)
        return ahorros
        