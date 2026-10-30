n = int(input())
x = list(map(int, input().split(' ')))
y = list(map(int, input().split(' ')))

nivel = set(x[1:] + y[1:])

if len(nivel) == n and max(nivel) == n :
    print('I become the guy.')
else:
    print('Oh, my keyboard!')