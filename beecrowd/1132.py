a = int(input())
b = int(input())

lista = []

if a > b:
  for x in range(b,a+1):
    if x%13 != 0:
      lista.append(x)
else:
  for x in range(a,b+1):
    if x%13 != 0:
      lista.append(x)  

print(sum(lista))