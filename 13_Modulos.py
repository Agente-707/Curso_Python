### Modulos ###

'''
Con los módulos podemos llamar
directamente a cualquier función
que creemos en otro archivo 
'''

# Formas de llamar a una función de un módulo

import my_module # Importamos nuestro modulo 'my_module'

my_module.sumValue(5, 3, 1) # Llamo a la función 'suma' del archivo 'my_module.py'
my_module.printValue("Hola Python!") # Llamo a la función 'printValue' del archivo 'my_module.py'


# Otra forma
from my_module import sumValue, printValue

# LLamamos directamente a las funciones de 'my_module'
sumValue(5,3,1) 
printValue("Hola python!")


# Módulos del sistema de Python

# Módulo math
import math

''' 
'math' es un módulo que nos da el 
acceso a diversas notaciones y 
operaciones matemáticas
'''

print(math.pi) # valor de pi
print(math.sin(45)) # seno
print(math.cosh(5)) # Coseno hiperbólico
print(math.pow(2,5)) # Potencia

from math import pi as PI_VALUE # Renombramos pi a 'PI_VALUE'

print(PI_VALUE)

# Módulo random
import random
'''
'random' es un módulo que nos da 
acceso a diversos recursos para
realizar elecciones aleatorias
'''

print(random.choices("Agente-707")) # => Me devuelve una letra aleatoria del string
print(random.randrange(2,7)) # Me devuelve un número aleatorio dentro del rango de 2 a 7