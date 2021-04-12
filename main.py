from typing import List

initial_state = [[7, 2, 4], [5, None, 6], [8, 3, 1]]
goal_state = [[None, 1, 2], [3, 4, 5], [6, 7, 8]]


def distance_to_goal(init: List[List[int]], goal: List[List[int]]):
    rows = len(init)
    columns = len(init[0])

    distances = [[[0] for i in range(rows)]
                 for j in range(columns)]
    # distances = np.zeros((3, 3), dtype=np.int64)

    for i, array in enumerate(init):
        for j, number in enumerate(array):
            (row, column) = find_index(x=number, goal=goal)
            distances[i][j] = abs(i - row) + abs(j - column)
    return distances


def find_index(x: int, goal: List[List[int]]):
    for row, i in enumerate(goal):
        try:
            column = i.index(x)
        except ValueError:
            continue
        return row, column
    return -1


distances1 = distance_to_goal(init=initial_state, goal=goal_state)
print("Distance:")
for distance in distances1:
    print(distance)

print("Init:")
for row in initial_state:
    print(row)

print("Goal:")
for row in goal_state:
    print(row)
