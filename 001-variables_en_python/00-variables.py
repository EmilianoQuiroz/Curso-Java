#---- Variables en Python ----#
"""
Una variable nos va a permitir almacenar informacion de  manera temporal datos de cualquier tipo. Una vez almacenados estos datos en su variable, podemos usar esta las veces que querramos e incluso cambiar su contenido
"""

#Para declarar una variables debemos asignarle un nombre y mediante el signo "=" asignarle un valor
#Estos valores que son los que se les asignan a las variables se llaman literales

miVariable = "Cadena de texto";#En este caso asignamos una cadena de caracteres (string) a "miVariable"
print(miVariable);#Imprimimos en pantalla el contenido de nuestra variable

#En Python no es necesario indicar el tipo de dato que contiene nuestra variable
miVariable = 1;#Podemos modificar el valor de nuestra variable con otro tipo de dato si ningun problema
print(miVariable)#Imprimimos la variable con el nuevo valor

#--- Ubicar espacios en memoria de una variable ---#
#Para ubicar el espacio en  memoria que ocupa una variable podemos usar la funcion id()

print(id(miVariable));#Esto nos dara la posicion en memoria de donde se encuentra nuestra variable
