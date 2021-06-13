# import sys
# sys.path.append('../')
# from message import general_message 

"""
    Cree una clase llamada Animales, con atributos de nombre, tipo (Gato, Chimpace, Pez, etc.), 
    si es vertebrado o no, fecha de nacimiento y edad.
    
    La edad debe sobreentenderse a partir de la fecha de nacimiento.
    La clase debe poseer getters y setters.
    
    Debe hacer una lista de objetos de tipo animal, a parir de la entrada en consola.
    Despues, muestre a lodos los animales en order de edades (del menor al mayor).
"""
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


if __name__ == "__main__":
    # general_message()

    # Objects instantiation
    # data entry
    print("Ingreso de datos de cada animal.")
    animal_list = [] 

    while True:
        print("\nAnimal #", (len(animal_list) + 1))

        name = str(input("\tNombre: "))
        type_ = str(input("\tTipo(Gato, Chimpace, Pez, etc.): "))
        is_vertebrate = True if str(input("\tEs un animal vertebrado [y/n]: ")) == 'y' else False
        birth_date = str(input("\tFecha de nacimiento (yyyy/mm/dd): ")) 
        
        animal = Animal(name, type_, is_vertebrate, birth_date)

        animal_list.append(animal)        
        
        stay_in_loop = True if str(input("\t\tDesea seguir ingresando animales? [y/n]: ")) == 'y' else False
       
        if not stay_in_loop:
            break 
    
    print("\nLos datos ingresados, con edades del menor al mayor, son:") 
    animal_list.sort(key=lambda x: x.get_age())

    for (animal, i) in zip(animal_list, range(0, len(animal_list))):
        print("\nAnimal ", (i+1)) 
        print("\tNombre:", animal.get_name())
        print("\tTipo:", animal.get_type())
        print("\tEs vertebrado?:", "Si" if animal.is_vertebrate() else "No")
        print("\tFecha de nacimiento:", animal.get_birth_date())
        print("\tEdad:", animal.get_age(), "años.")