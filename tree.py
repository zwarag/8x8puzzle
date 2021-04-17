# https://stackoverflow.com/questions/65909225/recursive-class-typing-in-python
from __future__ import annotations
import numpy.typing as npt
import numpy as np
from typing import Union, Any
from dataclasses import dataclass
from disposition import calculateDisposition


class Node():
    """
    A Node can have up to 4 Children.
    Children: "Right", "Above", "Left", "Below"
    """
    arr: np.ndarray
    name: str
    cost: int
    depth: int
    parent: Node
    childs: np.ndarray

    def __init__(self, arr: np.ndarray = None, name: str = None, cost: int = None, depth: int = None, parent: Node = None):
        self.arr = arr if arr is not None else None
        self.name = name if name is not None else "root"
        self.cost = cost if cost is not None else 0
        self.depth = depth if depth is not None else 0
        self.parent = parent if parent is not None else None
        self.childs = np.empty(4, dtype=object)

    def right(self) -> Union[Node, None]:
        return self.childs[0]

    def above(self) -> Union[Node, None]:
        return self.childs[1]

    def left(self) -> Union[Node, None]:
        return self.childs[2]

    def below(self) -> Union[Node, None]:
        return self.childs[3]

    def getChildren(self) -> ntp.array:
        return np.array((self.right(), self.above(), self.left(), self.below()))

    def moveAlreadyInParent(self, parent_arr, candiate) -> bool:
        return calculateDisposition(parent_arr, candiate) != 0

    def setChildren(self, parent, possible_moves, costFunction, goal_state) -> None:
        for i, elem in enumerate(possible_moves):
            self.childs[i] = Node(
                name=parent.name + f":{i}",
                parent=parent,
                depth=parent.depth+1,
                arr=possible_moves[i],
                cost=costFunction(possible_moves[i], goal_state)
            ) if possible_moves[i] is not None and self.moveAlreadyInParent(parent.arr, possible_moves[i]) else None


if __name__ == '__main__':
    # Only for testing purposes
    p = Node(cost=0)
    right = Node(cost=1, parent=p)
    above = Node(cost=2, parent=p)
    left = Node(cost=3, parent=p)
    below = Node(cost=4, parent=p)
    p.childs[0] = right
    p.childs[1] = above
    p.childs[2] = left
    p.childs[3] = below
    assert p.childs[0].parent.cost == p.cost
    assert p.childs[1].parent.cost == p.cost
    assert p.childs[2].parent.cost == p.cost
    assert p.childs[3].parent.cost == p.cost
    assert p.childs[0] == right
    assert p.childs[1] == above
    assert p.childs[2] == left
    assert p.childs[3] == below
    p.cost += 1
    assert p.childs[0].parent.cost == 1
    assert p.childs[1].parent.cost == 1
    assert p.childs[2].parent.cost == 1
    assert p.childs[3].parent.cost == 1
    p.childs[0].cost += 1
    p.childs[1].cost += 1
    p.childs[2].cost += 1
    p.childs[3].cost += 1
    right.cost = 2
    above.cost = 3
    left.cost = 4
    below.cost = 5
    assert p.right().cost == p.childs[0].cost
    assert p.above().cost == p.childs[1].cost
    assert p.left().cost == p.childs[2].cost
    assert p.below().cost == p.childs[3].cost
    neighbours = p.getChildren()
    assert neighbours[0].cost == p.right().cost
    assert neighbours[1].cost == p.above().cost
    assert neighbours[2].cost == p.left().cost
    assert neighbours[3].cost == p.below().cost
