x = int(input())

while True:
    z = int(input())

    if z <= x:
        pass
    else:

        a = x
        lst = [a]

        while True:
            a += 1
            lst.append(a)
            if sum(lst) >= z:
                print(len(lst))
                break
        break