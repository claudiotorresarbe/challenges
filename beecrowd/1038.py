preco = [4,4.5,5,2,1.5]

a = input()

codigo = int(a.split(' ')[0])
qtd = int(a.split(' ')[1])

total = (preco[codigo-1]*qtd)+0.000001

print('Total: R$',str(total)[:-4])