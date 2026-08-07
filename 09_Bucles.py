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





