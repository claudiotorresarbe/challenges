def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    div = ((a * d) - (b * c))
    if div == 0:
        return None
    det = 1 / div

    aa = round(a*det,1)
    bb = round((b*-1)*det,1)
    cc = round((c*-1)*det,1)
    dd = round(d*det,1)
    r = [[dd, bb], [cc,aa]]
    return r

print(inverse_2x2([[4, 7], [2, 6]]))
print(inverse_2x2([[1, 2], [2, 4]]))