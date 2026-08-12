### Clases ###


# Clase vacía
class MyEmptyPerson: # Primera letra del nombre de una clase en mayusculas (Camel Case)
    pass # => No hace nada

print(MyEmptyPerson)
print(MyEmptyPerson()) 


# Clase con parametros 'name' y 'surname'
class Person:
    def __init__(self, name, surname): # => Constructor de clase
        self.name = name         # Atributo 'name'
        self.surname = surname   # Atributo 'surname'

'''
Nota: 
Definimos los atributos de la clase 'Person'
con 'self' y les pasamos el valor de los
parametros

'Atributo: self.name  =  Parametro: name'
'Atributo: self.surname  =  Parametro: surname'
'''

my_person = Person("Luis", "Pareja") # Definimos la clase con sus parametros

# llamamos a los atributos  
print(my_person.name)     # => Luis
print(my_person.surname)  # => Pareja


# Clase sin parametros
class MyOtherPerson:
    def __init__(self): # No le pasamos parametros

        # Definimos sus atributos dentro del constructor
        self.name = "Luis"
        self.surname = "Pareja"

my_person = MyOtherPerson() # Definimos la clase sin parametros

# Llamamos a los atributos
print(my_person.name)     # => Luis
print(my_person.surname)  # => Pareja


# Clase con atributo almacenado
class Person2:
    def __init__(self, name, surname): # Clase con dos parametros 'name' y 'surname'
        self.full_name = f"{name} {surname}" # Atributo almacenado 'full_name' trabaja con los dos parametros

my_person = Person2("Luis", "Pareja") # Definimos la clase con sus parametros

# llamamos al atributo
print(my_person.full_name) #  => "Luis Pareja"


# Clase con función
class Person3:
    # Constructor
    def __init__(self, name, surname): 
        self.full_name = f"{name} {surname}"

    # Función 'walk'
    def walk (self): # Sin parametros
        print(f"{self.full_name} está caminando")

my_person = Person3("Luis", "Pareja") # Definimos la clase con sus parametros
print(my_person.full_name) # llamamos al atributo almacenado => "Luis Pareja"
my_person.walk() # Llamamos a la función sin atributos => "Luis Pareja está caminando"

'''
Nota: 
Aparte del constructor dentro del cual 
se definen los atributos, tambien tenemos 
funciones que definen acciones con los
atributos las cuales llamamos 'métodos'
'''


# Otros casos

class Person4:
    def __init__(self, name, surname, alias = "sin alias"): # Agregamos un tercer parametro por defecto
        self.full_name = f"{name} {surname} {alias}"

    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person4("Luis", "Pareja") # Definimos la clase sin el tercer parametro (ya tiene un valor por defecto)
print(my_person.full_name); # => Luis Pareja sin alias
my_person.walk() # => Luis Pareja sin alias está caminando

my_other_person = Person4("Luis", "Pareja", "Agente-707") # Definimos otra variable con la misma clase y le agregamos otro valor para el tercer parametro
print(my_other_person.full_name); #  => Luis Pareja Agente-707
my_other_person.walk() # => Luis Pareja Agente-707 está caminando

my_other_person.full_name = "Noob_Master69"
print(my_other_person.full_name)

'''
Nota: 
Podemos acceder a los atributos de una 
clase y modificarlos sin problemas
'''