print ('-Ejemplo #3 Interfas Primaria con el Usuario (2)')
Nombre = input ('Hola Usuario cual es tu Nombre?: ')
print ('Hola ' + Nombre + ', vamor a realizar una suma con mas de un valor (Entero y flotante)')
N3 = int (input ('Por favor introduce el primer valor Entero: '))
N4 = float (input ('Por favor introduce el primer valor flotante: '))
N5 = complex (input ('Por favor introduce el primer valor complejo: '))
N6 = int (input ('Por favor introduce el segundo valor Entero: '))
N7 = float (input ('Por favor introduce el segundo valor flotante: '))
N8 = complex (input ('Por favor introduce el segundo valor complejo: '))
N9 = int (input ('Y por ultimo introduce un ultimo numero Entero: '))
#
Resultado = N3 + N4 + N5 + N6 + N7 + N8 + N9
Resultado = str (Resultado)
print (Nombre + ' , El resultado de la operacion es: ' + Resultado)