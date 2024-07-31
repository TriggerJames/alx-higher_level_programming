#!/usr/bin/python3
"""
Module that does matrix multiplication
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list, or not a list of lists, or if
                   elements are not integers or floats, or if rows of the
                   matrices are not of the same size.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be
                    multiplied due to dimension mismatch.
    """

    # Check if both m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if both m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if both m_a and m_b are non-empty
    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    # Check that all elements in m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check that all rows in m_a and m_b are of the same size
    row_size_a = len(m_a[0])
    if any(len(row) != row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_size_b = len(m_b[0])
    if any(len(row) != row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if row_size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(row_size_a):
                sum += m_a[i][k] * m_b[k][j]
            result_row.append(sum)
        result.append(result_row)

    return result
