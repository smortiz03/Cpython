## SETS ##
'''
Un set no es una estructura ordenada por lo tanto no se puede consultar o acceder por indices y no acepta repetidos
'''
my_set = set() #palabra reservada
my_other_set = {} #tipado
print(type(my_set)) #indica que es un set
print(type(my_other_set)) #indica que es un diccionario ¿por que?

my_other_set = {"Monse", "Ortiz",23}
print(type(my_other_set)) #Llenando los campos ya indica que es un tipo set

print(len(my_other_set)) #indica los elementos del set

print(my_other_set) #Un set no es una estructura ordenada
print(my_other_set.add("MonseO"))  #para agregar 
print(my_other_set) 
print(my_other_set.add("MonseO"))  #Si agregamos lo mismo 2 veces NO ACEPTA repetidos
print(my_other_set) 

print("Monse" in my_other_set) #Para realizar busqueda por medio del in
print("Mons" in my_other_set)


my_other_set.remove("Monse") #Para eliminar un elemento
print(my_other_set)

my_other_set.clear() #borra todos los elementos del set
print(len(my_other_set))



#NOTAAAAAAAAAAAAAAAAA! las operaciones propias de un objecto se acceden a traves del punto(.)
#del palabra resrvada del sistema 
del my_other_set #elimina todo


#Pasar de un set a una lista
my_set= {"Monse", "Ortiz",23}
my_list =list(my_set)
print(my_list)
print(my_list[0])

my_set.update(["Sanjuana","Tovar",1.56]) #Agregar varios elementos usando el update()
print(my_set)

#Tabien se puede agregar toda una lista con el update
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

my_other_set = {"Kotlin", "Swift","python"}

my_new_set = my_set.union(my_other_set)  #para unir los dos set
print(my_new_set)

print(my_new_set.union(my_new_set)) #No hace nada porque no permite repetidos 

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript","c#"})) #Aqui ya une la informacion porque javaScript y c# son nuevos por lo que no existe una repeticion y permite la union

print(my_new_set.difference(my_set)) #De my_new_set le estamos quitando los elementos de my_set 

print(my_new_set.intersection(my_set)) #Devuelve el conjunto de elementos que se encuentran en AMBOS conjuntos

print(my_new_set.isdisjoint(my_set)) #Si dos conjuntos no tienen uno o mas elementos en comun se les llaman conjuntos disjuntos. En este caso el resultado es falso porque si tienen elementos en comun 

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item6', 'item7'}
print(st2.isdisjoint(st1)) #En este ejemplo es true porque no tienen ningun elemento en comun