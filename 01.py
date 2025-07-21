def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    if not a or not b:
        return -1
    num_cols = len(a[0])
    if any(len(row) != num_cols for row in a) or num_cols != len(b):
        return -1
    result = []
    for row in a:
        dot_product = sum(x * y for x, y in zip(row, b))n
        result.append(dot_product)
    return result
