# 15. Write a function that takes a list of lists of numbers, representing a square matrix
# and returns a list containing the elements of the main diagonal sorted in descending order.

def sorted_main_diagonal(matrix: list):
    """
    :param matrix: list of lists of numbers representing a square matrix
    :return: a list containing the elements of the main diagonal sorted in descending order
    """
    size = len(matrix)

    if size == 0:
        return []

    for row in matrix:
        if len(row) != size:
            raise ValueError("The matrix must be square.")

    diagonal = []

    for i in range(size):
        diagonal.append(matrix[i][i])

    return sorted(diagonal, reverse=True)


example_matrix = [
    [5, 12, 8, 3],
    [7, 19, 4, 2],
    [6, 1, 33, 9],
    [10, 15, 14, 27]
]

print("\n Exercise 15:", sorted_main_diagonal(example_matrix))