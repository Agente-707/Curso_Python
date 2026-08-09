### Variables ###

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
my_boolean = True # True o False
print(my_boolean)

'''
Nota: En python no existe el tipo de dato 'char',
ni el tipo de dato 'double', ni el tipo de dato 'long'.
'''

# concatenacion de variables
print(my_string, my_int, my_float, my_boolean);
print("Este es el valor de:", my_int)

# type
# Imprime el tipo de variable
print(type(my_string)) # tipo 'str'
print(type(my_int)) # tipo 'int'
print(type(my_float)) # tipo 'float'
print(type(my_boolean)) # tipo 'bool'
print(type(print(my_string, my_int, my_float, my_boolean))) # tipo 'NoneType'

# str 
# Transforma cualquier variable a un string
my_int_to_string = str(my_int) # int => string
print(type(my_int_to_string))
my_float_to_string = str(my_float) # float => string
print(type(my_float_to_string))

# Algunas Funciones
# 'len' cuenta la cantidad de caracter de un string
print(len(my_string))
print(len(my_int_to_string))
print(len(my_float_to_string))

# Variables en una sola linea
nombre, apellido, nombre_usuario, edad = "Luis", "Pareja", "Agente-707", 19
# nombre = "Luis"
# apellido = "Pareja"
# alias = "Agente-707"
# edad = 19
print("Me llamo", nombre, apellido, "mi edad es", edad, ". Y mi nombre de usuario es ", nombre_usuario) 
# Podemos concatenar strings y otras variables separandolas por comas dentro del print.

# input
# Con el input puedes asignar valores a las variables desde la ejecución del código  
name = input("Cual es tu nombre?: ") # Pide al usuario que ingrese su nombre
age = input("Cuantos años tienes?: ") # Pide al usuario que ingrese su edad
print(name)
print(age)

# Cambio de variables
name = 19
age = "Luis"
print(name)
print(age)
'''
Nota: En Python puedes cambiar el tipo de variable 
      a una que ya hayas asignado anteriormente sin
      ningun problema.
      - name = "Luis" => name = 19 (cambio de string a entero)
      - age = 19      => age = "Luis" (cambio de entero a string) 
'''
