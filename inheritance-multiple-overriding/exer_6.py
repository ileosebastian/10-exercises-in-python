import sys
sys.path.append('c:/Users/ileos/Desktop/tarea-2')
sys.path.append('../')
from message import general_message 


"""
    Realice una clase llamada Perosna, la cual tenga lo siguuiente:
        - att: nombres y apellidos, cedula, fecha de nacimiento, edad (autocalculada)
        - metodos: getters and setters, calculo de la edad, describir todos los atributos
    
    Luego, herede esa clase a otra llamada Estudiante, la cual tenga, por si misma, lo siguiente:
        - att: universidad a la que pertenece, anios de estudio, semestre, materia favorita
        - met: getters y setters, mensaje que muestre si se tiene que preparar ya para la tesis de grado
            describir TODOS los atributos
     
     Muestre un objeto de una persona y otro de estudiate. Modifique el semestre y anio de estudio
     de tal forma que muestre el mensaje de que se tiene que preoparar la la tesis.
"""
import datetime
class Person:
    def __init__(self, fname, lname, ci, birth_date):
        self.__fname = fname
        self.__lname = lname
        self.__ci = ci
        self.__birth_date = self.__str_to_datetime(birth_date) 
        self.__age = self.__calculate_age()
    
    # Methods
    def __calculate_age(self):
        days_in_year = 365.2425
         
        return int((
                (datetime.date.today() - self.__birth_date).days / days_in_year
            ))  
    def __str_to_datetime(self, str_):
        return datetime.datetime.strptime(str_, "%Y/%m/%d").date()
    
    def describe(self, name):
        print(
            """
                La {} con los nombres {} {}, cedula de identidad {}, anio de 
                nacimiento {} y edad de {} anios. Te saluda!
            """.format(
                name,
                self.get_fname(),
                self.get_lname(),
                self.get_ci(),
                self.get_birth_date(),
                self.get_age() 
            )
        )
    
    # Getters and setters
    
    def get_fname(self):
        return self.__fname
    def set_fname(self, value):
        self.__fname = value
     
    def get_lname(self):
        return self.__lname
    def set_lname(self, value):
        self.__lname = value

    def get_ci(self):
        return self.__ci
    def set_ci(self, value):
        self.__ci = value
    
    def get_birth_date(self):
        return self.__birth_date
    def set_birth_date(self, value):
        self.__birth_date = value
    
    def get_age(self):
        return self.__age

""" Class Student that desbribe a person to study """
class Student(Person):
    def __init__(self, fname, lname, ci, birth_date, n_uni, semester, years_study, fav_subj):
        super().__init__(fname, lname, ci, birth_date)
        self.__n_uni = n_uni
        self.__semester = semester
        self.__years_study = years_study
        self.__fav_subj = fav_subj
    
    # Methods
    # New methods
    def check_if_tesis_began(self):
        if int(self.get_semester()) >= 8:
            print(
                """
                    Este estudiante, {}, debe estar empezando a hacer la tesis para su graduacion!
                """.format(
                    self.get_fname()
                )
            )
    
    # overriding describe method
    def describe(self, name):
        super().describe(name)    
        print(
            """
                Tambien es el {}, de la {}, va en el semestre {}, y lleva estudiando {} anios.
                Su materia favorita es {}
            """.format(
                name,
                self.get_n_uni(),
                self.get_semester(),
                self.get_years_study(),
                self.get_fav_subj()
            )
        )
        
    # Getters and setters
    def get_n_uni(self):
        return self.__n_uni
    def set_n_uni(self, value):
        self.__n_uni = value
    
    def get_semester(self):
        return self.__semester
    def set_semester(self, value):
        self.__semester = value
    
    def get_years_study(self):
        return self.__years_study
    def set_years_study(self, value):
        self.__years_study = value
    
    def get_fav_subj(self):
        return self.__fav_subj
    def set_fav_subj(self, value):
        self.__fav_subj = value


if __name__ == "__main__":
    general_message()

    person_1 = Person(
        "Pepe Francisco",
        "Perez Aguilar",
        '1313211234',
        '1999/01/13' 
    )

    person_1.describe("Persona 1")

    student_1 = Student(
        "Leo Sebastian",
        "Intriago Zambrano",
        '1317889549',
        '2001/05/19',
        "Universidad Tecnica de Manabi",
        6,
        3,
        "Analisis y disenio de sistemas"
    )

    student_1.describe("Estudiante 1")
    
    student_1.set_semester(int(input(
            "Usted va a cambiar de semestre del estudiante {}: ".format(student_1.get_fname())
        )))
    
    student_1.check_if_tesis_began()