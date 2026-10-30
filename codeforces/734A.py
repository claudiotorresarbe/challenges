a = int(input())
b = input()
 
txt = [x for x in b]
 
d = txt.count('D')
a = txt.count('A')
 
if d > a:
    print('Danik')
elif d < a:
    print('Anton')
else:
    print('Friendship')