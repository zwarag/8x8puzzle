import numpy as np
from manhatten import calculateManhattenDistance
from disposition import calculateDispositionSum
from tree import Node
import helper
from a_star import a_star


initial_state = np.array([[7, 2, 4], [5, 0, 6], [8, 3, 1]])

goal_state = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

if(initial_state.shape != goal_state.shape):
    print("initial and goal shape must be equal")
    exit(1)

# TODO: assert that all numers between 0-9 exist in both matrixes

n = 3
nn = 9
root = Node(
    arr=initial_state,
    name="root",
    h=0,
    g=0,
    parent=None
)
goal = Node(
    arr=goal_state,
    name="goal",
    h=0,
    g=0,
)

solution = a_star(root, goal, calculateManhattenDistance)
print("found solution :)", solution.name, solution.g)
