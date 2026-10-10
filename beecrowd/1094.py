n = int(input())
c = []
r = []
s = []
for x in range(0,n):
    quantia,tipo = input().split(' ')
    quantia = int(quantia)
    tipo = str(tipo)
    if 1 <= quantia <= 15:
        if tipo == 'C':
            c.append(quantia)
        elif tipo == 'R':
            r.append(quantia)
        elif tipo == 'S':
            s.append(quantia)

print(f"Total: {sum(c+r+s)} cobaias")
print(f"Total de coelhos: {sum(c)}")
print(f"Total de ratos: {sum(r)}")
print(f"Total de sapos: {sum(s)}")
print(f"Percentual de coelhos: {'%.2f'%((sum(c)/sum(c+r+s))*100)} %")
print(f"Percentual de ratos: {'%.2f'%((sum(r)/sum(c+r+s))*100)} %")
print(f"Percentual de sapos: {'%.2f'%((sum(s)/sum(c+r+s))*100)} %")