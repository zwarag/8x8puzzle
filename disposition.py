import numpy as np


def calculateDisposition(matrix1, matrix2):
    """returns a how many elements in matrix1 are at the same place in matrix2"""
    n, m = matrix1.shape
    flatMatrix1 = matrix1.reshape(n*m)
    flatMatrix2 = matrix2.reshape(n*m)
    return np.sum(flatMatrix1 == flatMatrix2)
