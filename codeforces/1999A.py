n = int(input())
 
for x in range(n):
    p = int(input())
 
    z = [int(x) for x in str(p)]
 
    print(sum(z))