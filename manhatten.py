import numpy as np
from helper import buildPositionMatrix


def calculateManhattenDistance(matrix1, matrix2):
    """
    Calculates the distance of the elements in the matrix.
    Only works for numbers. Make sure that any number occurs only once per matrix.
    """
    pos_matrix1 = buildPositionMatrix(matrix1)
    pos_matrix2 = buildPositionMatrix(matrix2)
    n = pos_matrix1.shape
    xInitPos, yInitPos = pos_matrix1 % n, pos_matrix1//n
    xGoalPos, yGoalPos = pos_matrix2 % n, pos_matrix2//n
    distancex = np.abs(xGoalPos-xInitPos)
    distancey = np.abs(yGoalPos-yInitPos)
    distance = distancex+distancey
    return np.sum(distance)


if __name__ == '__main__':
    initial_state = np.array([[7, 2, 4], [5, 3, 6], [8, 1, 0]])
    goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    sol = calculateManhattenDistance(initial_state, goal_state)
    assert sol == 30
