def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)

n = int(input())

for x in range(n):

    f1,f2 = map(int,input().split())

    print(MDC(f1,f2))
