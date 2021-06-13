import sys
sys.path.append('c:/Users/ileos/Desktop/tarea-2')
sys.path.append('../')
from message import general_message 

"""
    Crear una clase llamada Restaurante, la cual tenga atributos como: nombre y
    tipo de cocina, hora de apertura y hora de cierre. Tambien debe tener dos metodos:
    Uno que describa al restaurante, y otro que indique si esta abierto o no a partir de su 
    horario de apertura y cierre. 

    Cree dos objetos de esta clase, mostrando todos sus atributos y sus metodos.
   
    Cambie la hora de cierre de cualquier restaurante instanciado como entrada
    en la consola. Esta abierto dicho restaurante?  
"""
import datetime

class Restaurant:
    def __init__(self, name, cuisine_type, opening_time, closing_time):
        self.__name = name 
        self.__cuisine_type = cuisine_type
        self.__opening_time = opening_time 
        self.__closing_time = closing_time

    # Methods
    def desctiption(self):
        return 'El restaurante {}, de cocina "{}", abre desde las {} hasta las {} horas.'.format(
                self.__name, 
                self.__cuisine_type, 
                self.str_to_datetime(self.__opening_time), 
                self.str_to_datetime(self.__closing_time)
            ) 
    
    def isOpen(self):
        current_time = datetime.datetime.now().time()
        opening = self.str_to_datetime(self.__opening_time)
        closing = self.str_to_datetime(self.__closing_time)

        if opening > closing and opening >= current_time <= closing:  
            return True
        elif opening < closing and not opening >= current_time <= closing:
            return True
        else:
            return False
    
    # Other methods
    def str_to_datetime(self, str):
        return datetime.datetime.strptime(str, '%H:%M').time()

    # Getters and Setters
    # For name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    # For cuisine type
    def get_cuisine_type(self):
        return self.__cuisine_type
    def set_cuisine_type(self, cuisine_type):
        self.__cuisine_type = cuisine_type

    # For opering time
    def get_opening_time(self):
        return self.__opening_time
    def set_opening_time(self, opening_time):
        self.__opening_time = opening_time

    # For closing time
    def get_closing_time(self):
        return self.__closing_time
    def set_closing_time(self, closing_time):
        self.__closing_time = closing_time 


if __name__ == "__main__":
    # general_message()

    # Objects Intantiation
    restaurant_1 = Restaurant("La carreta", "Ecuatoriana", "15:00", "20:00")
    restaurant_2 = Restaurant("La traviata", "Italiana", "19:00", "22:00")
    
    # Attributes and methods of each class
    # Restaurant 1:
    print("Restaurante 1") 
    print("\tNombre:", restaurant_1.get_name())
    print("\tTipo de cocina:", restaurant_1.get_cuisine_type())
    print("\tHora de apertura:", restaurant_1.get_opening_time())
    print("\tHora de cierre:", restaurant_1.get_closing_time())

    print("\tDescripcion:\n", "\t", restaurant_1.desctiption())
    answer = "Si" if restaurant_1.isOpen() else "No" 
    print("\tEsta abierto:", answer)

    # Restaurant 2:
    print("Restaurante 2")
    print("\tNombre:", restaurant_2.get_name())
    print("\tTipo de cocina:", restaurant_2.get_cuisine_type())
    print("\tHora de apertura:", restaurant_2.get_opening_time())
    print("\tHora de cierre:", restaurant_2.get_closing_time())

    print("\tDescripcion:\n", "\t", restaurant_2.desctiption())
    answer = "Si" if restaurant_2.isOpen() else "No" 
    print("\tEsta abierto:", answer)

    # Modify closing time attribut and verify if is open
    print("\nModificacion de un atributo")
    new_closing_time = str(input("\tHora de cierre del restaurante 2:"))

    restaurant_2.set_closing_time(new_closing_time)

    print("\tEl nuevo horario de cierre es,entonces, a las", restaurant_2.get_closing_time())    
    
    print("\tEsta abierto:", "Si" if restaurant_2.isOpen() else "No")
    
   
    