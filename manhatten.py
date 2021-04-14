import numpy as np


def calculateManhattenDistance(matrix1, matrix2):
    """
    Calculates the distance of the elements in the matrix.
    Only works for numbers. Make sure that any number occurs only once per matrix.
    """
    n = matrix1.shape
    xInitPos, yInitPos = matrix1 % n, matrix1//n
    xGoalPos, yGoalPos = matrix2 % n, matrix2//n
    distancex = np.abs(xGoalPos-xInitPos)
    distancey = np.abs(yGoalPos-yInitPos)
    distance = distancex+distancey
    return distance
