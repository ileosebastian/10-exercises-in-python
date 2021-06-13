import sys
sys.path.append('c:/Users/ileos/Desktop/tarea-2')
sys.path.append('../')
from message import general_message

"""
    
"""

class Animal:
    def __init__(self, name, age, is_vertebrate):
        self.__name = name
        self.__age = age
        self.__is_vertebrate = is_vertebrate

    #  this methos will be override
    def action(self):
        pass
    
    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name = value
    
    def get_age(self):
        return self.__age
    def set_age(self, value):
        self.__age = value
    
    def get_is_vertebrate(self):
        return self.__is_vertebrate
    def set_is_vertebrate(self, value):
        self.__is_vertebrate = value    
    
class Bird(Animal):
    def __init__(self, name, age, is_vertebrate=True):
        super().__init__(name, age, is_vertebrate) 
     
    def fly(self):
        print("El/la {} esta volando.".format(self.get_name()))

class Mammal(Animal):
    def __init__(self, name, age, is_vertebrate=True):
        super().__init__(name, age, is_vertebrate)
    
    def run(self):
        print("El/la {} esta corriendo.".format(self.get_name())) 

class Bat(Mammal, Bird):
    def __init__(self, age):
       super().__init__('murcielago', age) 
       
    
    def action(self):
        print("El/la {} hace lo siguiente cuando esta despierto:".format(self.get_name()))
        self.fly()
        self.run()

    def describe(self):
        print(
            """
                El {} es capaz de ver por las noches, tiene {} anios. {}s un animal vertebrado, 
                capaz de realizar diversas acciones, como volar, y correr en las cuevas.
            """.format(
                self.get_name(),
                self.get_age(),
                "E" if self.get_is_vertebrate() else "No e"
            )
        )


if __name__ == "__main__":
    # general_message()

    bat_1 = Bat(3)

    print("\nAcciones de un muercielago.")
    bat_1.action() 

    print("\nDescripcion del murcielago.")
    bat_1.describe()