n = int(input())
 
result = 0
l = list(map(int,input().split()))
 
if l.count(1):
    result = 1
 
if result == 1:
    print('HARD')
else:
    print('EASY')