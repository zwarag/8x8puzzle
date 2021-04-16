import numpy as np
from manhatten import calculateManhattenDistance
from disposition import calculateDisposition


def buildPositionMatrix(matrix):
    posMatrix = np.empty(nn, dtype=int)
    posMatrix[matrix.reshape(nn)] = np.arange(nn)
    return posMatrix


def findZero(matrix):
    flatMatrix = matrix.reshape(nn)
    # 1. find the zero
    zeroPosition = np.where(flatMatrix == 0)[0][0]
    zeroPosition = [0, zeroPosition]
    while zeroPosition[1] > n-1:
        zeroPosition[1] = zeroPosition[1] - n
        zeroPosition[0] += 1
    return tuple(zeroPosition)


def swapPlaces(matrix, zero, elem):
    matrix[zero[0]][zero[1]] = matrix[elem[0]][elem[1]]
    matrix[elem[0]][elem[1]] = 0
    return matrix


def permuatePlayableMoves(matrix):
    solutions = []
    # 1. find the zero
    zeroPosition = findZero(matrix)
    # 2. swap with a neighbour
    # Right
    if(zeroPosition[1] < n-1):
        solutions.append(swapPlaces(np.copy(matrix), zeroPosition,
                         tuple([zeroPosition[0], zeroPosition[1]+1])))
    # Above
    if(zeroPosition[0] > 0):
        solutions.append(swapPlaces(np.copy(matrix), zeroPosition,
                         tuple([zeroPosition[0]-1, zeroPosition[1]])))
    # Left
    if(zeroPosition[1] > 0):
        solutions.append(swapPlaces(np.copy(matrix), zeroPosition,
                         tuple([zeroPosition[0], zeroPosition[1]-1])))
    # Below
    if(zeroPosition[0] < n-1):
        solutions.append(swapPlaces(np.copy(matrix), zeroPosition,
                         tuple([zeroPosition[0]+1, zeroPosition[1]])))
    return solutions


initial_state = np.array([[7, 2, 4], [5, 3, 6], [8, 1, 0]])

goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

if(initial_state.shape != goal_state.shape):
    print("initial and goal shape must be equal")
    exit(1)

# TODO: assert that all numers between 0-9 exist in both matrixes

n = 3
nn = 9

initPos = buildPositionMatrix(initial_state)
goalPos = buildPositionMatrix(goal_state)
distance = calculateManhattenDistance(initPos, goalPos)  # heuristic 1

solutions = permuatePlayableMoves(initial_state)
disposition = calculateDisposition(initial_state, goal_state)

print(disposition)
