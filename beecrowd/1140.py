while True:

    a = input().split(' ')

    if '*' in a:
        break

    t = len(set([x[0].upper() for x in a]))
    
    print('Y' if t == 1 else 'N')