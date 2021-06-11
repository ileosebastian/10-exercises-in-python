import sys
sys.path.append('c:/Users/ileos/Desktop/tarea-2')
sys.path.append('../')
from message import general_message 

"""
    Cree una clase llamada vehiculo la cual tenga especialidades como Camnion,
    Carro de Carreras.
    
    Cada uno de estos debe tener metodos y atributos unicos, como:
        Para Camion:
            - atributos nuevos: carga actual (un conjunto de elementos
                ordenados por lo que carga y su peso), peso maximo de carga
            - metodos nuevos: getters y setters de nuevos atributos, agregar nueva carga
                sabiendo que no puede pasarse del peso maximo, describir toda la carga actual. 
       
        Para Carro de carreras:
            - atributos nuevos: pieza para velocidad (Splitter y faldones, aletas, etc.)
            - metodos nuevos: get y set del nuevo atributo, sobreescribir la accion de 
                acelerar y frenar (20% mas rapido), describir los datos de dicha instancia. 
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

    # Describe all atributes
    def describe_all(self, name):
        print(
            """
            El {} posee los siguientes atributos:
                Marca: {},
                Velocidad maxima (Km/h): {},
                Velocidad actual (Km/h): {},
                Kilometraje (Km/h): {}
            """.format(
                name,
                self.get_make(),
                self.get_max_speed(),
                self.get_curr_speed(),
                self.get_mileage()
            )
        )
        
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



""" TRUCK VEHICLE """
from collections import namedtuple
class Truck(Vehicle):
    def __init__(self, make, max_speed, curr_speed, mileage, curr_carry, max_carry_weight):
        super().__init__(make, max_speed, curr_speed, mileage)
        self.__carry = namedtuple('Carry', ['carry_name', 'weight'])
        
        response = self.__is_overflow(curr_carry, max_carry_weight)
        if response:
            raise Exception("No puede instanciar superando la carga maxima declarada.")
        
        self.__curr_carry = curr_carry
        self.__max_carry_weight = max_carry_weight
    
    
    def describe_all(self, name):
        super().describe_all(name)
        self.describe_carry()
        
        
    # Add new carry
    # args: new_carry is a tuple("carry came", weight)
    def add_carry(self, new_carry):
        if len(new_carry) == 2 and not self.__is_overflow_to(new_carry):
            self.__curr_carry.append(new_carry)  
            print("\tCarga agregada con exito!")
        else:
            print("\tCarga no permitida, por maximo de peso ingreso invalido de datos.")
    
    def describe_carry(self):
        n = 1
        for item in self.__curr_carry:
            print("\tCarga ", n)
            i = self.__carry(*item)
            print("\t\tNombre de carga:", i.carry_name)
            print("\t\tPeso que ocupa", i.weight)
            n += 1
        print("\t\t\tPESO TOTAL DE LA CARGA ACTUAL:", self.__calculate_weight(self.__curr_carry))
        print("\t\t\tPESO MAXIMO:", self.get_max_carry_weight())

    # args a tuple  
    def __is_overflow(self, carry, max_weight):
        if self.__calculate_weight(carry) > max_weight:
            return True
        else:
            return False 
        
    # args a tuple 
    def __is_overflow_to(self, new_carry):
        carry = self.__carry(*new_carry) 
        new_weight = carry.weight
        curr_weight = self.__calculate_weight(self.__curr_carry)
        if (new_weight + curr_weight) > self.__max_carry_weight:
            return True
        else:
            return False
        
    # args: a list of tuple
    def __calculate_weight(self, carry):
        return sum([self.__carry(*item).weight for item in carry]) 
    
    # Getter and setters
    # For current carry
    def get_curr_carry(self):
        return self.__curr_carry
    def set_curr_carry(self, values):
        self.__curr_carry = values
    
    # For max carry weight 
    def get_max_carry_weight(self): 
        return self.__max_carry_weight
    def set_max_carry_weight(self, value):
        self.__max_carry_weight = value 


class Racecar(Vehicle):
    def __init__(self, make, max_speed, curr_speed, mileage, piece_for_speed="Ninguna"):
        super().__init__(make, max_speed, curr_speed, mileage)
        self.__piece_for_speed = piece_for_speed
        
        
    # Methods
    # Overriding methods
    # To accelerate
    def accelerate(self, speed_increase):
        speed_changed = self.get_curr_speed() + speed_increase
        speed_changed += (speed_changed * 0.20)
        if speed_changed > self.get_max_speed():
            print("Este incremento es mas de lo que el auto de carreras {} puede hacer".format(
                self.get_make()
            ))
        else:
            self.set_curr_speed(speed_changed)
            print("Velocidad incrementada! Ahora va a {} km/h.".format(self.get_curr_speed()))
            self.set_mileage(int(self._Vehicle__mileage + speed_changed))
        
    # To slow down
    def slowing_down(self, speed_decrease):
        speed_changed = self.get_curr_speed() + speed_decrease
        speed_changed -= (speed_changed * 0.20)
        if speed_changed < self._Vehicle__min_speed:
            print("Este decremento es menos de lo que el auto de carreras {} puede hacer".format(
                self.get_make()
            ))
        else:
            self.set_curr_speed(speed_changed)
            print("Velocidad decrementada, ahora va a {} km/h.".format(self.get_curr_speed()))

    # describe all
    def describe_all(self, name):
        super().describe_all(name) 
        print("\t\tPieza para mejorar aerodinamica:", self.get_piece_for_speed())
        
        
    # Getters and setters
    # For piece for improve speed
    def get_piece_for_speed(self):
        return self.__piece_for_speed
    def set_piece_for_speed(self, value):
        self.__piece_for_speed = value 
            


if __name__ == "__main__":
    general_message() 

    # For truck 
    carry_1 = [
       ("Lana", 100),
       ("Trigo",200) 
    ]
    truck_1 = Truck(
        "Mazda",
        200,
        0,
        1200,
        carry_1,
        400
    )

    truck_1.describe_all("Camionsito 1")

    extra_carry = ("Paja", 300)
    print("Inrgesa el siguiente peso al camnion:", extra_carry) 
    truck_1.add_carry(extra_carry)

    correct_carry = ("Carne", 100)
    print("Inrgesa el siguiente peso al camnion:", correct_carry) 
    truck_1.add_carry(correct_carry)

    truck_1.describe_all("Camion 1 -actualizado-")    

    # For Racecar
    racecar_1 = Racecar(
        "Ferrari",
        400,
        100,
        4000
    )

    racecar_1.describe_all("Carro de carreras")

    racecar_1.accelerate(100)

    racecar_1.describe_all("Carro de carreras -actualizado-")
    