valor = int(input())
 
n = 0
for x in range(5,0,-1):
    resta = valor//x
    
    if resta > 0:
        n += resta
 
    valor -= resta * x
    
print(n)