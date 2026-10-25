def two_to_three(a):
    r = []
    for x in range(3):
        rr = []
        for y in a:
            rr.append(y[x])
        r.append(rr)
    return r
    
def three_to_two(a):
    r = [[],[]]

    for x in range(2):
        for y in range(len(a)):
            r[x].insert(y,a[y][x])
    return r

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    t = len(a[0])
    if t == 3:
        return two_to_three(a)
    elif t == 2:
        return three_to_two(a)
    elif t == 1:
        return [x[0] for x in a]

