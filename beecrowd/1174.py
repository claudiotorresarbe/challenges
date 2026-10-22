lista = []
for x in range(0,100):
  a = float(input())
  lista.append(a)

for y in range(0,len(lista)):
  if lista[y] <= 10:
    print(f'A[{y}] =','%.1f'%lista[y])