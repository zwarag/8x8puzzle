import heapq as heapq
from tree import Node
from typing import Callable, List


def a_star(start: Node, goal: Node, h: Callable):
    openSet = [start]
    closedSet: List[Node] = []
    heapq.heapify(openSet)

    while len(openSet) != 0:
        current: Node = heapq.heappop(openSet)
        closedSet.append(current)

        if current == goal:
            return current

        for neighbor in current.permuatePlayableMoves():
            if neighbor is None or neighbor in closedSet:
                continue

            neighbor.g = current.g + 1
            neighbor.h = h(neighbor.arr, goal.arr)
            if neighbor not in openSet and neighbor not in closedSet:
                heapq.heappush(openSet, neighbor)

    print("no solution found :(")
    exit()
