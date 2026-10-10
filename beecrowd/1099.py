x = int(input())
for y in range(0,x):
    qtd = 0
    a,b = input().split(' ')
    a = int(a)
    b = int(b)
    if a > b:
        for z in range(b+1,a):
            if z%2 == 1:
                qtd = qtd + z
        print(qtd)
    else:
        for z in range(a+1,b):
            if z%2 == 1:
                qtd = qtd + z
        print(qtd)