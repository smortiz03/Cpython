#Clases#
'''
Objetos que definimos nosotros a nuestra medida
sintaxy 
escribir la primera con mayuscula y sin _ 
ejemplo MyPerson

class Person:
    pass #para intentar que se ejecute(no hace nada) se utiliza cuando el bloque de codigo no tiene nada

print(Person)
print(Person())

#El init es una palabra reservada que nos sirve para crear un constructor de clase
#aqui esta clase ya puede recibir un parametro
'''
class MyPerson:
    def __init__(self,name,surname) -> None: #esto es un constructor de clase, siempre llama a self porque es algo que es requerido
        #el self es algo obligatorio si queremos construir una clase que tenga un constructor le tenemos que pasar self, self se refiere a el mismo(a la instancia de MyPerson)
        self.name=name #aqui estamos diciendo que self tiene una propiedad que se llama name y la igualamos a name ya estamos asignando una propiedad
        self.surname=surname
'''
#Aqui marca error ya que no se le esta enviando los dos parametros
my_person = Person()
print(my_person)
'''
'''
#Ejemplo de propiedades que definamos fuera de la clase
my_person = MyPerson("Monse","Ortiz")
print(my_person.name)
print (f"{my_person.name} {my_person.surname}")


#Ejemplo de propiedades que definamos dentro de la clase 
class MyPerson2:
    def __init__(self) -> None:
        self.name="Monserrat "
        self.surname="Ortiz Tovar"

my_person2=MyPerson2()
print(f"{my_person2.name}{my_person2.surname}")

#Ejemplo con nombre y surname se crea una propiedad almacenada que es full name

class MyPerson3:
    def __init__(self,name,surname) -> None:
        self.fullname=f"{name}{surname}"

my_person3=MyPerson3('Sanjuana ','Ortiz')
print(my_person3.fullname) #Aqui ya no se puede acceder a las propiedades name o surname por separado si no solo a fullname que contiene los dos propiedades



class MyPerson4:
    def __init__(self,name,surname) -> None:
        self.fullname=f"{name}{surname}"

    #Creando dentro de la clase una función
    def walk(self): #le pasamos por defecto como parametro self. No debe llamar a la calse MyPerson4 porque la funcion walk esta dentro de la clase, dentro de la clase no se va llamar a la misma clase.
        # la forma que se tiene de llamar a la misma clase es siempre con self. (Si se utiliza self como parametro vamos a tener acceso a todo lo que esta dentro de self)
        print(f"{self.fullname} esta caminado")

my_person4=MyPerson4('Sanjuana ','Ortiz')
print(my_person4.fullname) 
my_person4.walk()  #Aqui se imprime el contenido de la funcion de la clase MyPerson4

class MyPerson5:
    def __init__(self,name,surname,alias=' sin alias') -> None: #Aqui le podemos dar un valor por defecto como lo vemos en el alias
        self.fullname=f"{name}{surname} ({alias})"
    def walk(self):
        print(f"{self.fullname} esta camiando")


my_person5=MyPerson5("Ian","Sagastegui")
print(my_person5.fullname)
my_person5.walk()

#Creamos otra persona
my_other_person=MyPerson5("Estephania"," Sagastegui"," flaquis")  #Aqui si le estamos dando un alias para que no tome el de "por defecto"
print(my_other_person.fullname)
my_other_person.walk()

#el constructor(my_other_person) es para crear la instancia, es decir ya lo cree una vez y aqui lo puedo simplemente cambiar
#Aqui cambiamos los datos
my_other_person.fullname="Guillero Ortiz jefe"
my_other_person.walk()
'''

class MyPerson6:
    def __init__(self,name,surname,alias=' sin alias') -> None: #Aqui le podemos dar un valor por defecto como lo vemos en el alias
        self.fullname=f"{name}{surname}({alias})"
        self.__name=name #al poner el __name estoy haciendolo privado
    def walk(self):
        print(f"{self.fullname} esta camiando")
    
    

my_person6=MyPerson6("Ian ","Sagastegui")
print(my_person6.fullname)
my_person6.walk()
#my_person6.fullname='fddfdsds'  #Aqui se puede modificar el valor sin problema
print(my_person6.fullname)
print(my_person6.__name) #marca error para poder acceder a ella
#my_person6.__name='monseeeeee' #pero aqui si deja cambiarlo
#print(my_person6.__name) #para despues mostrarlo