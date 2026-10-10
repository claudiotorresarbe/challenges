x = int(input())

if 1 <= x <= 1000:
    for x in range(0,x+1):
        if x%2 != 0:
            print(x)