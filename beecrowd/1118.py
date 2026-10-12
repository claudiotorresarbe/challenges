lista = []
y = 0

while y == 0:

  n = float(input())
  x = 0

  if 1 <= n <= 10:
    lista.append(n)
  else:
    print('nota invalida')

  if len(lista) == 2:
    valor = sum(lista)/2
    print(f"media = {'%.2f'%valor}")
    x = 1

  while x == 1:
    print('novo calculo (1-sim 2-nao)')
    p = int(input())

    if p == 1 or p == 2:

      if p == 2:
        y = 1
        break
      else:
        lista.clear()
        x = 0
        
    else:
      x = 1