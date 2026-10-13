def transpose(matrix):
    """Return the transpose of a rectangular matrix.

    C++ typically uses nested loops and push_back. Python expresses the same
    traversal with nested list comprehensions. These are concise and can avoid
    explicit append calls; a speed claim requires a benchmark.
    """
    if not matrix:
        return []

    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]
