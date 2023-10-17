### TUPLES ###
'''
Una tupla es una colección de diferentes tipos de datos que estan ordenados y es INMUTABLE.
A diferencia de las listas las tuplas NO permite cambiar o agregar  valores

LAS TUPLAS AL SER INMUTABLES POR LO REGULAR SE UTILIZAN CUANDO SE QUIEREN VALORES CONSTANTES

#sintaxis
my_tuple = tuple()  #tuple() es su nombre reservador y con el se indica que es una tupla
my_other_tuple = () # TIPADO por este lado con puros parentesis indicamos que es una tupla como en el caso de listas si ponemos solo corchetes [] con ellos se indica que es una lista
'''
#Asta aqui una tuple es como una lista 
my_tuple=(35,1.77,"Monse","Ortiz","Ortiz")
my_other_tuple = tuple()
my_other_tuple = (23,26,25,13)

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Ortiz")) #cuenta cantas veces exite el ortiz en la tupla
print(my_tuple.index("Monse"))  #indica el indice del valor

my_sum_tuples = my_tuple + my_other_tuple

print(my_sum_tuples[3:6])

#comprobar si un elemento existe o no en la tupla usando in, que devuelve un valor booleano
print("Monse" in my_tuple)

#Cuando queremos hacer un cambio en la tupla primero la convierto a lista y luego la vuelvo a convertir a tupla
print(type(my_tuple))
my_tuple=list(my_tuple)  #la tupla la convertimos a lista
print(type(my_tuple))

#con esto ahora si tenemos la lista mutable
print(my_tuple)
my_tuple[4]="Tovar"
my_tuple.insert(1,"Morado")
print(my_tuple)
print(type(my_tuple))
my_tuple=tuple(my_tuple) #aqui la convierto de nuevo a tupla
print(type(my_tuple))

del my_tuple #para eliminar una tupla
print(my_tuple)