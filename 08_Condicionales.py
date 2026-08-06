### Condicionales ###

my_condition = True

if my_condition: # Si 'my_condition' es 'True' => imprime "sí se cumple"
    print("sí se cumple") # Texto dentro de la condición
print("la ejecucion continua") # Texto fuera de la condicion

my_condition = False

if my_condition: # Si 'my_condition' es 'False' => no imprime "sí se cumple"
    print("sí se cumple") # como my_condition es False esto no se imprimira
print("la ejecucion continua")


my_condition = int(input("Ingrese un valor: ")) # el usuario ingresa un valor entero para my_condition

if my_condition == 10: 
    print("tu número es 10")

if my_condition > 10:
    print("Tu número es mayor que 10")

if my_condition < 10:
    print("Tu número es menor que 10")
# Si una condicion no se cumple, no imprimira el texto
print("La ejecución continua")


# else
# Si no se comple la condicion del 'if', entonces se cumplira la condicion del 'else'
my_condition = int(input("Ingrese otro valor: ")) 
if my_condition < 20:
    print("Tu número es menor que 20")
else:
    print("Tu número es mayor o igual que 20") # Si el numero no es menor que 20 se imprimira esto
print("La ejecución continua")


# Condicionales con operadores logicos
my_condition = int(input("Ingrese otro valor: ")) # digite un valor entero
if my_condition > 10 and my_condition < 20: # si se se cumple que (10 < my_condition < 20) imprime:
    print("Tu número es mayor que 10 y menor a 20")
else: # si no se cumple lo contrario (10 >= my_condition or 20 <= my_condition) 
    print("Es menor o igual a 10 o mayor igual que 20")
print("La ejecución continua")

# elif
# else + if
# Antes si no se cumplía la condición del 'if', por defecto se cumplía la condición del 'else'
# Ahora si no se cumple la condición del 'if', va a comprobar con todas las condiciones de todos los 'elif'
my_condition = int(input("Ingrese otro valor: ")) # digite un valor entero
if my_condition > 2 and my_condition < 8: #Condición del 'if'
    print("Tu número es mayor que 2 y menor que 8")
elif my_condition == 1: #Condición del 'elif'
    print("Tu número es 1")
elif my_condition == 9 or my_condition == 10: #Condición del otro 'elif'
    print("Tu número es 9 o 10")
else: #Condición del 'else'
    print("Tu número es mayor que 10")


my_string = "Hola a todos"
if my_string: # Si la cadena de texto no esta vacía imprime su condición (True)
    print("Mi string no está vacío")
print("La ejecución continua")

my_string = ""
if my_string: # La cadena de texto esta vacía (False)
    print("Mi string no está vacío")
print("La ejecución continua")

    
    



