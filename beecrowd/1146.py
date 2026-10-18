while True:
    x = int(input())
    valor = ''
    if x != 0:
        for n in range(1,x+1):
            if n == 1:
                valor = str(n)
            else:
                valor = valor + ' ' + str(n)
        print(valor)
    else:
        break