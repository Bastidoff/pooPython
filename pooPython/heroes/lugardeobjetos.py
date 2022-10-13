#aquí utilizo la clase creando objetos
#debemos importar la clase para crear los objetos
from Heroe import Heroe

#utilizamos la clazse creando un objeto de esta misma

#Un Objeto es una VARIABLE
objetoHeroe=Heroe("Goku",99)

#creamos objetos para poder acceder a los métodos y atributos de la clase
print(objetoHeroe.nombre)
print(objetoHeroe.fuerza)
objetoHeroe.saludar()
