import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        arr = np.array([y for x in a for y in x])
        return arr.reshape(new_shape)
    except:
        return []


print(reshape_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], (1, 4)))