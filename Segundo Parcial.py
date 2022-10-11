print ('                               *SEGUNDO PARCIAL*                                \n')

print ('                 ***Sentencias Condicionales***                \n')
print ('Ejercicio # Sentencia condicional (if) \n')
N = input ('Hola usuario, cual es tu nombre?: ')
print ('Hola ' + N + ', vamos a calcular tu calificacion. \n')
E = int (input('Por favor ingresa tu calificacion de la materia EspaNol: ' ))
M = int (input ('Por favor ingresa tu calificacion de la materia Matematicas: '))
I = int (input ('Por favor ingresa tu calificacion de la materia Ingles: '))
Q = int (input ('Por favor ingresa tu calificacion de la materia Quimica: '))
F = int (input ('Por favor ingresa tu calificacion de la materia Fisica: '))
D = int (input ('Por favor ingresa tu calificacion de la materia Deportes: '))
Prom = (E + M + I + Q + F + D) /5
if Prom >= 6 :
	print ('Felicitaciones ' + N + ', Haz aprobado el curso con un promedio de: ', Prom)
if Prom <= 6 :
	print ('Lo sientop ' + N + ', NO haz aprobado el curso, tu promedio fue de: ', Prom)
print ('Fin del primer programa. \n')
######
print ('Hola se que  haz tenido un dia pesado calculemos las ganancias de hoy.')
En = int (input ('Por favor ingresa la entrada total de dinero: '))
Sa = int (input ('Ahora ingresemos la salida de dinero y/o el pago de proveedores: '))
Din = En - Sa
print ('La cantidad de dinero que sobro es', Din)
if Din >= 25 :
	print ('Felicitaciones ganas mas que el salario minimo.') 
if Din <= 25 :
	print ('Deberian darte verguenza tus finanzas. ')
print (' \n Recuerda que el salario actual en mexico es de 25pesos por hora trabajada.')
##########################################################################################
print ('\n                 ***Sentencias Condicionales Multiples***                \n')

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
############################################################################################
print ('\n                       ***Sentencias Condicionales Anidadas***                        \n')
N = input ('Hola usuario Cual es tu nombre?: ')
if N == 'Doris' :
	print ('Credenciales aceptadas')
	F = int (input ('Hola Doris, Roberto tiene un mensaje para ti, pero antes digita su fecha de nacimiento, tomando dos digitos para el dia, dos para el mes y dos para el aN*o ejemplo: (205841): '))
	if F == 301194 :
		print ('Credenciales aceptadas, el mensaje es el siguiente.')
		print ( 'Doris, TE AMO TE AMO COMO NUNCA HABIA AMADO ANTES A AGLUIEN, QUEDATE SIEMPRE A MI LADO.')
	else :
		print ('Credenciales Erroneas Fin del programa')
else :
	print ('Credenciales Erroneas Fin del programa.')