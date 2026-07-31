### Strings ###

my_string = "Mi String"
my_string2 = 'mi otro string'

print(my_string + " " + my_string2) # Concatenación

my_string3 = "Este es un string\ncon salto de linea" #salto de linea
print(my_string3)

my_string4 = "Este es un string\tcon tabulacion" #tabulacion
print(my_string4)

my_string5 = "\\tEste es un String \\n escapado" #caracteres escapados
print(my_string5)

# Formateo

name, surname, age = "Luis", "Pareja", 19

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division

language_slice = language[1:3] # desde el indice 1 hasta el 3 (sin incluirlo)
print(language_slice)

language_slice = language[1:] # desde el indice 1 hasta el final
print(language_slice)

language_slice = language[-2] # conteo desde el final, -1 es la ultima letra
print(language_slice)

language_slice = language[0:6:2] # desde el indice 0 hasta el 6 (sin incluirlo) de 2 en 2
print(language_slice)

# Reverse

language_reverse = language[::-1] # Invierte el string
print(language_reverse)

# Funciones

print(language.capitalize()) # Primera letra en mayuscula
print(language.upper()) # Todo en mayuscula
print(language.count("t")) # Cantidad de veces que aparece un caracter
print("123".isnumeric()) # Comprueba si es un numero
print(language.lower()) # Todo en minuscula
print(language.upper().isupper()) # Comprueba si todo esta en mayuscula
print(language.startswith("Py")) # Comprueba si empieza con el string entre parentesis
print("Py" == "py") # Son dieferentes strings
