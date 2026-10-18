a = input().split(' ')

lista = [int(x) for x in a]
nova = []
soma = 0
for x in lista:
    if x > 0:
        nova.append(x)
a = nova[0]
b = nova[1]

for y in range(a,a+b):
    soma = soma+y
print(soma)