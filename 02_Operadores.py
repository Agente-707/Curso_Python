### Operadores Aritmeticos ###

print(3+4) # Suma
print(3-4) # Resta
print(3*4) # Multiplicación
print(3/4) # División
print(3%4) # Módulo
print(10//3) # División entera
print(2**3) # Potencia

# Concatenación de cadenas
print("Hola" + " Mundo") 
print("Tengo " + str(19) + " años")

# Repetición de cadenas
print("Hola " * 5) 
print("Hola " * (2**3))

my_float = 2.5 * 2
print("Hola " * int(my_float)) 

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Mundo")
print("Hola" < "Mundo")
print("Hola" >= "Mundo")
print("Hola" <= "Mundo")
print("Hola" == "Mundo")
print("Hola" != "Mundo")


print("aaaa" >= "abaa") # Operaciones alfabeticas
print(len("aaaa") >= len("abaa")) # Cuenta caracteres y compara

### Operadores Logicos ###
print(3 > 4 and "Hola" > "Mundo") # False and False = False
print(3 > 4 or "Hola" > "Mundo") # False or False = False
print(3 < 4 and "Hola" < "Mundo") # True and True = True
print(3 < 4 or "Hola" > "Mundo") # True or False = True
print(3 < 4 or ("Hola" > "Mundo" and 4 == 4)) # True or (False and True) = True
print(not(3>4)) # True