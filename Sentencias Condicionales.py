print ('                                        ***SENTENCIAS CONDICIONALES****                           ')
print ("""Una sentencia condicional, es una instruccion o grupo de instrcciones, que
se ejecutan cuando a un programa se le establece una condicion logica. Al cumplirse 
dicha condicion, el programa ejecuta la instruccion que ha sido asignada a esta condicion.
Las sentencias condicionales, nos ayudan ah controlar la toma de deciciones dentro de un programa,
haciendo uso de la logica.
De esta manera, las sentencias condicionales comprueban, si una condicion es verdadera o falsa
y con base a eso se lleva a cabo una accion.
En Python, la sintaxis para las sentencias condicionales son las siguientes:""")
print ('                                                                                                  ')
print ('                                                                                                  ')
print ('-1.- Sentencias condicionales Simples')
print (""" *if* condicion logica : 
                     Instruccion
                     Instruccion
                     Instruccion 
Instruccion""") 
print ('                                                                                                  ')
print ('                                                                                                  ')
######################
print ('Ejemplo #1 Sentencias condicionales Simples')
print ('                                                                                                  ')
num_uno = 5
if num_uno == 5 :
	print ('El numero es 5')
print ('FIN')
print ('                                                                                                  ')
print ('                                                                                                  ')
#####################
print ('Practica Propuesta por el Maestro #1')
print ('                                                                                                  ')
print ('                                                                                                  ')
nombre = input ('Hola Usuario cual es tu nombre?: ')
print ('Hola ' + nombre + ', vamos a calcular tu calificacion')
M = int (input ('Por favor proporcioname tu calificacion en Matematicas: '))
Q = int (input ('Ahora proporcioname tu calificacion en Quimica: '))
I = int (input ('Y por ultimo tu calificacion en Ingles: '))
Prom = (M + Q + I) / 3
if Prom >= 6 :
	print ('Felicitaciones ' + nombre + ' Haz "aprobado" el Curso', Prom )
if Prom <= 6 :
	print ('Lo siento ' + nombre + ' No haz "aprobado" el Curso', Prom)
print ('FIN')
#############################################
print ('                                                  ')
print ('                                                  ')
print ('Ejemplo #2 Sentencias condicionales (if)')
N = 6 
if N >= 6:
	print ('True')
print ('FIN')
print ('                                                  ')
print ('Ejemplo #3 Sentencias condicionales (if)')
N1 = 10
if N1 == 10:
	print ('El numero es 10')
print ('FIN')









