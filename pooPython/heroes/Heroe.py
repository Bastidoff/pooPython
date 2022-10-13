#En la clase defino mi molde, lo describo
class Heroe:
    #En PYTHON se declaran y se inicializan los atributos dentro del método constructor
    
    #CONSTRUCTOR
    def __init__(self, nombre, fuerza):
        #creamos los atributos y los inicializamos con los valores que nos llegan como parámetros
        self.nombre=nombre
        self.fuerza=fuerza
    
    
    #Métodos
    def saludar(self):
        print("Hola soy: ", self.nombre)
        
        