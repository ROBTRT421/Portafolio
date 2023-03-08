print ('                ***OPERADORES RELACIONALES***                       \n')
print ('Con este programa ayudaremos a comparar las edades de dos personas. ')
Nom1 = input ('Cual es el nombre de la primer persona?: ')
Nom2 = input ('Ingresa el nombre de la segunda persona: ')
N1 = int (input ('Muy bien, ahora en numeros ingresa la edad de ' + Nom1 + ' :'))
N2 = int (input ('Hagamos lo mismo con la edad de ' + Nom2 + ' :'))
if N1 < N2 :
	print (Nom1, ' es menor que, ', Nom2)
if N1 > N2 :
	print (Nom1, ' es mayor que, ', Nom2)
if N1 == N2 :
	print (Nom1, ' y ', Nom2, ' Comparten la misma edad.')
if N1 != N2 :
	print ('sus edades son diferentes')
if N1 <= N2 :
	print ('La edad de ', Nom1, ' es menor o igual que la de ', Nom2)
if N1 >= N2 :
	print ('La edad de ', Nom1, ' es mayor o igual que la de ', Nom2)
