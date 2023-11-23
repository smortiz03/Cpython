## DICCIONARIOS ##
'''
Un diccionario es una coleccion de tipos de datos emparejados (clave:valor), modificables(mutables) desordenados.
'''
my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict={"Nombre":"Monse", "Apellido":"Ortiz","Edad":23, 1:"Python"}
print(my_other_dict)


#Un diccionario es lo que se conoce como un json
my_dict={
    "Nombre":"Monse",
    "Apellido":"Ortiz",
    "Edad":23,
    "Lenguajes": {"Python","Swift","Kotlin"}, #esta clave tiene como valor un tipo set por lo que ya no se le puede agregar mas valores
    1:1.56
}

print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"]) #Acceder a un elemento por medio de la clave

my_dict["Nombre"]="Monserrat"  #Forma de actualizar la el valor de una clave
print(my_dict["Nombre"]) #Muestra el valor de la clave nombre actualizado
print(my_dict[1]) #Muestra el valor de la clave 1

print(my_dict.get("Calle")) #Verifica si existe una clave a traves del metodo get, si la clave no existe devuelve un None


my_dict["Calle"]= "Monte celeste"   #En este caso como no existe la clave "calle" como para modificar su valor como en el ejemplo anterior entonces al diccionario le agrega un nuevo campo llamado "Calle" con el valor de "Monte celeste"
print(my_dict)
               

print("Ortiz" in my_dict) #Esto arroja falso porque aqui se esta buscando por clave no por valor
print("Apellido" in my_dict) #Esto arroja true porque Apellido es una clave y si existe en el diccionario
print(my_dict.items()) #Listado de cada uno de las items
print(my_dict.keys()) #Solo retorna un listado de las keys(claves, llaves)
print(my_dict.values()) #Solo retorna todas los valores del diccionario
my_new_dict= dict.fromkeys(my_dict) #Crea un nuevo diccionario reutilizando solo las claves del diccionario my_dict
print(my_new_dict)


my_new_dict= dict.fromkeys(my_dict,) #Crea un nuevo diccionario reutilizando solo las claves del diccionario my_dict
print(my_new_dict)




#my_dict_copy=my_dict.copy()
#print("es mi copia: ", my_dict_copy)

'''
my_dict={
    "Nombre":"Monse",
    "Apellido":"Ortiz",
    "Edad":23,
    "Lenguajes": {"Python","Swift","Kotlin"}, #esta clave tiene como valor un tipo set por lo que ya no se le puede agregar mas valores
    1:1.56
}
my_dict["Lenguajes"].append("Node") #AttributeError: 'set' object has no attribute 'append' 
MARCA ERROR PORQUE LOS SET NO SON INMUTABLES POR LO QUE YA NO SE LES PUEDE AGREGAR VALORES UNA VEZ YA CREADO

En este caso vamos a cambiar los valores de la clave Lenguajes a lista para poder agregar un nuevo elemento en los valores 
'''


'''

my_dict2={
    "Nombre":"Monse",
    "Apellido":"Ortiz",
    "Edad":23,
    "Lenguajes": ["Python","Swift","Kotlin"], 
    1:1.56
}
print("my_dict2 sin campos agregados: ", my_dict2)
my_dict2["Lenguajes"].append("Node") #Para agregar un nuevo valor a un diccionario en este caso como la clave "Lenguajes" esta conformado por un set se agrega a traves del .append
print("my_dict2 con campos agregados: ", my_dict2)


my_dict2.pop("Nombre") #Elimina el elemento con el nombre de clave especificado.
print(my_dict2)

my_dict2.popitem() #Elimina el ultimo elemento
print(my_dict2)

del my_dict2["Edad"] #Elimina un elemento con el nombre de clave especificado 
print(my_dict2)

print(my_dict2.clear())  #Borra los elementos del diccionario. 

del my_dict2 #Elimina todo el diccionario
print(my_dict2)
'''