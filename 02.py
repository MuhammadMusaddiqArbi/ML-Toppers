def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    b = [list(row) for row in zip(*a)]
    return b
