print ('                            ***Sentencias condicionales Anidadas***                                    ')
print ('                                                                                                       ')
print ("""Las sentencias condicionales anidadas, se presentan cuando por el camino de verdadero o falso de una sentencia
condicional hay otra sentencia condicional. Es decir, cuando trabajamos con sentencias condicionales simples, compuestas, o multiples, podemos colocar dentro de la instruiccion o instrucciones a ejecutar de cada una de estas sentencias, otra sentencia condicional. En conclusion, las sentencias condicionales anidadas consiten en tener una instruccion condicional dentro de la otra, y dependiendo de si la condicion de la primera sentencia condicional se cumple o no se cumple, se ejecutara otra sentencia condicional. De esta manera tendremos una condicion, ampliando la cantidad de opciones para que nuestros programas puedan resolver un problema, sin importar la cantidad de situaciones que se presenten. \n""")
print ('*-Practica propuesta por el Doscente \n')
print ('==============')
print ('Conversor')
print ('============== \n')
print ('Menu de Opciones: \n')
print ('Presiona 1 para convertir de numero a palabra.')
print ('Presiona 2 para convertir de palabra a numero. ')
N = int (input ('Cual es tu opcion deseada?. '))
if N == 1:
	print ('\n Conversor de Numero a Palabra. \n')
	N1 = int (input ('Cual es el numero que deseas convertir a palabra?: '))
	if N1 == 1:
		print ("El numero es 'UNO'. ")
	elif N1 == 2:
		print ("El numero es 'DOS.' ")
	elif N1 == 3:
		print ("El numero es 'TRES.' ")
	elif N1 == 4:
		print ("El numero es 'CUATRO.' ")
	elif N1 == 5:
		print ("El numero es 'CINCO.' ")
	else :
		print ('El numero seleccionado no esta REGISTRADO.')
elif N == 2:
	print (' \n Conversor de Palanra a Numero. \n')
	N2 = input ('Cual es el la palabra que deseas convertir a numero?: ')
	if N2 == 'uno':
		print ("El numero es '1'. ")
	elif N2 == 'dos':
		print ("El numero es '2'. ")
	elif N2 == 'tres':
		print ("El numero es '3'. ")
	elif N2 == 'cuatro':
		print ("El numero es '4'. ")
	elif N2 == 'cinco':
		print ("El numero es '5'. ")
	else :
		print ('El numero seleccionado no esta REGISTRADO.')
else :
	print ('Esta no es una Opcion Elegible.')
print ('FIN.')


 