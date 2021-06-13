import sys
sys.path.append('c:/Users/ileos/Desktop/tarea-2')
sys.path.append('../')
from message import general_message 

"""
    Cree una clase llamada Producto, con su nombre, precio unitario y cantidad.
    Genere el IVA de ser necesario y calcule el total de la venta de dicho producto.

    Haga una lista de productos y muestrelos como si fuese una factura. Es decir, 
    con su fecha y hora, su precio unitario, y un total de factura.
"""
import datetime

class Product:
    def __init__(self, name, unit_price, quantity):
        self.__name = name
        self.__unit_price = unit_price
        self.__quantity = quantity
        self.__total = self.__calculate_total()  
    
    
    # Methods
    # generate IVA
    #   arg: price to get IVA, it is assumed that IVA's value is 12%
    #   return: price  with IVA include
    def generate_IVA(self, price):
        return price * 0.12
    
    def __calculate_total(self):
        return self.__unit_price * self.__quantity 
    
    
    # Getters and setters
    # For name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    
    # For unit_price
    def get_unit_price(self):
        return self.__unit_price
    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price
    
    # For quantity
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    def get_total(self):
        return self.__total


 
if __name__ == "__main__":
    # general_message()

    # Objects intantiacion
    product_list = [
        Product("Pasta dental Colgate", 3.40, 2),
        Product("Mentol chino", 2.50, 1),
        Product("Cereal Chocapic", 5.25, 3),
        Product("Cerveza Pilsener", 3.40, 5),
        Product("Cepillo de dientes Oral-B", 3.40, 1),
        Product("Atun Real", 1.90, 3)
    ]

    print("Factura N1.")

    today = datetime.datetime.now()
    today = today.strftime("%Y/%m/%d a las %H:%M")
    subtotal = 0
    print("\tFecha: ", today)

    for product in product_list:
        if len(product.get_name()) > 20:
            print("\n", product.get_name()[0:20], end="\t")
        else:
            product_name = product.get_name()
            while( len(product_name) <= 20 ):
               product_name = product_name + ' '     
            print("\n", product_name, end="\t")

        print('{0:.2f}'.format(product.get_unit_price()), end="\t")
        print(product.get_quantity(), end="\t")
        print('{0:.2f}'.format(product.get_total()))    
        subtotal = product.get_total() + subtotal

    print("\t\t\t     Subtotal: {0:.2f}".format(subtotal))
    subtotal_IVA = Product.generate_IVA(product_list.pop(), subtotal) 
    print("\t\t\t     IVA(12%): {0:.2f}".format(subtotal_IVA))
    print("\t\t\t     TOTAL:    {0:.2f}".format(subtotal + subtotal_IVA))