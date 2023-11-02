#modulos#
'''
Un modulo es un archivo que contiene conjunto de códigos o conjunto de funciones que se pueden incluir en una aplicación.
Un módulo pordia ser un archivo que contenga una sola variable, una función o una gran base de código.
'''
#No se puede importar ninguno de los demas archivos que empieza por un numero porque no acepta la sintaxis 
# marca error al importar import 09_loops pero no marca error al importar module 

'''
#SE ESTA IMPORTANDO TODO LO UE EXISTE EN EL ARCHIVO MODULE

import module
module.suma(6,8)
module.printValue("Hola")
'''

#ESTA IMPORTANDO SOLO LA FUNCION SUMA (osea que si pongo la funcion printValue marca error ya que solo se importo la funcion suma)
#Se pueden importar varias funciones del archivo module por ejemplo con: from module import suma,printValue
'''
from module import suma
suma(6,8)
#printValue("Hola")

#IMPORTAR FUNCIONES DESDE EL MÓDULO Y CAMBIARLE EL NOMBRE CON EL (as)
from module import generar_nombre as fullname
print(fullname('Monse','Ortiz'))
'''
'''
#IMPORTAR MODULOS INTEGRADOS
Tambien podemos importar los modulos integrados los cuales los mas comunes son: math, datetime, os, sys, random, stats, collections, json y re
'''
#MÓDULO DE ESTADISTICAS
#Proporciona funciones para estadísticas matemáticas de datos numéricos(las mas utilizadas son media, mediana,moda,stdev,etc)
#Se pueden importar multiples funciones a la vez (from math import pi, sqrt, pow, floor, ceil, log10) o si queremos importar todas las funciones (from math import pi as  PI)
from statistics import *  #importa todos los modulos de estadisticas
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       
print(median(ages))     
print(mode(ages))   

#MÓDULO DE MATEMÁTICAS
import math
print(math.factorial(5))
print(math.pow(2,5)) #función exponencial
print(math.sqrt(2)) #raiz cuadrada
print(math.floor(9.81)) #redondea al minimo
print(math.ceil(9.81)) #redondea al maximo

#MÓDULO ALEATORIO que da un numero aleatorio entre 0 y 0,9999...
from random import random,randint
print('numero random',random())
print('numero aleatorio entre 5 y 20',randint(5,20))
from datetime import date
print(date.today())

'''
#IMPORTAR MODULO DE SISTEMA OPERATIVO
Utilizando el módulo os es posible realizar automáticamente muchas tareas del sistema operativo, este modulo proporciona funciones para crear,
 cambiar el directorio actual de trabajo, eliminar una carpeta, recuperar su contenido, cambiar e identificar el directorio actual. 
#importando el modulo 
import os
#creando un directorio
os.mkdir('nombre del directorio')
#cambiando el directorio actual
os.chdir('ruta')
#Obteniendo el directorio de trabajo actual
os.getcwd()
#eliminado directorio
os.rmdir()
'''
import os
print(os.getcwd())

'''
#IMPORTAR MODULO DE SISTEMA 
El módulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de ejecución de python. 
#Para salir del sistema
sys.exit()

#Para conocer la variable entera más grande que se necesita
sys.maxsize

#Para conocer la ruta del entorno
sys.path

#Para saber la versión de python que se esta usando

sys.version
'''

import sys
print(sys.version)