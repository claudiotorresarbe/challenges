def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

    if len(b) != len(a):
        return -1

    r = []
    for x in a:
        calc = 0
        for y in b:
            i = b.index(y)
            calc += x[i] * y
        r.append(calc)
    return r

#Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; 
#Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10
# resposta [5, 10]