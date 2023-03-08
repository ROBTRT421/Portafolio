print ('                                 ***EXAMEN***                                \n')
#La Empresa multinacional Rappi, solicita un sistema que determine los dias de vacaciones 
#a los que tiene derecho un trabajador, tomando en cuenta las siguientes caracteristicas:
#Existen tres departamentos dentro de la empresa con sus respectivas claves:
#1.- Departamento de Atencion al cliente, (Clave 1)
#   *Con 1 a/o de servicio, reciben 6 dias de vacaciones.
#   *Con 2 a 6 a/os de servicio, reciben 14 dias de vacaciones.
#   *A partir de 7 a/os de servicio. reciben 20 dias de vacaciones.
#2.- Departamento de Logistica. (Clave 2)
#   *Con 1 a/o de servicio, reciben 7 dias de vacaciones.
#   *Con 2 a 6 a/os de servicio, reciben 15 dias de vacaciones.
#   *A partir de 7 a/os de servicio, reciben 22 dias de vacaciones.
#3.- Gerencia. (Clave 3)
#   *Con un 1 a/o de servicio, reciben 10 dias de vacaciones.
#   *Con 2 a 6 a/os de servicio, reciben 20 dias de vacaciones.
#   *A partir de 7 a/os de servicio, reciben 30 dias de vacaciones.
#REQUERIMIENTOS INDISPENSABLES:
#El sistema debe solicitar el Nombre, Clave de departamento y Antiguedad del trabajador desde teclado.
#Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre del trabajador y los 
#dias de vacaciones a los que tiene derecho.###
print ('========================================================')
print ('| S I S T E M A   V A C A C I O N A L   D E   R A P P I |')
print ('========================================================')
N = (input ('Hola Usuario cual es tu nombre?: '))
C = int (input ('Hola ' + N + ', Por favor digita la clave del departamento al cual perteneces: '))
if C == 1 :
	print ('Perfecto perteneces al Departamento de Atencion al Cliente. \n')
	A = int (input ('Ahora proporcioname en a/os tu Antiguedad en la empresa: '))
	if A == 1 :
		print ('Excelente ' + N + ', Tus dias de vacaciones son 6.')
	elif A >= 2 and A <= 6 :
		print ('Excelente ' + N + ', Tus dias de vacaciones son 14.')
	elif A >= 7 :
		print ('Felicitaciones ' + N + ', Tus dias de vacaciones son 20.')
elif C == 2:
	print ('Perfecto perteneces al Departamento de Logistica. \n')
	A = int (input ('Ahora proporcioname en a/os tu Antiguedad en la empresa: '))
	if A ==  1:
		print ('Excelente ' + N + ', Tus dias de vacaciones son 7.')
	elif A >= 2 and A <= 6 :
		print ('Excelente ' + N + ', Tus dias de vacaciones son 15.')
	elif A >= 7 :
		print ('Felicitaciones ' + N + '. Tus dias de vacaciones son 22.')
elif C == 3 :
	print ('Perfecto perteneces al Area de Gerencia. \n')
	A = int (input ('Ahora proporcioname en a/os tu Antiguedad en la empresa: '))
	if A == 1 :
		print ('Excelente ' + N + ', Tus  dias de vacaciones son 10.')
	elif A >= 2 and A <= 6 :
		print ('Excelente ' + N + ', Tus dias de vacaciones son 20.')
	elif A >= 7 :
		print ('Felicitaciones ' + N + ', Tus dias de vacaciones son 30.')
else :
	print ('Clave no reconocida, vuelve a intentarlo.')
