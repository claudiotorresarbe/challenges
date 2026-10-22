lista = []

while True:
  x = int(input())
  if x < 0:
    print('%.2f'%(sum(lista)/len(lista)))
    break
  else:
    lista.append(x)