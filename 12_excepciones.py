##excepciones##
#print(5+"5")
num1,num2=5,2
num2='1'

#Lo que va dentro del try es lo que se debe ejecutar, en dado caso que ese codigo marque error se controla en el except, este cacha el error y muestra el mensaje que quiero al momento de que sea error
try:
    print(num1+num2)
    print("No se ha producido un error")
except:
    #se ejecuta si se produce una excepción
    print("Se ha produccido un error")

#try con else
try:
    print(num1+num2)
    print("No se ha producido un error")
except:
    print("Se ha produccido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: #Opcional
    #se ejecuta siempre (si marca un error o no al igual se muestra)
    print("La ejecución continúa")


'''
Aunque controle el error como lo hice en la parte de arriba y vuelva a ejecutar otro codigo que provoque el mismo error este nuevo ya no se va controlar
Cuando ejecutamos nuevamente el print(num1+num2) marca el error TypeError por lo mismo ahora se van hacer exepción por tipo
'''

#Excepciones por tipo
try:
    print(num1+num2)
    print("No se ha producido un error")
#except ValueError:
    #se ejecuta si se produce una excepción
    #print("Se ha produccido un ValueError")
except TypeError as error:
    #se ejecuta si se produce una excepción
    #la variable error guarda lo del error
    print(error)
except Exception as error:  #El Exception es para que guarde los errores en general osea si es TypeError o ValueError lo mostrara como quiera
    #se ejecuta si se produce una excepción
    print(error)


#Captura de la información de la excepción
