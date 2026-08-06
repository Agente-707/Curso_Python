### Condicionales ###

my_condition = True

if my_condition: # Si 'my_condition' es 'True' => imprime "sí se cumple"
    print("sí se cumple")

print("la ejecucion continua") # Texto aparte

my_condition = False

if my_condition: # Si 'my_condition' es 'False' => no imprime "sí se cumple"
    print("sí se cumple")

print("la ejecucion continua")


my_condition = int(input("Ingrese un valor: ")) # el usuario ingresa un valor entero para my_condition

if my_condition == 10: 
    print("tu número es 10")

if my_condition > 10:
    print("Tu número es mayor que 10")

if my_condition < 10:
    print("Tu número es menor que 10")
# Si una condicion no se cumple, no imprimira el texto

