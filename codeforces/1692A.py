n = int(input())
 
for x in range(n):
    a,b,c,d = list(map(int,input().split()))
 
    qtd = 0
 
    if a < b:
        qtd += 1
    if a < c:
        qtd += 1
    if a < d:
        qtd += 1
    
    print(qtd)
