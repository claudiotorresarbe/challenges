x = int(input())
if 1 < x < 1000:
    for a in range(1,x+1):
        for b in range(0,2):
            print(a,(a**2)+b,(a**3)+b)