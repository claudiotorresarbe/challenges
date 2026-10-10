lista = []
total = 0
for x in range(0,2):
    a = int(input())
    lista.append(a)

for y in range(min(lista)+1,max(lista)):
    if y % 2 == 1:
        total = total + y

print(total)