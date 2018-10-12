while(1):
    x = int(input())
    if(x==0):
        break
    
    x,y = map(int,input().split())
    for i in range(x):
        x1, y1 = map(int,input().split())
        if(x1 == x or y1 == y):
            print('divisa')
        elif(x1>x and y1>y):
            print('NE')
        elif(x1<x and y1>y):
            print('NO')
        elif(x1>x and y1<y):
            print('SE')
        else:
            print('SO')
	
