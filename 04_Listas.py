### Lists ###

# Listas vacias
my_list = list()
my_other_list = []

print(len(my_list))

#Listas con datos
my_list = [35, 24, 62, 27, 17, 21, 10]

print(my_list)
print(len(my_list))

my_other_list = [19, 1.74, "Luis", "Pareja"]

print(type(my_list))
print(type(my_other_list))

# Elementos de la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1]) # Cuenta en revesa
print(my_other_list[-4])
print(my_list.count(30)) # Cuenta cuantas veces aparece el elemento en la lista
#print(my_other_list[4]) # Error, no existe el indice 4 #IndexError
#print(my_other_list[-5]) # Error, no existe el indice -5 #IndexError

# Desempaquetado de listas
age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(height)
print(age)
print(surname)

print(my_list + my_other_list) # Concatenacion de listas

my_other_list.append("Agente-707") # Inserta un nuevo elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Verde") # Inserta un nuevo valor en la posicion que se le indica
print(my_other_list)

my_other_list.remove("Verde") # Borra un elemento de la lista
print(my_other_list)

print(my_list.pop()) # Extrae el ultimo elemento de la lista por defecto
print(my_list)

print(my_list.pop(2)) # Extrae el elemento de la posicion 2 de la lista
print(my_list)

my_pop_element = my_list.pop(2) # Recupera el elemento eliminado
print(my_pop_element)

print(my_list)
del my_list[2] # Elimina el elemento de la posicion 2 de la lista
print(my_list)

my_new_list = my_list.copy() # Copia los elementos de "my_list" a "my_new_list"

my_list.clear() # Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Invierte el orden de los elementos
print(my_new_list)

my_new_list.sort() # Ordena los elementos de la lista de menor a mayor
print(my_new_list)

