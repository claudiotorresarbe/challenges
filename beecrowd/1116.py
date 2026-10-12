resultado = []

for x in range(0,1):
  nro = input()
  for y in range(0,int(nro)):
    a,b = input().split(' ')
    try:
      calculo = int(a) / int(b)
      resultado.append(calculo)
    except:
      resultado.append('divisao impossivel')

for z in resultado:
  print(z)