while True:

    n = int(input())

    if n == 0:
        break

    num = [z for z in range(1,n+1)]
    disc = []

    if n == 1:
            print(1)

    for x in range(n-1):
        disc.append(num[0])
        num.pop(0)
        num.append(num[0])
        num.pop(0)

    print('Discarded cards:',', '.join([str(x) for x in disc]))
    print('Remaining card:',num[0])
