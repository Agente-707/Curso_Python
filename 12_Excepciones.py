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

# Controlando errores con 'try except'
try:
    print(numberOne + numberTwo) # Si se produce un error se salta al bloque de 'except'
    print("No se ha producido un error") # Si no hay error el mensaje se ejecuta y se salta el bloque de except
except:
    print("Se ha producido un error")
# => Se ha producido un error

'''
Nota: 
En este caso, el error se ejecuta pero
nuestro programa no se cierra
'''


# try except else
