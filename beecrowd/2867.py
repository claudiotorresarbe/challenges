a = int(input())

for b in range(a):
    m,n = map(int,input().split())
    r = len(str(m**n))
    print(r)