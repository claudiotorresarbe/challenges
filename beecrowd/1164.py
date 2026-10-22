n = int(input())
if 1 <= n <= 20:
    for x in range(0,n):
        y = int(input())
        soma = 0
        if 1 <= y <= (10**8):
            for z in range(1,y):
                if y%z == 0:
                    soma = soma + z
            if soma == y:
                print(y,'eh perfeito')
            else:
                print(y,'nao eh perfeito')