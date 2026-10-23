n = int(input())

for x in range(n):
    a = input()

    if a == 'P=NP':
        print('skipped')
    else:
        a2 = [int(x) for x in a.split('+')]
        print(sum(a2))