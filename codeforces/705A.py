n = int(input())
l = []
 
for x in range(n):
    if x % 2 != 0:
        l.append('I love')
    else:
        l.append('I hate')
 
print(' that '.join([x for x in l]) + ' it')