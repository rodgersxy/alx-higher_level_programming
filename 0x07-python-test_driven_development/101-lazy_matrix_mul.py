#!/usr/bin/python3
"""function that multiplies 2 matrices by using the module NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    Args:
        m_a (list of lists): The first matrix to multiply
        m_b (list of lists): The second matrix to multiply
    Returns:
        A new matrix that is the result of multiplying m_a and m_b
    Raises:
        ValueError: If m_a and m_b cannot be multiplied
    """

    a_np = np.array(m_a)
    b_np = np.array(m_b)
    if a_np.shape[1] != b_np.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(a_np, b_np).tolist()
