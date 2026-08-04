### Diccionarios ###

''' 
Los diccionarios son un tipo de estructura en los cuales
podemos almacenar datos de tipo 'clave:valor'
'''
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict)) # Tipo de dato 'dict' (vacio)

my_other_dict = {"Name":"Luis", "Surname":"Pareja", "Age":19, 10:"hola"}
#            "Name" almacena "Luis" - "Surname" almacena "Pareja"
#            "Age" almacena 19      - 10 almacena "hola"

my_dict = {
    "Name":"Luis",
    "Surname":"Pareja",
    "Age":19,
    "Lenguajes":{"Python","C++","Java"}, # => Set
    1:1.75
}

print(my_dict)
print(my_other_dict)

# print(my_dict[clave]) => imprime el valor
print(my_dict["Name"]) # => "Luis"
print(my_dict["Surname"]) # => "Pareja"
print(my_dict["Age"]) # => 19
print(my_dict["Lenguajes"]) # => {"Python","C++","Java"}
print(my_dict[1]) # => 1.75

# Agregando elementos dentro de un diccionario
my_dict["Color"] = "Rojo"
print(my_dict) # Añade 'color': 'rojo' al final del diccionario

# Algunas funciones

# len
print(len(my_other_dict)) 
'''
"Name":"Luis"
"Surname":"Pareja"
"Age":19
10:"hola"

=> 4 elementos
'''
print(len(my_dict))
'''
"Name":"Luis"
"Surname":"Pareja"
"Age":19
"Lenguajes":{"Python","C++","Java"} => solo cuenta el set "Lenguajes", no sus elementos
1:1.75

=> 5 elementos
'''

# del
del my_dict["Color"] # Elimina un elemento del diccionario
print(my_dict)

# in
print("---in---")
print("Luis" in my_dict) # => False
print("Surname" in my_dict) # => True
print("Pareja" in my_dict) # => False
print("Name" in my_dict) # => True
# el 'in' solo identifica las claves

# items - keys - values
print("---items---")
print(my_dict.items()) # nos da una lista de todos los items ('llave', 'valor') del diccionario
print("---keys---")
print(my_dict.keys()) # nos da una lista de todas las llaves del diccionario
print("---values---")
print(my_dict.values()) # nos da una lista de todos los valores del diccionario
# Nos lo devuelven en formato de "Lista" []

# fromkeys
print("---fromkeys---") # Crea diccionarios con solo recibir las llaves

my_list = ["Name",12,"Age"]
my_new_dict = dict.fromkeys(my_list) # Es posible crear un diccionario con una lista desde fromkeys
print(my_new_dict)

my_new_dict = dict.fromkeys(("Name",12,"Age")) # Nos crea un diccionario con las llaves dentro del parentesis, cada una sin valor (None)
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict)  
'''
Si le pasamos al fromkeys 'my_dict' creara otro diccionario 'my_new_dict'
con las mismas claves, cada una sin valores (None)
'''
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, "Agente-707") # El valor de cada llave es ahora "Agente-707"
print(my_new_dict)

# Transformaciones
print(list(my_new_dict)) # dict => list     []
print(tuple(my_new_dict)) # dict => tuple   ()
print(set(my_new_dict)) # dict => set       {}
# solo toman las llaves como elementos, no los valores
