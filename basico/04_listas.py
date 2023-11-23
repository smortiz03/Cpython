##Lists
"""
Lista: es una colección ordenada y modificable de datos. (Permite datos duplicados)
*syntaxis 
my_list = list()
my_other_list = [] TIPADO
"""
#syntaxis 
my_list = list()
my_other_list = []

print(len(my_list))

#para ingresar valores en la lista
my_list=[35,24,62,52,30,30,17]
print(my_list)
print(len(my_list))

my_other_list=[23,1.56,"Monse"]

print(type(my_other_list))
print(type(my_list))

#para acceder a un valor de la lista es atraves de la posicion 
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

#cuenta cuantas veces se repite el  numero 30 en la lista 
print(my_list.count(30))


#desempaquetar una lista, si en lugar de poner las 3 nuevas variables poner 2 va marcar error ya que la lista esta compuesta de 3 elementos 
age,height,name=my_other_list
print(name)

#concatenar listas
print(my_list + my_other_list)

#para agregar un elemento a la lista con el .append que inserta al final de la lista 
my_other_list.append("MonseDev")
print(my_other_list)

#para agregar un elemento a la lista en cualquier posicion de la lista que quieras se utiliza el .insert(la posicion, el valor)
my_other_list.insert(1,"azul")
print(my_other_list)


#Para modificar 
my_other_list[1]="Morado"
print(my_other_list)

#remove para eliminar un valor 
#remove es para eliminar un elemento que nosotros conocemos que esta dentro de la lista 
my_other_list.remove("Morado")
print(my_other_list)

#en este ejemplo en la lista tenia dos elementos con 30 pero solo elimino la primera que coincidio con este valor
my_list.remove(30)
print(my_list)

#con el pop elimina el ultimo de la lista pero se queda con ese elemento eliminado
my_list.pop()
print(my_list)

#con el pop pasandole el indice del valor que queremos eliminar 
my_list.pop(2)
print(my_list)

#Elimina por indice 
del my_list[2]
print (my_list)

#para copiar la lista
my_new_list=my_list.copy()

#El clear elimina la lista completa 
my_list.clear()
print(my_list)
print(my_new_list)

#para devolver los valores al reves 
my_new_list.reverse()
print(my_new_list)

#para ordenar de menor a mayor 
my_new_list.sort()
print(my_new_list)

#devuelve la lista ordenada sin modificar la lista original
print(sorted(my_new_list))