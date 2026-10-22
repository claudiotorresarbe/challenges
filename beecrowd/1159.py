while True:
  x = int(input())
  soma = 0
  if x == 0:
    break

  nro = x
  soma = 0
  row = 0
  while True:
    if nro % 2 == 0:
      soma = soma + nro
      row += 1
    nro += 1
    if row == 5:
      break
  print(soma)