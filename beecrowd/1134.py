a = []
g = []
d = []
while True:
    x = int(input())
    if x == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {sum(a)}')
        print(f'Gasolina: {sum(g)}')
        print(f'Diesel: {sum(d)}')
        break
    if 1 <= x < 4:
        if x == 1:
            a.append(1)
        elif x == 2:
            g.append(1)
        elif x == 3:
            d.append(1)