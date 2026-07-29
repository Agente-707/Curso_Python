# Variables

# string
my_string = "My String Variable"
print(my_string)

# int
my_int = 10
print(my_int)

# float
my_float = 5.3
print(my_float)

# boolean
my_boolean = True
print(my_boolean)

# concatenacion de variables
print(my_string, my_int, my_float, my_boolean);
print("Este es el valor de:", my_int)

# type
print(type(my_string)) # tipo 'str'
print(type(my_int)) # tipo 'int'
print(type(my_float)) # tipo 'float'
print(type(my_boolean)) # tipo 'bool'
print(type(print(my_string, my_int, my_float, my_boolean))) # tipo 'NoneType'

# str 
my_int_to_string = str(my_int)
print(type(my_int_to_string))
my_float_to_string = str(my_float)
print(type(my_float_to_string))

# Algunas Funciones
print(len(my_string))

# Variables en una sola linea
nombre, apellido, alias, edad = "Luis", "Pareja", "Agente-707", 19
print("Me llamo", nombre, apellido, "mi edad es", edad, ". Y mi alias es ", alias)

# inputs
name = input("Cual es tu nombre?: ")
age = input("Cuantos años tienes?: ")
print(name)
print(age)

# Cambio de variables
name = 19
age = "Luis"
print(name)
print(age)
