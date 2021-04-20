import numpy as np
import numpy.typing as npt


def calculateDispositionSum(matrix1: np.ndarray, matrix2: np.ndarray) -> int:
    """returns a how many elements in matrix1 are at the same place in matrix2"""
    n, m = matrix1.shape
    flatMatrix1 = matrix1.reshape(n*m)
    flatMatrix2 = matrix2.reshape(n*m)
    return 9 - np.sum(flatMatrix1 == flatMatrix2)


def calculateDisposition(matrix1: np.ndarray, matrix2: np.ndarray) -> bool:
    """returns a the difference in matrix1 are at the same place in matrix2"""
    n, m = matrix1.shape
    flatMatrix1 = matrix1.reshape(n*m)
    flatMatrix2 = matrix2.reshape(n*m)
    return (flatMatrix1 == flatMatrix2).all()


if __name__ == '__main__':
    goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    sol = calculateDispositionSum(goal_state, goal_state)
    assert sol == 0
    initial_state = np.array([[7, 2, 4], [5, 3, 6], [8, 1, 0]])
    sol = calculateDispositionSum(initial_state, goal_state)
    assert sol == 9
    sol = calculateDispositionSum(goal_state, initial_state)
    assert sol == 9
