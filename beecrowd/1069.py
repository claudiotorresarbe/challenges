n = int(input())
for x in range(n):
  m = input().replace('.','')
  qtd = 0
  texto = m
  for y in m:
    qtd += texto.count('<>')
    texto = texto.replace('<>','')
  print(qtd)