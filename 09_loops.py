##Loops o bluces##

'''
Para manejar tareas repetitivas se utilizan los bluces
1.- while loop  (mientras)
2.- for loop (en)
'''

#WHILE

#El bluce while se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condicion determinada.
#syntax
'''

count=0
while count <5:
    print(count)
    count=count+1

#En el bucle anterior la condicion se vuelve falsa cuando el count es igual a 5. Ahi es cuando el ciclo se detiene y ya no entra al bucle.

#Si se necesita ejecutar un bloque de codigo cuando la condicion ya no sea cierta se utiliza el else

count=0
while count <5:
    print(count)
    count=count+1
else:
    print("El ciclo while se detuvo ya que el contador ya vale ", count)

#BREAK: Se utiliza cuando se quiere detener o salir de ciclo
#syntax

count=0
while count <5:
    print(count)
    count=count+1
    if count==3:
        print("El ciclo se detuvo porque el count ya vale", count)
        break

#En el bucle anterior se anexo una condicion para detener el ciclo cuando el count fuera igual a 3 (solo imprime 0,1,2 porque se detuvo cuando llega al 3)

#CONTINUE: Con la instruccion continue se puede omitir la interación actual y continuar con la siguiente
#En este bucle solo imprime el 0,1,2,(salta el 3) y 4
#Explicación: cuanto el count=3 entra al if dentro del if se le suma +1 y el count ya vale 4 y con la instruccion continue sale del if y continua el ciclo while 
count=0
while count <5:
    if count==3:
        count=count+1
        continue
    print(count)
    count=count+1

'''
#BUCLE FOR: se utiliza para iterar sobre una secuencia(es decir, una lista, una tupla, un diccionario, un conjunto o cadena)
#syntax
'''
for interator in lst:
    codigo
'''

#for en listas
'''
print("for en listas")
numeros=[0,1,2,3,4,5]
for numero in numeros:
    print(numero)

#for en string

print("for en string(cadenas)")
lenguaje='Python'

for letra in lenguaje:
    print(letra)

print("for en string(cadenas) utilizando len(que cuenta el numero de caracteres)")
for i in range(len(lenguaje)):
    print(lenguaje[i])


#for en tuplas
print("for en tuplas")

numeros=(0,1,2,3,4,5)

for numero in numeros:
    print(numero)

#for en diccionario, al recorrer un diccionario se obtiene la clave del mismo
print("for en diccionarios")

person ={
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

#print(person.items())  CON EL ITEMS TRAE TANTO LLAVES COMO VALORES
print("En este for muestra solo las claves del diccionario")
for key in person:
    print(key)

print("En este for muestra las claves y valores del diccionario")

for key,value in person.items():
    print(key,value)


#for en set
print("for en set")
compañias={'facebook','google','apple','microsoft','IBM','oracle','amazon'}

for compañia in compañias:
    print(compañia)

#BREAK Y CONTINUE EN LOS BUCLES FOR

print("Break en for")
#se detiene cuando numero=3
numeros=(0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero ==3:
        break


#En este ejemplo si el numero=3, el paso despues de la condicion(dentro del bucle) se omite(es decir el print del "siguiente numero debe ser...") y la ejecución del bucle continua si quedan iteraciones.
print("instrucción continue en for")
numeros=(0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero==3:
        continue
    print("el siguente numero debe ser", numero+1) if numero!=5 else print("fin del bucle")
print("fuera del bucle")


#FUNCION DE RANGO

La funcion de range() se utiliza como lista de numeros. El rango(inicio,fin,paso) toma tres parametros: inicio, fin e incremento.
De forma predeterminada, comienza en 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento(fin).

lista=list(range(11))  #crea una lista de 11 numeros iniciando del 0 al 10
print(lista)

st=set(range(1,11)) #se crea un set donde los argumentos indican el inicio y el final de la secuencia, el paso esta configurado en el valor predeterminado 1.
#en este ejemplo indicamos que inicia en 1 y termina en 11 pero no concidera el 11 si no que solo llega de 1 a 10
print(st)


#Aqui se indica que inicia en el valor 0, hasta el 11 con un incremento de 2
lista=list(range(0,11,2))
print(lista) #0,2,4,6,8,10

st=set(range(0,11,2))
print(st) #0,2,4,6,8,10

for numero in range(11):
    print(numero) # imprime del 0 al 10, no incluye el 11



#BUCLES ANIDADOS
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for llave in person:
    #print(llave)
    if llave =='skills':  #si skills esta dentro de las llaves entonces entra al if
        for skill in person['skills']:  #entra al for y muestra los valores dentro de dicha llave
            print(skill)

#Si en este ejemplo utilizamos las llaves 'age' o 'is_marred' va marcar error ya que el objeto bool o int no son iterable

#EJECUTAR MENSAJE CUANDO SE FINALICE EL BUCLE SE USA EL ELSE

for numero in (range(11)):
    print(numero)
else:
    print("El bucle se detiene en ", numero)

#la palabra pass se usa como marcador de posicion para declaraciones futuras

for numero in range(6):
    pass

#Ejercicio 1
print("Itere de 0 a 10 usando el bucle for")
for numero in (range(11)):
    print(numero)


print("Itere de 0 a 10 usando  el bucle while.")
count=0
while count<=10:
    print(count)
    count=count+1

#Ejercicio 2
print("Itere de 10 a 0 usando el bucle for utilizando reversed")

for numero in (reversed(range(11))):
    print(numero)

print("Itere de 10 a 0 usando el bucle for utilizando ranger(start,end,step)")
for numero in range(10,-1,-1):
    print(numero)

print("Itere de 10 a 0 usando  el bucle while.")
count=10
while count<=10:
    print(count)
    count=count-1
    if count<0:
        break

#Ejercicio 3


count=0
while count<7:
    count=count+1
    print("#"*count)


#Ejercicio 4
print("p2 ejercicio3")
y="#"*8 #representa las verticales
for x in y:
    for t in x:
        print(t*8)  #representa las horizontales



#Ejercicio 5

print("con while")
count=0
while count<=10:
    mult=count*count
    print(count,"x", count, "=",mult)
    count=count+1

print("con for")
for numero in range(0,11,1):
    print(numero,"x",numero,"=",numero*numero)


#Ejercicio 6

lista=['Python','Numpy','Pandas','Django','Flask']

for elemento in lista:
    print(elemento)

#Ejercicio 7

print("Numeros pares del 0 al 100")
for numero in range(0,101,1):
    if numero%2==0:
        print(numero)

#Ejercicio 8
print("Numeros impares del 0 al 100")
for numero in range(0,101,1):
    if numero%2!=0:
        print(numero) 

#Ejercicio 9
suma=0
for numero in range(0,101,1):
    
    suma=numero+suma
    #print(numero)
    
print("La suma de todos los números es",suma)    

#Ejercicio10
suma=0
suma2=0
for numero in range(0,101,1):
    if numero%2==0:
        suma=numero+suma
    else:
        suma2=numero+suma2


print("La suma de todos los pares es ",suma,"y la suma de las probabilidades es ", suma2)
    
'''  
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Yemen',
  'Zambia',
  'Zimbabwe',
  'Tierra',
]
#print ("Cuba" in countries)

for texto in countries:
    if texto=="Tierra":
        print("si existe Tierra")


