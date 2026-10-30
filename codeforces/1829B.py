n = int(input())
 
for x in range(n):
    l = input()
    m = list(map(str,input().replace(' ','').split('1')))
    
    qtd = 0
    for x in m:
        
        if qtd < len(x):
            qtd = len(x)
 
    print(qtd)