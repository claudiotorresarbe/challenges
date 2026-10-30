n = int(input())
 
result = 0
for x in range(n):
    a,b,c = map(int,input().split())
    
    if a + b + c >= 2:
        result += 1
    
print(result)