### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.75, "Luis", "Pareja")
my_other_tuple = (13,27,40)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

# Desempaquetado de tuplas
print(my_tuple.count("Luis")) # Cuenta cuantas veces aparece el elemento en la tupla
print(my_tuple.index("Pareja")) # Devuelve el indice del elemento en la tupla

# my_tuple[1] = 1.80 Error: no se puede modificar una tupla

# Concatenacion de tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Slicing de tuplas
print(my_sum_tuple[3:6])
print(my_sum_tuple[2:4])

# Convertir tupla a lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "Agente-707"
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminacion de tuplas

# del my_tuple[2] Error: no se puede eliminar un elemento de una tupla

# del my_tuple()
# print(my_tuple) Error: no se puede imprimir una tupla eliminada

