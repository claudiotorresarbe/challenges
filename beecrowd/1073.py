x = int(input())

if 5 < x < 2000:
    for x in range(1,x+1):
        if x%2 == 0:
            print(str(x)+'^2 =',x**2)