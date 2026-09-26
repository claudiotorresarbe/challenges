total = 0
for x in range(1,3):
    a,b,c = input().split(' ')

    total = total + (int(b)*float(c))+0.001

print('VALOR A PAGAR: R$',"{:.2f}".format(total))
