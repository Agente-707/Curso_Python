### Functions ###

# La palabra reservada para definir funciones es 'def'
def my_function (): # Nombre de la función: 'my_function'
    print("Esto es una función.")
# 'my_function' imprime un string => "Esto es una función." 

my_function () # => Llamamos a la función


# Función con parametros
def suma (first_number, second_number): # Función 'suma' con dos parametros 
    print(first_number + second_number) # Imprime la suma de los dos parametros

# Cuando llamamos a la función tenemos que pasarle dos valores para los dos parametros
suma(3,7) # => fist_number = 3 + second_number = 7
suma(2.5,10)
suma(3.5,3.5)
suma("Hola", " mundo") # Concatenación de strings

def resta (first_number, second_number):
    print(first_number - second_number)

print(10,4)
print(2,19)
print(2.3,10)
#print("hola","mundo") Error: Los strings no se pueden restar

# Asignando tipo de variable para los parametros
def suma (first_number: int, second_number: int): # first_number: int => primer número entero
    print(first_number + second_number)           # Second_number: int => segundo número entero

suma(3.4,1.23) # La llamada es correcta (ignora la asignación de ambos parametros con :int)
suma("3","5") # => Incluso funciona con strings

'''
Nota: Al final no sirve de mucho la asignación por ':',
      nosotros podemos asignar todo tipo de
      variables (strings, floats, etc) dentro de la llamada
      y seguiría siendo válido.
'''

# Función con return
def suma_return (first_value, second_value):
    return first_value + second_value # 'return' nos da el valor de la suma pero no la imprime

suma_return(10,12) # Si llamamos a la función no pasara nada porque no estamos imprimiendo la suma
my_result = suma_return(10,12) # Podemos asignar el valor que nos retorna la función 'suma_return' a una variable
print(my_result)

'''
Nota: 'return' nos retorna un valor el cual podemos asignarle a
       una variable o directamente podemos imprimirla, a diferecia
       de la anterior función 'suma' la cual no nos retornaba ningún
       valor, solo imprimía la suma de los dos parametros
'''

my_result = suma(12,10) # No retorna un valor
print(my_result) # => None

# Función para imprimir tu nombre
def print_name (name, surname):
    print(f"{name, surname}") # Función con formateo

print_name("Pareja","Luis") # Imprime mi nombre pero al revés
print_name(surname="Pareja", name="Luis") # Podemos especificar el orden de llamada de los parametros

# Especificación por defecto
'''
Podemos asignar valores a los parametros por defecto
sin tener que especificarlo cuando llamemos a la función.
'''
def print_name_with_default (name, surname, alias = "Sin alias"): # Asignamos por defecto el valor de 'alias'
    print(f"{name} {surname} {alias}")

print("Luis","Pareja") # El valor de alias, por defecto, es "Sin alias" por lo que no hace falta pasarle el valor

# Parametros dinamicos
# A un parametro con * podemos pasarle varios parametros en la llamada 
def print_texts(*text): # Solo tiene un parametro *text
    print(text)

print_texts("hola","adios","buenas noches","buenos días") # Le pasamos más parametros
# Imprime ('hola', 'adios', 'buenas noches', 'buenos dias')

def print_texts(*texts):
    for text in texts:
        print(text)
        
print_texts("Hola","adios","buenas noches","buenos días")
# Imprime:
# hola
# adios
# buenos noches
# buenos días


