from Producto import Producto

opcion=100

print("*****Supermercado TBK****")
print("0. Salir")
print("1. Ingresar Producto")
print("2. Mostrar Productos")
print("3. Editar Precio de un Producto")
print("4. Eliminar Producto")

productos=[]

while opcion!=0:    
    opcion=int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        codigo=input("Ingrese el código del producto: ")
        nombre=input("Ingrese el nombre del producto: ")
        precio=int(input("Ingrese el precio del producto: "))
        producto=Producto(codigo,nombre,precio)
        productos.append(producto)
    
    elif opcion == 2:
        for producto in productos:
            print(f"Producto {producto.codigo}")
            producto.mostrar()
            print("__________________")

    elif opcion == 3:
        productoBusqueda=input("Ingrese el código del producto que desea editar su precio: ")
        for producto in productos:
            encontrado=False
            if producto.codigo==productoBusqueda:
                producto.precio=int(input("Ingrese el nuevo precio del producto: "))
                encontrado=True
                break
        if encontrado:
            print("¡El precio del producto fue cambiado con éxito!")
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 4:
        productoBusqueda=input("Ingrese el código del producto que desea eliminar: ")
        for producto in productos:
            encontrado=False
            if producto.codigo==productoBusqueda:
                eliminado=producto
                productos.remove(producto)
                encontrado=True
                break
        if encontrado:
            print(f"El producto {eliminado.nombre} fue eliminado con éxito.")
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción válida.")