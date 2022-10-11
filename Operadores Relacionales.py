print ('                              ***Operadores Relacionales***                     \n')
print ("""Los operadores Realacionales son simbolos que se usan para comparar dos valores, y generalmente son utilizados en las sentencias condicionales para la toma de decisiones. Al utilizar operadores relacionales dentro de una sentencia condicional, si el resultado de la comparacion es correcto, la expresion o condicion es considerada verdadera (true), y en caso contrario sera falsa (false). """)
print ('Los operadores relacionales en python son los siguientes')
print ("(<) este operador nos indica que la variable 'es menor que'.")
print ("(>) este operador indica que la varibale es 'mayor que'.")
print ("(==) este operador indica que las variables 'son iguales'. ")
print ("(!=) este operador indica que las variables 'no son iguales/diferente'.")
print ("(<=) este operador indica que las variables son 'igual o menor que'.")
print ("(>=) este operador indica que las variables son 'igual o mayor que'. ")
print ("\n                      ***Practica Propuesta por el Doscente***                   \n")
print ('Introduce dos numeros a comparar. \n')
N = int (input ('Introduce el primer numero: '))
N1 = int (input ('Introduce el segundo numero: '))

print ('\n Los numeros a comparar son :' , N , ' y ' ,N1, "\n") 

if N < N1 :
	print ('Es menor que...')
if N > N1 :
	print ('Es mayor que...')
if N == N1 :
	print ('Son Iguales...')
if N != N1 :
	print ('Es Diferente...')
if N <= N1 :
	print ('Es menor o igual...')
if N >= N1 :
	print ('Es mayor o igual...')











