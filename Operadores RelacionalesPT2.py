print ('            *****OPERADORES RELACIONALES*****              ')
N = input ('Hola usuario cual es tu nombre?: ')
print ('Hola ', N, ',vamos a calcular tu calificacion y la compararemos con la de otro estudiante.')
M = float (input (N + ' Por favor ingresa en numero tu calificacion en Matematicas: '))
Q = float (input ('Ahora propórcioname tu calificacion en Quimica: '))
I = float (input('Por ultimo ' + N + ', ingresa tu calificacion en ingles: '))
Prom = (M + Q + I)/3
Apr = 6
Prom1 = float (input (N + ' Ahora propórcioname el promedio de tu compaÑero: '))
if Prom < Apr :
	print ('Que decepcion  ', N, ' tu calificacion es de', Prom, ' y no es aprobatoria.')
	if Prom1 <= Apr :
		print ('Tanto tu como tu compaÑero son un caso perdido. :) tu calificacion final fue de ')
	if Prom1 >= Apr :
		print (N, ' Deberias sentir verguenza al saber que tu compaÑero si aprobo, tu calificacion final fue de ')
if Prom > Apr :
	print ('Felicitaciones ', N, ' tu calificacion final due de', Prom, ' y es aprobatoria.')
	if Prom1 >= Apr :
		print ('Felicitense ambos aprobaron')
	if Prom1 <= Apr :
		print ('Sientete orgulloso ', N, ' a comparacion de tu compaÑero TU SI APROBASTE.')
if Prom == Apr :
	print ('Apenas y aprobaste, esfuerzate mas. tu calificacion fue de ', Prom)
	if Prom1 == Apr :
		print ('Ambos estan en la linea, deberian estudiar juntos.')
	if Prom1 <= Apr :
		print ('No eres el mejor estudiante pero ayudar a un compaÑero nunca esta por de mas.')