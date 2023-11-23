## condicionales ##

'''
Ejecucuion condicional: se ejecutara un bloque de una o mas declaraciones si una determinada expresion es verdadera

Ejecucion repetitiva: bloque de uno o mas declaraciones se ejecutara repetitivamente siempre que una determinada
expresion sea verdadera.

'''

#sintaxys 

#La palabra clave if se usa para verificar si una condicion es verdadera y ejecute el codigo del bloque 


a=2
if a>0:
    print("A es mayor a 0")

#En este caso la condicion es verdadera y se ejecuto el bloque. Sin embargo, si la condicion es falsa no se ve el resultado.
#Para ver el resultado de la condicion falsa debemos tener otro bloque, que es else

a=2
if a>5:
    print("A es mayor a 5")
else:
    print("A es menor a 5")

#Utilizamos el elif cuando se tienen multiples condiciones 
a=2
if a>5:
    print("A es mayor a 5")
elif a>0 and a<5:
    print("A es mayor que 0 pero menor a 5")
else:
    print("A es menor a 5")


#Codigo corto
a=3
print("A es mayor a 5") if a> 0 else print("A es menor a 5")

#condicion con operadores logicos
a=4
if a>0 and a<5:
    print("A es mayor a 0 y menor a 5")


user='Monse'
access_level=3
if user=='Admin' or access_level >=4:
    print("Acceso correcto")
else:
    print("Acceso denegado")

#1Ejercicio
edad=input("Ingrese su edad:")
edad=int(edad)

if edad >=18:
    print("Tiene edad para conducir")
else:
    años=18-edad
    print("Te faltan ",años," años para poder conducir")


#2Ejercicio
edad1=input("Ingrese su edad:")
edad1=int(edad1)

edad2=23

if edad1>edad2:
    años=edad1-edad2
    print("Eres", años, "años mayor que yo")
else:
    años=edad2-edad1
    print("Eres ",años," años menor que yo")


#3Ejercicio
a=input("Ingrese el valor de a: ")
b=input("ingrese el valor de b: ")
a=int(a)
b=int(b)

if a>b:
    print(a, "es mayor que ",b)
elif b>a:
    print(b, "es mayor que ",a)
else:
    print("a y b son iguales")
'''
'''
#4Ejercicio
puntuacion=79
if puntuacion>=80 and puntuacion<=100:
    print("A")
elif puntuacion>=70 and puntuacion<=79:
    print("B")
elif puntuacion>=60 and puntuacion<=69:
    print("C")
elif puntuacion>=50 and puntuacion<=59:
    print("D")
else:
    print("F")



#5Ejercicio
mes="ago"
mes=mes.lower()
print(mes)

if mes=="septembre" or mes=="octubre" or mes=="noviembre":
    print("temporada de otroño")
elif mes=="diciembre" or mes=="enero" or mes=="febrero":
    print("Temporada de invierno")
elif mes=="marzo" or mes=="abril" or mes=="mayo":
    print("Temporada de primavera")
elif mes=="junio" or mes=="julio" or mes=="agosto":
    print("Temporada de verano")
else:
    print("error, lo ingresado no es el nombre de un mes, capturar de nuevo")


#6Ejercicio
frutas=["banana","naranja","mango","limon"]

ifrutas="melon"
if ifrutas in frutas:
    print("Ya exite la fruta ",ifrutas, "en la lista: ",frutas)
else:
    frutas.append(ifrutas)
    print("se agrego la fruta",ifrutas," a la lista: ",frutas)

#6Ejercicio


'''
* Verifique si el diccionario de la persona tiene claves de habilidades; de ser así, imprima la habilidad intermedia en la lista de habilidades.
  * Verifique si el diccionario de la persona tiene la clave de habilidades; de ser así, verifique si la persona tiene la habilidad 'Python' e imprima el resultado.
  * Si una persona tiene habilidades solo JavaScript y React, imprima ('Es un desarrollador front-end'), si la persona tiene habilidades Node, Python, MongoDB, imprima ('Es un desarrollador backend'), si la persona tiene habilidades React, Node y MongoDB, Print('Es un desarrollador fullstack'), de lo contrario print('título desconocido'): para obtener resultados más precisos, se pueden anidar más condiciones.
  * Si la persona está casada y vive en Finlandia, imprima la información en el siguiente formato:Asabeneh Yetayeh vive en Finlandia. El está casado.
'''
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
'skills': ['Python', 'MongoDB','React','JavaScript'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }



#https://www.programarya.com/Cursos/Python/estructuras-de-datos/diccionarios#:~:text=En%20esencia%2C%20la%20manera%20de,%2C%20usando%20corchetes%20%22%5B%5D%22.
if 'skills' in person.keys():
    print(person['skills'][2])


print("Python" in person.get('skills'))  #Para validar si python esta dentro de los valores de la clave skills

if "Python" in person['skills']:
    print(person['skills'][4])


if "JavaScript" in person.get(('skills')) and "React" in person.get(('skills')):
    print("Es un desarrollador front-end")
elif "Node" in person.get(('skills')) and "Python" in person.get(('skills')) and "MongoDB" in person.get(('skills')):
    print("Es un desarrollador backend")
elif "React" in person.get(('skills')) and "Node" in person.get(('skills')) and "MongoDB" in person.get(('skills')):
    print("Es un desarrollador fullstack")
else:
    print("titulo desconocido")


##* Si la persona está casada y vive en Finlandia, imprima la información en el siguiente formato:Asabeneh Yetayeh vive en Finlandia. El está casado.

if person['is_marred']==True and person['country']=="Finland":
    print(person['first_name'], person['last_name'], " vive en ", person['country'], " y el esta casado") 