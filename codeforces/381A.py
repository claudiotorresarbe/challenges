n = int(input())
l = list(map(int,input().split()))
 
s = []
d = []
for x in range(n):
    valor_e = l[0]
    valor_d = l[-1]
 
    valor = 0
    if valor_e > valor_d:
        valor = valor_e
    else:
        valor = valor_d
 
    if x % 2 == 0:
        s.append(valor)
    else:
        d.append(valor)
    l.remove(valor)
 
print(sum(s),sum(d))