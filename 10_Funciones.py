### Functions ###

# La palabra reservada para definir funciones es 'def'
def my_function (): # Nombre de la función: 'my_function'
    print("Esto es una función.")
# 'my_function' imprime un string => "Esto es una función." 

my_function () # => Llamamos a la función


# Funcion con parametros
def suma (first_number, second_number): # Función 'suma' con dos parametros 
    print(first_number + second_number) # Imprime la suma de los dos parametros

suma(3,7) # Cuando llamamos a la función tenemos que pasarle dos valores para los dos parametros
suma(2.5,10)
suma(3.5,3.5)
suma("Hola", " mundo") # Concatenación de strings

# Asignando tipo de variable para los parametros
def suma (first_number: int, second_number: int): # first_number: int => primer número entero
    print(first_number + second_number)           # Second_number: int => segundo número entero

suma(3.4,1.23) # La llamada es correcta (ignora la asignación de ambos parametros con :int)
suma("3","5") # => Incluso con strings

'''
Nota: Al final no sirve de mucho la asignación por ':',
      nosotros podemos asignar todo tipo de
      variables (strings, floats, etc) dentro de la llamada
      y seguiría siendo válido.
'''