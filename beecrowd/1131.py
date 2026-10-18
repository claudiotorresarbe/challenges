grenais = 0
inter = 0
gremio = 0
empates = 0
while True:
    x = input().split(' ')
    grenais += 1
    if int(x[0]) > int(x[1]):
        inter += 1
    elif int(x[0]) < int(x[1]):
        gremio += 1
    elif int(x[0]) == int(x[1]):
        empates += 1

    if len(x) == 2:
        print('Novo grenal (1-sim 2-nao)')
        y = input()
        if int(y) == 1:
            pass
        elif int(y) == 2:
            print(str(grenais),'grenais')
            print('Inter:'+str(inter))
            print('Gremio:'+str(gremio))
            print('Empates:'+str(empates))
            if inter > gremio:
                print('Inter venceu mais')
            elif inter < gremio:
                print('Gremio venceu mais')
            elif inter == gremio:
                print('Nao houve vencedor')
            break