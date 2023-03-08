print ('En Python, los bucles o ciclos pueden ser interrumpidos, o simplemente,')
print ('dejar de ejecutar el codigo que se encuentre dentro del bucle e iniciar una nueva interacion.')
print ('Cabe destacar que en programacion una interacion es la repeticion de un segmento de codigo')
print ('dentro de un programa. Para lograr la interrupcion de una interacion, contamos con las')
print ('sentencias break y continue. \n ')
print ('****SENTENCIA BREAK*****')
print ('En Python, la sentencia break se utiliza para detener la ejecucion de una interacion y salir de ella')
print ('con lo cual, el programa podra continuar con la ejecucion del codigo que se encuentre fuera de')
print ('nuestro bucle\n')
print ('Ejemplo para Break\n')
print ('While con la sentencia break \n')
contador = 0
while contador < 10:
	contador += 1
	if contador == 5:
		break 
	print ('Valor actual de la variable: ', contador)
print ('Fin del programa, la sentencia break se ah ejecutado.\n')
print ('*****SENTENCIA CONTINUE*****')
print ('Por otro lado, en Python, tambien contamos con la sentencia continue, la cual permite detener la interacion')
print ('actual y volver al principio del bucle para realizar una nueva interacion, si es que la condicion que')
print ('rige a nuestro bucle se sigue cumpliendo.')
print ('Recordemos que en programacion una interacion es la repeticion de un segmento de codigo dentro de un programa.\n')
print ('Ejemplo para Continue\n')
print ('While con la sentencia continue \n')
contador = 0
while contador < 10:
	contador += 1
	if contador == 5:
		continue 
	print ('Valor actual de la variable: ', contador)
print ('Fin del programa, la sentencia continue se ah ejecutado.\n')