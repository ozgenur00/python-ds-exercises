def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    nrows = len(matrix)
    if not nrows or not all(len(row) == nrows for row in matrix):
        raise ValueError("Input must be square")
    # Top left to bottom right diagonal (TL-to-BR)
    tltr = sum(matrix[i][nrows - i - 1] for i in range(nrows))
    # Bottom left to top right diagonal (BL-to-TR)
    bltr = sum(matrix[i][i] for i in range(nrows))
    return tltr + bltr

