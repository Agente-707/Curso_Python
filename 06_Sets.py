### Sets ###

my_set = set()
my_other_set = {} # => dicionario (vacio)

print(type(my_set)) # Tipo de dato "set" (vacio)
print(type(my_other_set)) # Tipo de dato "dict"

my_other_set = {"Luis", "Pareja", 19}
print(my_other_set)

'''
Nota: Los sets no son una estructura ordenada, 
no se puede acceder a un elemento por su indice.
'''

# Algunas operaciones con sets

# add
my_other_set.add("Agente-707") # Agrega un elemento al set
print(my_other_set)

my_other_set.add("Luis") 
print(my_other_set) # No se puede añadir elementos repetidos a los sets

# in
print("Luis" in my_other_set) # Luis existe dentro de mi set? => True
print("LuiSSSSS" in my_other_set) # LuiSSSSS existe dentro de mi set? => False

# remove
my_other_set.remove("Luis") # Elimina a "Luis" del set
print(my_other_set)

# clear
my_other_set.clear() # Elimina todos los elementos del set 
print(len(my_other_set)) # Cantidad de elementos del set => 0

# del
del my_other_set # Elimina el set
#print(my_other_set) Error: my_other_set no esta definido

# transformacion set => list
my_set = {"Luis", "Pareja", 19}
my_list = list(my_set) # Convertimos el set a lista
print(my_list)
print(my_list[0]) # Accedemos a un elemento de la lista

my_other_set = {"yo", "tu", "el", "ella"}

# union
my_new_set = my_set.union(my_other_set) # Union de sets
print(my_new_set) # Los imprime sin ningun orden y sin elementos repetidos
print(my_new_set.union(my_new_set).union(my_set)) 
print(my_new_set.union(my_new_set).union(my_set).union({"elpepe", ":v"})) 

# Diferencia entre sets
print(my_new_set.difference(my_set)) 
# me da los elementos que estan en "my_new_set" pero no en "my_set"
print(my_set.difference(my_new_set)) 
# me da los elementos que estan en "my_set" pero no en "my_new_set"
