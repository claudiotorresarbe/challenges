a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
qtd = 0
for x in range(a[0]):
 
    if b[x] // a[1] == 0 and b[x] % a[1] > 0:
        qtd += 1
    elif b[x] // a[1] > 0 and b[x] % a[1] == 0:
        qtd += b[x] // a[1]
    elif b[x] // a[1] > 0 and b[x] % a[1] > 0:
        qtd += 2
print(qtd)
