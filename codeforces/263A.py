linha = 0
qtd = 0
col = 0
for x in range(5):
    a = list(map(int,input().split(' ')))
    
    try:
        if a.count(1):
            linha = qtd
            col = a.index(1)
    except:
        pass
 
    qtd += 1
 
result = abs((linha - 2)) + abs((col - 2))
print(result)