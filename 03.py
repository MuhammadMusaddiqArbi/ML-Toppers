import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    total_elements = sum(len(row) for row in a)
    if total_elements != new_shape[0] * new_shape[1]:
        return []
    reshaped_matrix = np.array(a).reshape(new_shape).tolist()
    return reshaped_matrix
