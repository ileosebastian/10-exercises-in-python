import sys
sys.path.append('../')
from message import general_message 

"""
    Cree una clase llamada Vehiculo, la cual tenga como atributos la marca, la velocidad
    maxima, velocidad actual y su kilometraje. Cada atributo debe tener sus respectivos getters y setters. 
    Ademas, cree una clase que indique que esta acelerando y otra que se esta frenando. 

    Cree dos objetos a partir de la clase. Muestre sus atributos con los que se 
    instrancio y que cada uno ha empesado a acelerar. Luego, modifique el kilometraje 
    de uno de esos atributos y muestre dicho cambio, para terminar desacelerando. 
"""

class Vehicle:
    def __init__(self, make, max_speed, curr_speed, mileage):
        self.__make = make
        self.__max_speed = max_speed
        self.__min_speed = 0
        self.__curr_speed = curr_speed
        self.__mileage = mileage

    # Methods
    # To accelerate
    def accelerate(self, speed_increase):
        if (self.__curr_speed + speed_increase) > self.__max_speed:
            print("Este incremento es mas de lo que el vehiculo {} puede hacer".format(
                self.__make
            ))
        else:
            self.__curr_speed = self.__curr_speed + speed_increase
            print("Velocidad incrementada, ahora va a {} km/h.".format(self.__curr_speed))
        
    # To slow down
    def slowing_down(self, speed_decrease):
        if (self.__curr_speed - speed_decrease) < self.__min_speed:
            print("Este incremento es menos de lo que el vehiculo {} puede hacer".format(
                self.__make
            ))
        else:
            self.__curr_speed = self.__curr_speed - speed_decrease
            print("Velocidad decrementada, ahora va a {} km/h.".format(self.__curr_speed))

        
    # Getters and Setters
    # For make
    def get_make(self):
        return self.__make 
    def set_make(self, make):
        self.__make = make

    # For max_speed
    def get_max_speed(self):
        return self.__max_speed 
    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    # For curr_speed
    def get_curr_speed(self):
        return self.__curr_speed 
    def set_curr_speed(self, curr_speed):
        self.__curr_speed = curr_speed

   # For mileage
    def get_mileage(self):
        return self.__mileage 
    def set_mileage(self, mileage):
        self.__mileage = mileage


if __name__ == "__main__":
    general_message()

    # Objects instantiation
    vehicle_1 = Vehicle("Mazda", 200, 0, 4000)
    vehicle_2 = Vehicle("Ford", 150, 0, 5500)

    # Displaying objects and their methods
    print("Vehiculo 1.") 
    print("\tMarca:", vehicle_1.get_make())
    print("\tVelocidad maxima (Km/h):", vehicle_1.get_max_speed())
    print("\tVelocidad actual (Km/h):", vehicle_1.get_curr_speed())
    print("\tKilometraje (Km/h):", vehicle_1.get_mileage()) 
   
    speed_change_1 = int(input("\tIndique cuanto quiere que acelere (Km/h):"))
    vehicle_1.accelerate(speed_change_1)

    print("\nVehiculo 2.")
    print("\tMarca:", vehicle_2.get_make())
    print("\tVelocidad maxima (Km/h):", vehicle_2.get_max_speed())
    print("\tVelocidad actual (Km/h):", vehicle_2.get_curr_speed())
    print("\tKilometraje (Km/h):", vehicle_2.get_mileage()) 
    
    speed_change_2 = int(input("\tIndique cuanto quiere que acelere (Km/h):")) 
    vehicle_2.accelerate(speed_change_2)

    # Modify speed with set method and display changes
    vehicle_2.set_mileage(int(speed_change_2 + vehicle_2.get_mileage())) 
    print("\t\tSe ha modificado el kilometraje del Vehiculo 2.")
    # Slow down vehicle 2
    speed_change_2 = int(input("\tIndique cuanto quiere que el vehiculo 2 desacelere:"))
    vehicle_2.slowing_down(speed_change_2)
    