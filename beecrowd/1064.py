lista = []
for x in range(0,6):
    a = float(input())
    lista.append(a)

positivos = 0
media = []
for y in lista:
    if y > 0:
        positivos += 1
        media.append(y)

if positivos >= 1:
    print(positivos,'valores positivos')
    print('%.1f'%(sum(media)/len(media)))