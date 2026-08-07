### Bucles ###

# while

my_condition = 5

'''
while my_condition < 10: # condicion
    print("Hola") 
'''
# se imprimira "Hola" siempre y cuando 'my_condition' sea menor a 10 
# osea imprimira "Hola" infinitas veces hasta que explote tu PC

while my_condition < 10:
    print(my_condition) # Imprime el valor de 'my_condition'
    my_condition += 1 # el valor de 'my_condition' aumenta de uno en uno
# el bucle parara hasta que 'my_condition' sea mayor o igual a 10

# else
print("-------------------")
my_condition = 1
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Podemos combinar else con el while, pero no con elif
    print("Mi condición es mayor o igual que 10") # cuando la condicion del while no se cumpla se imprimira este mensaje

print("La ejecución continúa")

# Condicional if dentro de while
while my_condition < 20:
    my_condition += 1 # my_condition ira aumentando de uno en uno
    if my_condition === 15: # Cuando my_condition sea 15 imprimira el mensaje 
        print("Mi condición es 15")
    print(my_condition)

# break
my_condition = 10

while my_condition < 20:
    my_condition += 1
    print(my_condition)
    if my_condition == 15:
        print("mi condición es 15, el bucle terminó")
        break; # El break rompe con el bucle sin importar la condición principal de este

# for
my_list = [12, 23, 11, 46, 18]

for element in my_list:
    print(element)




