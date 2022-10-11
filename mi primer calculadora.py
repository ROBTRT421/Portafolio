print ('                    ***MI PRIMER CALCULADORA***                   \n')
N = input ('Hola usuario cual es tu nombre?: ')
print ('Bienvenido ' + N + ', hoy vamos a realizar algunas operaciones con ayuda de esta calculadora.')
Op = int (input ("Por favor digita una opcion del 1 al 5: ('1.Suma') ('2.Resta') ('3.Multiplicacion') ('4.Division'). ('5.Salir') \n") )
if Op == 1 :
	print ("Muy bien vamos ayudarte a sumar. \n")
	N1 = int (input ('Elige el primer digito a sumar. '))
	N2 = int (input ('Elige el segundo digito a sumar. '))
	N3 = int (input ('Y porque no? elige uno mas. '))
	R1 = N1 + N2 + N3
	print ('El resultado de la suma es ', R1 )
elif Op == 2 :
	print ("Muy bien vamos ayudarte a restar. \n")
	N1 = int (input ('Elige el primer digito a restar. '))
	N2 = int (input ('Elige el segundo digito a restar. '))
	N3 = int (input ('Y porque no? elige uno mas. '))
	R1 = N1 - N2 - N3
	print ('El resultado de la resta es ', R1 )
elif Op == 3 :
	print ("Muy bien vamos ayudarte a multiplicar. \n")
	N1 = int (input ('Elige el primer digito a multiplicar. '))
	N2 = int (input ('Elige el segundo digito a multiplicar. '))
	N3 = int (input ('Y porque no? elige uno mas. '))
	R1 = N1 * N2 * N3
	print ('El resultado de la Multiplicacion es ', R1 )
elif Op == 4 :
	print ("Muy bien vamos ayudarte a dividir. \n")
	N1 = int (input ('Elige el primer digito a dividir. '))
	N2 = int (input ('Elige el segundo digito a dividir. '))
	N3 = int (input ('Y porque no? elige uno mas. '))
	R1 = N1 / N2 / N3
	print ('El resultado de la Division es ', R1 )
elif Op == 5 :
	print ('Ok')
else :
	print ('Opcion no valida.')
print ('Fin del programa')
