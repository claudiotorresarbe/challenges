while True:
    try:
        a = int(input())
        l = []
        for b in range(a):
            r = float(input())
            l.append(r)

        print(min(l))
    except:
        break