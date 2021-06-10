import sys
sys.path.append('../')
from message import general_message

"""
    Cree una clase que realice operaciones basicas (suma, resta, multiplicacion,
    division) y que realice los dichas funciones a partir de pasarle una lista
    de numeros. Es decir, si se le pasa 5 numeros, el objeto instanciado debera
    calcular las operaciens bassicas con cada numero de la lista.

    Debe instanciar un objeto a partir de una lista de numeros. Luego, muestre 
    la lista de numeros y luego un resumen de cada operacion hecha y su respectiva
    solucion.
"""

class Calculator:
    def __init__(self, numbers):
        self.__numbers = numbers
        self.__sum_numbers = 0
        self.__subtraction_numbers = 0
        self.__multiplication_numbers = 0
        self.__division_numbers = 0
        
    
    # Methods
    # sum
    def __sum(self):
       self.__sum_numbers = sum(self.__numbers)
        
    # subrtaction
    def __subtraction(self):
        r = self.__numbers[0]
        for n in self.__numbers[1:]:
            r = r - n
        self.__subtraction_numbers = r

    # multiplication
    def __multiplication(self):
        r = self.__numbers[0]
        for n in self.__numbers[1:]:
            r = r * n 
        self.__multiplication_numbers = r 
     
    # division
    def __division(self):
        r = 0
        if not 0 in self.__numbers:
            r = self.__numbers[0]
            for n in self.__numbers[1:]:
	            r = r / n
        else:
            print("It is not possible to divide a set that has null elements (zeros)")
        self.__division_numbers = r 
    
    def get_summarize(self):
        self.__sum()
        self.__subtraction()
        self.__multiplication()
        self.__division()
        return """
                Suma: {0:.2f},
                Resta: {1:.2f},
                Multiplicacion: {2:.2f},
                Division: {3:.5f}
            """.format(
                self.__sum_numbers,
                self.__subtraction_numbers,
                self.__multiplication_numbers,
                self.__division_numbers
            ) 
    
    # Getters and Setters
    def get_numbers(self):
        return self.__numbers
    def set_numbers(self, numbers):
        self.__numbers = numbers 



if __name__ == "__main__":
    general_message() 

    list_n = [10,23,11,1,33]
    calculator = Calculator(list_n)
    
    print("La lista de numeros a operar es: ", list_n)
    print("\tLas operaciones basicas hechas sobre esta lista son los siguietes:")
    print(calculator.get_summarize())