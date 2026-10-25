def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    r = []
    for x in matrix:
        r.append([y * scalar for y in x])
    return r