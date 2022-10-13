from Cliente import Cliente

opcion=100

print("*****Banco de Hierro de Braavos****")

nombre=input("Ingrese el nombre del cliente")
apellido=input("Ingrese el apellido del cielnte: ")
cedula=input("Ingrese la cédula del cliente: ")
cliente=Cliente(nombre,apellido,cedula)
cuentaCliente=Cliente.crearCuenta()

print("*****Banco de Hierro de Braavos****")



while opcion!=0:
    print("0. Salir")
    print("1. Consultar Saldo")
    print("2. Ingresar dinero a la cuenta")
    print("3. Retirrar dinero de la cuenta")
    opcion=int(input("Qué desea realizar: "))
    if opcion==1:
        cuentaCliente.consultarSaldo()
    elif opcion==2:
        consignacion=float(input("Ingrese la cantidad que desea ingresar: "))
        cuentaCliente.ingresar(consignacion)
    elif opcion==3:
        retiro=float(input("Ingrese la cantidad que desea retirar: "))
        cuentaCliente.retirar(retiro)
    elif opcion==0:
        break
    else:
        print("Ingrese una opción válida.")