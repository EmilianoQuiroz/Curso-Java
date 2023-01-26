#---- Entrada de datos por consola en Python ----#
#Mediante la funcion input() podemos ingresar datos por consola en Python
#Por defecto esta funcion reecibe datos de tipo cadena de caracteres (string)

#Para esto creamos una variable y le asignamos como valor la variable input()
#Esto hara que el dato que ingresemos por consola se asignara a la variable a la que le asignamos el input()

resultado = input("Escribe un mensaje: ");#Dentro del input podemos imprimir el mensaje que querramos mostrar al usuario

print(resultado);#Imprimimos la variable con el valor ingresado

print("Fin del programa");

#--- Conversion de tipos de datos ---#
#Para que un input reciba un tipo de dato que no sea el que tiene por defecto debemos meterlo dentro del tipo de dato que queremos que reciba por ejemplo : int(input(valor a recivir: ));

numero1 = int(input("Digite un numero: "));
numero2 = int(input("Digite otro numero: "));

resultado = numero1 + numero2;

print(resultado);