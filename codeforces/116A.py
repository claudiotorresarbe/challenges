n = int(input())
 
maximo = 0
entsai = 0
for x in range(n):
    a,b = list(map(int,input().split()))
 
    entsai = (entsai - a) + b
 
    if entsai > maximo:
        maximo = entsai
 
print(maximo)
