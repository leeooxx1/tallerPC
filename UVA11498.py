x=input()


#poner raw input dentro de un loop qu este determinado por la cantidad de variables a ingresar y asi resolvemos el problema
#de los multiples input evitando que se cierre el programa

for i in range(x):
	y,x=map(input())
	print(y)
	print(x)