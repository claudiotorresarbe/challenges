qtd = 0
notas = []
while True:
    if qtd == 2:
        print('media =','%.2f'%(sum(notas)/len(notas)))
        break
    else:
        x = float(input())
        if 0 < x < 11:
            notas.append(x)
            qtd += 1
        else:
            print('nota invalida')