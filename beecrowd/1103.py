while True:

    h1,m1,h2,m2 = map(int,input().split())

    if h1 == m1 == h2 == m2 == 0:
        break

    horas = 0

    if h2 == 0:
        horas = ((24 - h1) * 60)
    elif h2 > 0 and h2 > h1:
        horas = ((h2 - h1) * 60)
    elif h2 < h1:
        horas = (((h2+24) - h1) * 60)
    elif h1 == h2 and m2 < m1:
        horas = 24*60
    print(horas + (m2 - m1))