data = []

for x in range(0,3):
    valor = input()

    data.append(valor)

if data[0] == 'vertebrado':
    if data[1] == 'ave':
        if data[2] == 'carnivoro':
            print('aguia')
        elif data[2] == 'onivoro':
            print('pomba')
    elif data[1] == 'mamifero':
        if data[2] == 'onivoro':
            print('homem')
        elif data[2] == 'herbivoro':
            print('vaca')
elif data[0] == 'invertebrado':
    if data[1] == 'inseto':
        if data[2] == 'hematofago':
            print('pulga')
        elif data[2] == 'herbivoro':
            print('lagarta')
    elif data[1] == 'anelideo':
        if data[2] == 'hematofago':
            print('sanguessuga')
        elif data[2] == 'onivoro':
            print('minhoca')