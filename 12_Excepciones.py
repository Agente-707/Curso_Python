### Gestión de excepciones ###

numberOne = 2
numberTwo = 5

print(numberTwo + numberOne) # Operación válida

#Pasamos 'numberTwo' de 'int' a 'str'
numberTwo = "1"
# print(numberTwo + numberOne) => Error: No se puede sumar un entero con un string

'''
Nota:
Podemos controlar este error
usando condicionales
'''

# Controlando error con condicionales

if type(numberTwo) == int: # type(numberTwo) = str => No se cumple
    print(numberOne + numberTwo) # No se ejecuta el error
else:
    print("No se cumplió") 
# => "No se cumplió"


'''
Nota:
La mejor práctica para 
controlar errores es usando
'try' y 'except'
'''

# try except

try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error.") # Si no hay error el mensaje se ejecuta y el bloque de 'except' se omite
except:
    print("Se ha producido un error.") # El mensaje se ejecuta si se produce un error en 'try'
# => Se ha producido un error

'''
Nota: 
En este caso, el error se ejecuta pero
nuestro programa no se cierra
'''


# try except else

try:
    print(numberOne + numberTwo) # => Error
    print("No se ha producido un error.") 
except:
    print("Se ha producido un error.") # Si se produce un error este mensaje se ejecuta
else:
    print("La ejeción continúa correctamente.") # El mensaje se ejecuta si no se produce una excepción
# => "Se ha producido un error"

numberTwo = 1 

try:
    print(numberOne + numberTwo) # => Válido
    print("No se ha producido un error.") 
except:
    print("Se ha producido un error.") # Si se produce un error este mensaje se ejecuta
else:
    print("La ejeción continúa correctamente.") # El mensaje se ejecuta si no se produce una excepción
# => 3
# => "No se ha producido un error."
# => "La ejeción continúa correctamente."


# try except else finally

try:
    print(numberOne + numberTwo) # => Válido
    print("No se ha producido un error.") 
except:
    print("Se ha producido un error.") # Si se produce un error este mensaje se ejecuta
else:
    print("La ejeción continúa correctamente.") # El mensaje se ejecuta si no se produce una excepción
finally:
    print("La ejecución continúa") # El mensaje siempre se ejecuta
# => 3
# => "No se ha producido un error."
# => "La ejeción continúa correctamente."
# => "La ejecución continúa"

numberTwo = "1"

try:
    print(numberOne + numberTwo) # => Error
    print("No se ha producido un error.") 
except:
    print("Se ha producido un error.") # Si se produce un error este mensaje se ejecuta
else:
    print("La ejeción continúa correctamente.") # El mensaje se ejecuta si no se produce una excepción
finally:
    print("La ejecución continúa") # El mensaje siempre se ejecuta
# => "Se ha producido un error."
# => "La ejecución continúa"

'''
Nota:
Dentro de esta estructura
'try - except - else - finally'
podemos omitir 'else' o 'finally'
pero no 'try' ni 'except'
'''


# Excepciones por tipo

# print(numberOne + numberTwo) => No salta un error 'TypeError'
try:
    print(numberOne + numberTwo) 
    print("No se ha producido un error.") # Si no hay error el mensaje se ejecuta y el bloque de 'except' se omite
except TypeError:
    print("Se ha producido un TypeError") # El mensaje se ejecuta si se produce un error de tipo 'TypeError'
except ValueError:
    print("Se ha producido un ValueError") # El mensaje se ejecuta si se produce un error de tipo 'ValueError'


# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error.")
except ValueError as ERROR: # => Nombre de la variable que guarda el error "ERROR"
    print(ERROR) # Imprime la informacion del error 
except Exception as my_random_error_name:
    print(my_random_error_name) # Imprime la excepción generica capturada

