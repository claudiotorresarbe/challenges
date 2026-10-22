lista = []
for x in range(10):
    a = int(input())
    lista.append(a)

lista = [x if x > 0 else 1 for x in lista]

for y in range(0,len(lista)):
    print(f'X[{y}] = {lista[y]}')