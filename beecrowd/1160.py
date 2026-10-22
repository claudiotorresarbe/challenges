t = int(input())

for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    ano = 0

    while pa <= pb:
        pa = int(pa + pa * (g1/100))
        pb = int(pb + pb * (g2/100))
        ano = ano + 1
        if ano > 100:
            break

    if ano > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(ano))