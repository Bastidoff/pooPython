class Cuenta:
    def __init__(self,numeroCuenta,saldo):
        self.numeroCuenta=numeroCuenta
        self.saldo=saldo
        
    def consultarSaldo(self):
        print (f"El saldo es: {self.saldo}")
        
    def ingresar(self,consignacion):
        self.saldo=self.saldo+consignacion
        print(f"Valar Doaheris! Consignación exitosa! El nuevo saldo es: {self.saldo}")
        
    def retirar(self,retiro):
        if(self.saldo>=retiro):
            self.saldo=self.saldo-retiro
            print(f"Valar Doaheris! Retiro exitoso. El nuevo saldo es: {self.saldo}")
        else:
            print(f"Valar Morghulis! No se pudo realizar el retiro. No cuenta con fondos suficientes.")