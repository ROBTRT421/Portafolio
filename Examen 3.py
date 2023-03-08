print ('              ***Examen 3***                 ')
#Desarrollar un programa que solicite 3 numero enteros
#desde el teclado al usuario, posteriormente,
#el programa debera terminar e indicart a traves de un mensaje 
#en la pantalla, cual de los tres es el mas grande.
#REQUERIMIENTOS INDISPENSABLES:
#El mensaje en pantalla debera mostrar el numero que resulto
#ser el mas grande de los tres, por ejemplo:
#"El numero 10 es el numero mas grande de los tres."
print ('*******************************************************************************')
print ('| Programa para determinar, Cual es el numero mas grande de los tres numeros. |')
print ('*******************************************************************************\n')
N = int (input ('Introduce el primer numero: '))
N1 = int (input ('Introduce el segundo numero: '))
N2 = int (input ('Itroduce el tercer numero: '))
if N > N1 and  N2 :
	print ('El numero ' , N , ' es el numero mas grande.')
else:
	if  N1 > N2 :
		print ('El numero ', N1 , ' es el numero mas grande.')
	else:
		print ('El numero ', N2 , ' es el numero mas grande.')