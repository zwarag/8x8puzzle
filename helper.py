import numpy as np
import numpy.typing as npt


def findZero(matrix: npt.ArrayLike):
    n, m = matrix.shape
    flatMatrix = matrix.reshape(n*m)
    # 1. find the zero
    zeroPosition = np.where(flatMatrix == 0)[0][0]
    zeroPosition = [0, zeroPosition]
    while zeroPosition[1] > n-1:
        zeroPosition[1] = zeroPosition[1] - n
        zeroPosition[0] += 1
    return tuple(zeroPosition)


def buildPositionMatrix(matrix):
    n, m = np.shape(matrix)
    nn = n*n
    posMatrix = np.empty(nn, dtype=int)
    posMatrix[matrix.reshape(nn)] = np.arange(nn)
    return posMatrix


if __name__ == '__main__':
    arr1 = np.array([[7, 2, 4], [5, 3, 6], [8, 1, 0]])
    arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    arr3 = np.array([[4, 1, 2], [3, 0, 5], [6, 7, 8]])
    arr4 = np.array([[4, 1, 2], [3, 5, 0], [6, 7, 8]])
    print(findZero(arr1))
    print(findZero(arr2))
    print(findZero(arr3))
    print(findZero(arr4))
