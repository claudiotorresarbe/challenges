def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    if mode == 'column':
        t1 = len(matrix[0])
        t2 = len(matrix)
        r = [0] * t1
        for x in matrix:
            for y in range(t1):
                calc = r[y] + x[y]
                r[y] = calc
        return [x / t2 for x in r]
    else:
        t1 = len(matrix[0])
        r = []
        for x in matrix:
            r.append(sum(x))
    return [x / t1 for x in r]



print(calculate_matrix_mean([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 'row'))
# [4.0, 5.0, 6.0]