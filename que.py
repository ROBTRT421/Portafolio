print ('*******************************************************************************')
print ('| Programa para determinar, Cual es el numero mas grande de los tres numeros. |')
print ('*******************************************************************************\n')
N = int (input ('Introduce el primer numero: '))
N1 = int (input ('Introduce el segundo numero: '))
N2 = int (input ('Itroduce el tercer numero: '))
if N > N1 and N > N2 :
	print ('El numero ' , N , ' es el numero mas grande.')
elif N1 > N2 and N1 > N :
	print ('El numero ', N1 , ' es el numero mas grande.')
elif N2 > N and N2 > N1 :
	print ('El numero ', N2 , ' es el numero mas grande.')