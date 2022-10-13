from Operacion import Operacion

opcion=100

print("*****Calculadora****")
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
operacion=Operacion(numero1,numero2)

print("0. Salir")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

while opcion!=0:    
    opcion=int(input("Ingrese la opción de la operación que desea realizar: "))
    
    if opcion==1:
        print(f"La suma entre {numero1} y {numero2} es {operacion.sumar()}")
        
    elif opcion==2:
        print(f"La resta entre {numero1} y {numero2} es {operacion.restar()}")
    elif opcion==3:
        print(f"El producto entre {numero1} y {numero2} es {operacion.multiplicar()}")
    elif opcion==4:
        if numero2==0:
            print("ERROR: No se puede dividir entre cero.")            
        else:
            print(f"El cociente entre {numero1} y {numero2} es {operacion.dividir()}")
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción válida.")
    