n, k = map(int,input().split(' '))
 
z = list(map(int,input().split(' ')))
 
ref = z[k-1]
 
qtd = 0
 
for x in z:
 
    if x >= ref and x > 0:
        qtd += 1
 
print(qtd)
