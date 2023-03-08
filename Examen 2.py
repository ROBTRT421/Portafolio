#Desarrollar un programa que solicite un numero entero desde teclado al usuario,
#posteriormente, el programa debera determinar e indicar a traves de un mensaje, si
#el numero introducido es par o impar.
#*REQUERIMIENTOS INDISPENSABLES:
#-El mensaje en pantalla debera mostrar la frase "el numero es par" o "el numero es impar"
#junto con el numero que el usuario introdujo desde el teclado, por ejemplo :
# "El numero 8 es par."
# "El numero 5 es impar."
print('******************************************************')
print('| Programa que determina si un numero es par o impar |')
print('******************************************************')
N = int (input ('Por favor introduce un numero entero: '))

if N % 2 == 0 :
	print ('El numero ', N,  ' Es un numero par.')
elif N % 2 == 1 :
	print ('El numero ', N, ' Es un numero inpar')
else :
        print ('elige un numero entero por favor')
