n=int(raw_input("ingrese numero"))
a=0
b=0
x=1

print(1)
for i in range(0,n-1):
	b=a
	a=x
	x=a+b
	print(x)
	