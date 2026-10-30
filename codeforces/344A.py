n = int(input())
 
l = []
xa = None
qtd = 0
for x in range(n):
    z = input()
 
    if xa != z:
        xa = z
        qtd += 1
 
print(qtd)