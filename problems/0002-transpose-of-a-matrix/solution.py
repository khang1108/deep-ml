def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    n, m = len(a) , len(a[0])
    b = []

    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(a[j][i])
        b.append(new_row)
    return b
