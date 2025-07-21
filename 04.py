def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return []

    if mode == 'row':
        means = [sum(row) / len(row) for row in matrix]
    elif mode == 'column':
        num_cols = len(matrix[0])
        if any(len(row) != num_cols for row in matrix):
            return []
        means = [sum(matrix[i][j] for i in range(len(matrix))) / len(matrix) for j in range(num_cols)]
    else:
        return []

    return means
