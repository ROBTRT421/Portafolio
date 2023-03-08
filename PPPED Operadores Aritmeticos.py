#Se le solciita desarrollar una calculadora con las siguientes caractersticas:
#1.- La calculadora debera ser capaz de calcular las operaciones de suma, resta, 
#multiplicacion, division, division entera, exponente y modulo o resto.
#2.- La calculadora debera tener un menu de opciones donde el usuario pueda elegir
#cual es la operacion que desea ejecutar.
#3.- La calculadora debera solicitar unicamente dos valores por cada operacion.
#**REQUERIMIENTOS INDISPENSABLES**
#El codigo de este programa debera funcionar con una unica variable que se llamara 
#'numero', es decir, no se permite la implementacion de otra variable.
print ('Calculadora con una sola variable \n')
print ('********************')
print ('* Menu de Opciones *')
print ('******************** \n')
print ('1. Suma')
print ('2. Resta')
print ('3. Multiplicacion')
print ('4. Division')
print ('5. Division Entera')
print ('6. Exponente')
print ('7. Modulo o Resto \n')
numero = int (input ('Introduce la opcion Deseada :'))
if numero == 1 :
	print ('Elegiste la Suma.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero += int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado de la Suma es: ' , numero )
elif numero == 2 :
	print ('Elegiste la Resta.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero -= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado de la Resta es: ' , numero )
elif numero == 3 :
	print ('Elegiste la Multiplicacion.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero *= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado de la Multiplicacion es: ' , numero )
elif numero == 4 :
	print ('Elegiste la Division.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero /= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado de la Division es: ' , numero )
elif numero == 5 :
	print ('Elegiste la Division Entera.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero //= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado de la Division Entera es: ' , numero )
elif numero == 6 :
	print ('Elegiste el Exponente.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero **= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado del Exponente es : ' , numero )
elif numero == 7 :
	print ('Elegiste el Modulo o Resto.\n')
	numero = int (input ('Introduce el Primer Numero: '))
	numero %= int (input ('Introduce el Segundo Numero: '))
	print ('El Resultado del Modulo o Resto es: ' , numero )
