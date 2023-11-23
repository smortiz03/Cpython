#funciones 
'''
bloque reutilizable de código o declaraciones de programación diseñada para realizar una determinada tarea.
'''


#syntax
'''
#Se declaro la función
def my_funcion():
    print("Esto es una función")

#Se llamo la funcion
my_funcion()

#Función sin parámetros

def sumaSinParametro():
    numero1=3
    numero2=4
    total=numero1+numero2
    print(total)

sumaSinParametro()

#Funcion con parámetros
#con un parametro
def area_circulo(r):
    PI=3.14
    area=PI*r**2
    return area
print(area_circulo(10))



def suma_numeros(n):
    total=0
    for i in range(n+1):
        total+=i
    print(total)

#cuando NO se usa el return si no el print, se llama de la siguiente forma a la funcion
suma_numeros(10)
suma_numeros(100)

#cuando se utiliza return se llama de la siguiente forma a la funcion
#print(suma_numeros(10))
#print(suma_numeros(100))


#con dos parametros
def sumaConParametro(num1,num2):
    suma=num1+num2
    return suma

print(sumaConParametro(8,9))

def calcular_edad(current_year,birth_year):
    edad=current_year-birth_year
    return edad

print('edad:',calcular_edad(2023,2000))

#Pasando argumentos con clave y valor
def add_two_numbers (num1, num2):
    total = num1 + num2
    return(total)
print(add_two_numbers(num2 = 3, num1 = 2))

def nombre(Nombre,apellido):
    espacio=' '
    nombre_completo=Nombre + espacio + apellido
    return nombre_completo

print(nombre(Nombre='monse',apellido='ortiz'))

#Devolviendo un valor booleano

def num_primos(n):
    if n % 2==0:
        print(n,"es numero primo")
        return True
    print(n,"no es un numero primo")
    return False

print(num_primos(10))
print(num_primos(7))



#funcion para devolver una lista 

def lista(n):
    lista=[]
    for i in range(n+1):
        if i % 2==0:
            lista.append(i)
    return lista
print(lista(10))

#Función con parámetros predeterminados
#Cuando no pasamos argumentos al llamar a la función pero se pasaron valores predeterminados a los parametros, cuando se invoque la función utilizara sus valores predeterminados. 

def saludo (name ='Monse'):
    mensaje= name + ', bienvendio, esta es una función con parámetros predeterminados'
    return mensaje

print(saludo())
print(saludo('Monserrat'))

#Número arbitrario de argumentos
#Se utilizan cuando no se sabe la cantidad de argumentos que se pasaran a la función, se puede crear una función que pueda tomar 'n' cantidad de argumentos agrengando un *antes del nombre del parametro

def suma_numeros(*num):
    total=0
    for nume in num:
        total=total+nume
        
    return total
print(suma_numeros(1,2,3,4,5,6,7,8,9,10))


#Numero predeterminado y arbitrario de parámetros en funciones
def generar_grupo(grado,*grupo):
    print(grado)
    for i in grupo:
        print(i)
        
generar_grupo('6to','A','B','C','D','F')

#Función como parámetro de otra función 
def num_cuadrado(n):
    return n*n
def operacion(f,x):
    return f(x)
print(operacion(num_cuadrado,3))


def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))


#LABORATORIO
#1 Declarar una función add_two_numbers . Toma dos parámetros y devuelve una suma.
def suma(num1,num2):
    total=num1+num2
    return total

print(suma(5,8))

#2 El área de un círculo se calcula de la siguiente manera: área = π xrx r. Escribe una función que calcule area_of_circle .
def area_circulo(r):
    pi=3.14
    area=pi*(r**2)
    return area
print(area_circulo(4))

#3Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos. Compruebe si todos los elementos de la lista son tipos numéricos. Si no, dé una valoración razonable.
def sum_num(*num):
    
    total=0
    for nume in num:
        if type(nume)==int:
            total=total+nume
        else:
            return("el tipo del valor ingresado no es int, por lo que no se pueden sumar")
    return total
print(sum_num('1',2,3))

#4.La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, convert_celsius_to- fahrenheit .
def convert_C_A_F(C):
    conversion=(C*9/5) + 32
    return conversion

print(convert_C_A_F(20))

#5Escribe una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
def temporada(mes):
    mes=mes.lower()
    if mes=='enero' or mes=='febrero' or mes=='diciembre':
        return ("temporada de invierno")
    elif mes=='marzo' or mes=='abril' or mes=='mayo' or mes=='junio':
        return("Temporaa de primavera")
    elif mes=='julio' or mes=='agosto':
        return("Temporada de verano")
    elif mes=='septiembre' or mes=='octubre'or mes=='noviembre':
        return("Temporada de otoño")
    else:
        return('Lo capturado no es valido')
    
print(temporada('GFHGFHGFH'))


def print_list(lista):
    for list in lista:
        print(list)
    
print_list([1,2,3,4,5,6])

def lista_inversa(lista):
    for list in reversed(lista):
        print(list)

lista_inversa([1,2,3,4,5,6])
lista_inversa(['A','B','C','D'])

def lista_may(lista):
    for list in lista:
        print(list.upper())

lista_may(['a','b','c'])
'''
def add_item(valor):
    list=['Potato', 'Tomato', 'Mango', 'Milk']
    list.append(valor)
    return list

print(add_item('uva'))