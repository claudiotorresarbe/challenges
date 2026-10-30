n, k = list(map(int,input().split()))
 
calc = 240 - k
tempo = 0
acumulado = 0
s = 0
for x in range(1,n+1):
 
    tempo += 5
    acumulado += tempo
    
    if acumulado > calc:
        s = 1
        print(x-1)
        break
 
    #print(calc,x,tempo, acumulado > calc)
 
if s == 0:
    print(x)