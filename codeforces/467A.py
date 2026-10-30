n = int(input())
 
quartos = 0
for x in range(n):
    a,b = list(map(int,input().split()))
 
    if b - a >= 2:
        quartos += 1
 
print(quartos)
