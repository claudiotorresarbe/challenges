numeros = []
a = int(input())

if a < 10000:
  for x in range(0,a):
    b = int(input())
    numeros.append(b)

qtdin = qtdout = 0

for y in numeros:
  if (-10**7) < y < (10**7):
    if 10 <= y <= 20:
      qtdin += 1
    else:
      qtdout += 1

print(qtdin,'in')
print(qtdout,'out')