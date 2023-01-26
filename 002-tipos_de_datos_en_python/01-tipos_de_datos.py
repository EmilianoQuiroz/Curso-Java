#---- Tipos de datos en Puthon ----#

#¿Como saber que tipo de dato contiene una variable?
#Esto lo podemos averiguar con la funcion type()

#Creamos una variable con un tipo de dato numerico
x = 12;
#Dentro de la funcion type() pondremos el nombre nuestra variable y luego la funcion type() dentro de un print para mostrar el resultado por consola
print(type(x));#En este caso nos dice que es un tipo de dato entero


#--- Tipos de datos basicos en Python ---#

#-- Tipos numéricos --#
#Enteros
"""
El tipo de los números enteros es int. Este tipo de dato comprende el conjunto de todos los números enteros, pero como dicho conjunto es infinito, en Python el conjunto está limitado realmente por la capacidad de la memoria disponible. No hay un límite de representación impuesto por el lenguaje.
Ejemplo
a = 10
b = 5
"""
#Flotantes
"""
Al igual que ocurre con los números enteros, los números reales son infinitos y, por tanto, es imposible representar todo el conjunto de números reales con un ordenador.
Para representar el mayor número posible de los números reales con las limitaciones de memoria (tamaños de palabra de 32 y 64 bits), se adaptó la notación científica de representación de números reales al sistema binario (que es el sistema que se utiliza en programación para representar los datos e instrucciones).
Ejemplo
a = 2.45;
b = 3.14;
"""
#Complejos
"""
El último tipo de dato numérico básico que tiene Python es el de los números complejos, complex.
Los números complejos tienen una parte real y otra imaginaria y cada una de ellas se representa como un float.
Para crear un número complejo, se sigue la siguiente estructura <parte_real>+<parte_imaginaria>j. Y se puede acceder a la parte real e imaginaria a través de los atributos real e imag:
complejo = 1+2j
complejo.real
1.0
complejo.imag
2.0
"""
#-- Tipos Booleanos --#
"""
En Python la clase que representa los valores booleanos es bool. Esta clase solo se puede instanciar con dos valores/objetos: True para representar verdadero y False para representar falso.
Una particularidad del lenguaje es que cualquier objeto puede ser usado en un contexto donde se requiera comprobar si algo es verdadero o falso. Por tanto, cualquier objeto se puede usar en la condición de un if o un while (son estructuras de control que veremos en tutoriales posteriores) o como operando de una operación booleana.
"""
#-- Tipo cadena de caracteres ---#
"""
Otro tipo básico de Python, e imprescindible, son las secuencias o cadenas de caracteres. Este tipo es conocido como string aunque su clase verdadera es str.
Formalmente, un string es una secuencia inmutable de caracteres en formato Unicode.
Para crear un string, simplemente tienes que encerrar entre comillas simples '' o dobles "" una secuencia de caracteres.
Se puede usar indistintamente comillas simples o dobles, con una particularidad. Si en la cadena de caracteres se necesita usar una comilla simple, tienes dos opciones: usar comillas dobles para encerrar el string, o bien, usar comillas simples pero anteponer el carácter \ a la comilla simple del interior de la cadena. El caso contrario es similar.
Ejemplo
a = "Hola";
b = 'Chau';
"""