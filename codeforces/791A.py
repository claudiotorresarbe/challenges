limak,bob = map(int,input().split(' '))
 
ano = 0
while True:
 
    if limak > bob:
        print(ano)
        break
    limak *= 3
    bob *= 2
    ano += 1