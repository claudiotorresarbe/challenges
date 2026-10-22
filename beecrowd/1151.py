n = int(input())
fibo = []
if 0 < n < 46:
    for x in range(n):
        if x == 0:
            fibo.append(x)
        elif x == 1:
            fibo.append(x)
        else:
            fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])
    str1 = ' '.join([str(x) for x in fibo])
    print(str1)