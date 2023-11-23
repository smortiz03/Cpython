#Operadores aritméticos
"""
Suma(+): a + b
Resta(-): a - b
Multiplicación(*): a * b
División(/): a / b
Módulo(%): a % b  →lo que resta en la división
División de piso(//): a // b  → es el cociente de la división(las veces que cabe el dividendo entre el divisor).
Exponenciación(**): a ** b


print(3+4)
print(3-4)
print(3*4)
print(3/4)
print( 10 // 3)
print( 10 % 3)
print( "hola"*3)
"""
#Operadores de comparación 
"""
== es igual que 
!= es diferente
> mayor que
< menor que 
>= mayor igual que 
<= menor igual que 


print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False
"""
"""
Además del operador de comparación anterior, Python usa:

is : Devuelve verdadero si ambas variables son el mismo objeto (x es y)
is not : Devuelve verdadero si ambas variables no son el mismo objeto (x no es y)
in : Devuelve Verdadero si la lista consultada contiene un elemento determinado (x en y)
not in : devuelve True si la lista consultada no tiene un elemento determinado (x en y)


print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
"""
#Operadores logicos

"""
AND Retorna true si ambas condiciones se cumplen
OR Retorna true si almenos una de las dos condiciones es verdadera 
NOT Retorna falso si el resultado es verdadero 
"""

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False