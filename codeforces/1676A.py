n = int(input())
 
for x in range(n):
    l = input()
    li = [int(x) for x in l]
    
    print('YES' if sum(li[0:3]) == sum(li[3:6]) else 'NO')