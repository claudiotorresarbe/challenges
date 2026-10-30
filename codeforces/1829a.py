n = int(input())
 
t = 'codeforces'
tt = [x for x in t]
 
for x in range(n):
 
    a = input()
    aa = [z for z in a]
 
    qtd = 0
    for y in range(len(aa)):
        
        if tt[y] != aa[y]:
            qtd += 1
 
    print(qtd)