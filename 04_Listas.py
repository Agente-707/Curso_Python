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
