n = int(input())
 
for x in range(n):
    a,b = list(map(int,input().split()))
 
    mod = a % b
    print((b - mod) % b)