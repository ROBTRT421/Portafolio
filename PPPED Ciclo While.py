#Desarrollar un programa que imprima en pantalla la Sucesion de Fibonacci desde el numero 0
#hasta el numero 1597, de manera horizontal. Ejemplo:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#Requerimientros Indispensables: 
#El programa debera tener un maximo de 7  lineas de codigo.
print ('******************************************')
print ('*S U C E S I O N  D E  F I B O N A C C I *')
print ('******************************************\n')
N1, N2 = 0, 1
while N2 <= 1597:
	print (N1, N2, end= " ")
	N1 = N1 + N2
	N2 = N1 + N2
print ('Fin')