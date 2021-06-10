import sys
sys.path.append('../')
from message import general_message 

import datetime


class Animal:
    __age = int(0)
    def __init__(self, name, type_, is_vertebrate, birth_date):
        self.__name = name
        self.__type = type_
        self.__is_vertebrate = is_vertebrate
        self.__birth_date = self.__str_to_datetime(birth_date)
        self.__calculate_age()  # To calculate age of animal 
   
    # Methods
    # For calculate age of the animal 
    def __calculate_age(self):
        days_in_year = 365.2425
         
        self.__age = int((
                (datetime.date.today() - self.__birth_date).days / days_in_year
            ))     
        
    def __str_to_datetime(self, str_):
        return datetime.datetime.strptime(str_, "%Y/%m/%d").date() 
    
    # Getters an setters    
    # For name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name  
    
    # For type
    def get_type(self):
        return self.__type
    def set_type(self, type_):
        self.__type = type_  

    # For is vertebrate
    def is_vertebrate(self):
        return self.__is_vertebrate
    # The set method to change if is vertebrate or not, doesn't correspond to real life.
    # But, for this exercise, this aproach will be discard.
    def set_is_vertebrate(self, is_vertebrate):
        self.__is_vertebrate = is_vertebrate

    # For birth date 
    def get_birth_date(self):
        return self.__birth_date
    # The set method to change birth date, doesn't correspond to real life a priori.
    # But, for this exercise, this aproach will be discard.   
    def set_birth_date(self, birth_date):
        self.__birth_date = self.__str_to_datetime(birth_date) 
        self.__calculate_age()
    
    # For age
    def get_age(self):
        return self.__age 

 
"""
    Cree una clase llamada Animales, con atributos de nombre, tipo (Mamifero, anfibio, etc.), si
    es vertebrado o no, fecha de nacimiento y edad.
    
    La edad debe sobreentenderse a partir de la fecha de nacimiento.
    La clase debe poseer getters y setters.
    
    Debe hacer una lista de objetos de tipo animal, a parir de la entrada en consola.
    Despues, muestre a lodos los animales en order de edades (del menor al mayor).
"""

if __name__ == "__main__":
    general_message()

    animal = Animal("Mishifu", "Mamifero", True, "2020/06/06")

    print(animal.calculate_age())
    
    