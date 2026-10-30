linhas, colunas = list(map(int,input().split()))

l0 = '#' * colunas
l1 = '.' * (colunas-1) + '#'

s = 0
for x in range(linhas):
    if x % 2 == 0:
        print(l0)
    else:
        if s == 0:
            print(l1)
            s = 1
        else:
            print(l1[::-1])
            s = 0