#!/usr/bin/python3
"""Multiplying two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiples two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        new_matrix: The new product matrix.

    Raises:
        TypeError: An error occurred accessing the variable type.
        ValueError: An error occurred accessing the variable value.
    """

    stmts = {
        "err_list": "must be a list",
        "err_matrix": "must be a list of lists",
        "err_type": "should contain only integers or floats",
        "war_empty": "can't be empty",
        "war_multi": "m_a and m_b can't be multiplied",
        "stmt_row": "each row of",
        "stmt_size": "must should be of the same size",
    }

    if type(m_a) is not list:
        raise TypeError("m_a " + stmts["err_list"])

    if type(m_b) is not list:
        raise TypeError("m_b " + stmts["err_list"])

    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a " + stmts["err_matrix"])

    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b " + stmts["err_matrix"])

    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a " + stmts["war_empty"])

    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b " + stmts["war_empty"])

    for row in m_a:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a " + stmts["err_type"])

    for row in m_b:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b " + stmts["err_type"])

    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError(stmts["stmt_row"] + " m_a " + stmts["stmt_size"])

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError(stmts["stmt_row"] + " m_b " + stmts["stmt_size"])

    if len(m_a[0]) != len(m_b):
        raise ValueError(stmts["war_multi"])

    new_matrix = []
    for arr in m_a:
        new_arr = []
        for i in range(len(m_b[0])):
            new_arr.append(
                sum(a * b for a, b in zip(arr, list(r[i] for r in m_b))))
        new_matrix.append(new_arr)

    return new_matrix
