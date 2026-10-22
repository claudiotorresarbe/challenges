n = int(input())
if 1 <= n <= 100:
    for x in range(0,n):
        y = int(input())
        qtd = 0
        if 1 < y <= (10**7):
            for z in range(1,y+1):
                #print(y,z,y%z,qtd)
                if y%z == 0:
                    qtd += 1
            if qtd > 2:
                print(y,'nao eh primo')
            else:
                print(y,'eh primo')