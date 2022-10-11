print ('\n                       ***Sentencias Condicionales Anidadas***                        \n')
N = input ('Hola usuario Cual es tu nombre?: ')
if N == 'Doris' :
	print ('Credenciales aceptadas')
	F = int (input ('Hola Doris, Roberto tiene un mensaje para ti, pero antes digita su fecha de nacimiento,\ntomando dos digitos para el dia, dos para el mes \ny dos para el aN*o ejemplo: (205841): '))
	if F == 301194 :
		print ('Credenciales aceptadas, el mensaje es el siguiente.')
		print ( 'Doris, TE AMO TE AMO COMO\n NUNCA HABIA AMADO ANTES A AGLUIEN, QUEDATE SIEMPRE A MI LADO.\n')
	else :
		print ('Credenciales Erroneas Fin del programa')
else :
	print ('Credenciales Erroneas Fin del programa.')