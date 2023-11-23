#Strings 

my_string="Mi string"
my_other_string="mi otro string"

#longitud del contenido de la variable
print(len(my_string))
print(len(my_other_string))

#concatenacion de string con una cadena de espacio
print(my_string+ "   " + my_other_string)

#Los string puedes llevar ciertos caracteres
#salto de linea \n
my_new_string="Este es un string\ncon salto de linea"
print(my_new_string)

#tabulaciones \t
my_tab_string="\tEste es un string con tabulación"
print (my_tab_string)

#escape primero hace la tabulacion y la siguiente no marca la tabulacion 
my_scape_string="\tEste es un string \n escapado"
print (my_scape_string)

#para que omita la tabulacion o el salto de line se utiliza doble diagonal y meter todo en una linea 
my_scape_string2="\\tEste es un string \\n escapado"
print (my_scape_string2)

#formateo %s
# $s indica que el primer texto que yo le pase formateado a esta cadena de texto lo va meter ahi
# %d si es entero 
# %f numeros de coma flotante

name,surname,age = "Monserrat","Ortiz",23
#sin formatear
print("Mi nombre es " +  name + " " + surname + " "+ "y mi edad es " +  str(age))
#con formateo 
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print("Mi nombre es {}{} y mi edad es {}" .format(name,surname,age))
print(f"Mi nombre es {name}{surname} y mi edad es {age}")

#Desempaquetado de caracteres 
language = "Python" #python tiene 6 letras

a,b,c,d,e,f=language #por eso aqui pusimos 6 letras 
print(a)  #aqui la letra 'a' representa la primera letra de "python"
print(e)  #aqui la letra 'b' representa la segunda letra de "python"


#División 
language_slice=language[1:4] #muestra las letras que estan entre el rango 1-4 en este caso seria 'yth' [1,2,3] (porque el elemento del indice 4 no se considra)
print(language_slice)

language_slice=language[-4]  #muestra la letra que esta en la posicion -4 que seria la letra 't'
print(language_slice)

#reverse 
reversed_language = language[::-1]  #muestra la variable al reves 'nohtyp'
print(reversed_language)

language = 'Python'
pto = language[0:6:2] #Es posible omitir caracteres mientras se corta pasando el argumento del paso al método de corte
print(pto) # Pto

#Funciones del sistema que se pueden utilizar en un string 

print(language.capitalize()) #la primera en mayuscula 
print(language.upper()) # lo convierte en mayusculas
print(language.count("t")) #cuenta cuantas t existen en el contenido de la variable
print(language.isnumeric()) #valida si es numerico
print(language.lower()) #convierte en minuscula 
print(language.lower().isupper()) #valida si esta en mayusculas
print(language.startswith("Py")) #valida que asi se inicie el valor de la variable en este caso arroja true porque el contenido de la variable language = "Python" si inicia con 'Py'
print(language.endswith('on'))  #valida que asi termine el valor de la variable en este caso arroja true porque el contenido de la variable language = "Python" si termina 'on'

#swapcase(): convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a mayúsculas.
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs(1)) #Reemplaza el caracter de tabulacion con espacios (se indica que sea de 1 espacio)

print(challenge.find('y')) #devuelve el indice de la PRIMERA aparicion de una subcadena, si no lo encuentra devuelve -1
print(challenge.rfind('y')) #devuelve el indice de la ULTIMA aparicion de una subcadena, si no lo encuentra devuelve -1

 # isalnum() --->  Comprueba que el caracter alfanumerico si cuenta con espacio no los va tomar como alfanumerico
 # isalpha() --->  Comprueba si todos los elementos de la cadena son caracteres alfabeticos (az AZ)
 #isdecimal() ---> Comprueba si todos los caracteres de una cadena son decimales (0-9)
 #isdigit() --->   Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números)
 #isnumeric() ---> comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½)

 # join() ---> Devuelve una cadena concatenada

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' # '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'


