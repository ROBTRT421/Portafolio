print ("                                    ***Operadores Logicos***                           ")
print ("""En ocasiones, es necesario utilizar mas de dos condiciones logicas dentro de una misma condicion, con lo cual nos vemos en la necesidad de implementar multiples operadores relacionales para crear una expresion logica mucho mas compleja. Sin embargo, no es posible colocar dos condiciones logicas dentro de una misma condicion, sin el apoyo de algun elmento que les indique a nuestros programas, que se realizara la union de dos o mas condiciones logicas dentro de una misma expresion. Para este tipo de situaciones existen los operadores logicos, los cuales, permiten agrupar condiciones logicas dentro de una misma condicion. Es decir, con los operadores logicos tenemos la posibilidad de utilizar multiples operadores relacionales dentro de una misma condicion logica. """)
print ('En python, contamos con tres tipos de operadores logicos: ')
print ("Conjuncion  ('and')   ")
print ("Disyuncion  ('or')    ")
print ("Negacion    ('not')   \n")
print ("*Ejemplo Operador. ('and') \n")
N = 5
N1 = 5
if N == 5 and N1 >= 5 :
	print ('Ambas condiciones se han cumplido \n')

N2 = 5
N3 = 2
if N2 == 5 and N3 >= 5 :
	print ('Ambas condiciones se han cumplido \n')

else :
	print ('Una o ambas condiciones no se ha cumplido. \n')

print ("*Ejemplo Operador. ('or') \n")
N4 = 5
N5 = 2
if N4 == 5 or N5 >= 5 :
	print ('Una o ambas condiciones se ha cumplido. \n')

N6 = 8
N7 = 2
if N6 == 5 or N7 >= 5 :
	print ('Una o ambas condiciones se ha cumplido. \n')

else :
	print ('Ninguna condicion se ha cumplido. \n')

print ("*Ejemplo Operador. ('not')  \n")
N8 = 2
if not N8 >= 5 :
	print ('La condicion se invirtio y se cumple al ser un numero menor o igual a 5. \n')

N9 = 9
if not N9 >= 5 :
	print ('La condicion se invirtio y se cumple al ser un numero menor o igual a 5. \n')
else :
	print ('No se cumple la condicion porque el numero es mayor a 5. \n')

print (' ***Practica Propuesta por el Doscente*** ')
print ('Conjuncion (and) .\n')
num_uno = int (input ('Escribe un numero mayor a 2 y menor que 5: '))
if num_uno >2 and num_uno <5 :
		print ('El numero ', num_uno, 'Cumple con la condicion. \n')
else :
	print ('El numero ' ,num_uno, ' No cumple con la condicion \n')
print ('Disyuncion (or) \n')
palabra = input ('Para complir con la condicion escrribe "si" o la palabra "yes": ')
if palabra == 'si' or 'yes' :
	print ('La condicion se ha cumplido \n')
else :
	print ('No se ha cumplido. \n')
print ('Negacion (not) ')
num_dos = int (input ('Introduce un numero igual a 5: '))
if not num_dos == 5 :
	print ('\n El numero es diferente a 5 y si se cumple la condicion. \n')
else :
	print ('El numero es igual a 5 y No se cumple la condicion. ')
