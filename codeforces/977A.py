a, b = list(map(int,input().split()))
 
val = a
for x in range(b):
    if val % 10 != 0:
        val -= 1
    elif val % 10 == 0:
        val = val / 10
 
print(int(val))