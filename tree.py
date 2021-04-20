# https://stackoverflow.com/questions/65909225/recursive-class-typing-in-python
from __future__ import annotations
import numpy.typing as npt
import numpy as np
import numpy.typing as npt
from typing import Union, Any, List, Optional
from dataclasses import dataclass
from disposition import calculateDispositionSum, calculateDisposition
from helper import findZero


class Node():
    def __init__(self, arr: np.ndarray = None, name: str = None, h: int = None, g: int = None, parent: Node = None):
        """Can have up to 4 Children.

        Args:
            arr (np.ndarray, optional): The actual array. Defaults to None.
            name (str, optional): A name which describes the node. Defaults to None.
            h (int, optional): The cost to reach this node. Defaults to None.
            g (int, optional): How many steps levels to reach this node. Defaults to None.
            parent (Node, optional): The parent node. Defaults to None.
        """
        self.arr = arr if arr is not None else None
        self.name = name if name is not None else "root"
        self.h = h if h is not None else float('inf')
        self.g = g if g is not None else 0
        self.parent = parent if parent is not None else None
        self.childs = np.empty(4, dtype=object)

    def f(self) -> float:
        return self.h + self.g

    def right(self) -> Node:
        assert isinstance(self.childs[0], Node)
        return self.childs[0]

    def above(self) -> Node:
        assert isinstance(self.childs[1], Node)
        return self.childs[1]

    def left(self) -> Node:
        assert isinstance(self.childs[2], Node)
        return self.childs[2]

    def below(self) -> Node:
        assert isinstance(self.childs[3], Node)
        return self.childs[3]

    def getChildren(self) -> np.ndarray:
        return np.array((self.right(), self.above(), self.left(), self.below()))

    def moveAlreadyInParent(self, candiate: np.ndarray) -> bool:
        assert isinstance(self.arr, np.ndarray)
        return calculateDispositionSum(self.arr, candiate) == 0

    def swapPlaces(self, matrix, zero, elem):
        matrix[zero[0]][zero[1]] = matrix[elem[0]][elem[1]]
        matrix[elem[0]][elem[1]] = 0
        return matrix

    def permuatePlayableMoves(self) -> List[Union[Node, None]]:
        assert isinstance(self.arr, np.ndarray)
        n = 3
        solutions: List[Union[None, Node]] = []
        # 1. find the zero
        zeroPosition = findZero(self.arr)
        # 2. swap with a neighbour
        # Right
        # Node(arr=None, name=None, cost=None, depth=None, parent=None)
        if(zeroPosition[1] < n-1):
            sol = self.swapPlaces(np.copy(self.arr), zeroPosition,
                                  tuple([zeroPosition[0], zeroPosition[1]+1]))
            if not self.moveAlreadyInParent(sol):
                solutions.append(
                    Node(
                        name=self.name + ':right',
                        arr=sol,
                        parent=self
                    )
                )
        else:
            solutions.append(None)

        # Above
        if(zeroPosition[0] > 0):
            sol = self.swapPlaces(np.copy(self.arr), zeroPosition,
                                  tuple([zeroPosition[0]-1, zeroPosition[1]]))
            if not self.moveAlreadyInParent(sol):
                solutions.append(
                    Node(
                        name=self.name + ':up',
                        arr=sol,
                        parent=self
                    )
                )
        else:
            solutions.append(None)

        # Left
        if(zeroPosition[1] > 0):
            sol = self.swapPlaces(np.copy(self.arr), zeroPosition,
                                  tuple([zeroPosition[0], zeroPosition[1]-1]))
            if not self.moveAlreadyInParent(sol):
                solutions.append(
                    Node(
                        name=self.name + ':left',
                        arr=sol,
                        parent=self
                    )
                )
        else:
            solutions.append(None)

        # Below
        if(zeroPosition[0] < n-1):
            sol = self.swapPlaces(np.copy(self.arr), zeroPosition,
                                  tuple([zeroPosition[0]+1, zeroPosition[1]]))
            if not self.moveAlreadyInParent(sol):
                solutions.append(
                    Node(
                        name=self.name + ':down',
                        arr=sol,
                        parent=self
                    )
                )
        else:
            solutions.append(None)

        return solutions

    def __lt__(self, other):
        return self.h < other.h

    def __eq__(self, other):
        return calculateDisposition(self.arr, other.arr)

    # def printTree(self) -> str:
    #    s = ""
    #    for d in range(node.depth):
    #        s += "\t"
    #    print(f"{s}{node.name}({node.cost})")
    #    for child in node.childs:
    #        if child is not None:
    #            printTree(child)


if __name__ == '__main__':
    # Only for testing purposes
    arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    arr3 = np.array([[1, 0, 2], [3, 4, 5], [6, 7, 8]])
    n1 = Node(arr=arr1, name="n1", h=0)
    n2 = Node(arr=arr2, name="n2", h=3)
    n3 = Node(arr=arr3, name="n3", h=4)
    assert n1 == n1
    assert n1 == n2
    assert n1 != n3
    assert n2 != n3
    p = Node(h=0)
    right = Node(h=1, parent=p)
    above = Node(h=2, parent=p)
    left = Node(h=3, parent=p)
    below = Node(h=4, parent=p)
    p.childs[0] = right
    p.childs[1] = above
    p.childs[2] = left
    p.childs[3] = below
    assert p.childs[0].parent.cost == p.h
    assert p.childs[1].parent.cost == p.h
    assert p.childs[2].parent.cost == p.h
    assert p.childs[3].parent.cost == p.h
    p.h += 1
    assert p.childs[0].parent.cost == 1
    assert p.childs[1].parent.cost == 1
    assert p.childs[2].parent.cost == 1
    assert p.childs[3].parent.cost == 1
    p.childs[0].cost += 1
    p.childs[1].cost += 1
    p.childs[2].cost += 1
    p.childs[3].cost += 1
    right.h = 2
    above.h = 3
    left.h = 4
    below.h = 5
    assert p.right().cost == p.childs[0].cost
    assert p.above().cost == p.childs[1].cost
    assert p.left().cost == p.childs[2].cost
    assert p.below().cost == p.childs[3].cost
    neighbours = p.getChildren()
    assert neighbours[0].cost == p.right().cost
    assert neighbours[1].cost == p.above().cost
    assert neighbours[2].cost == p.left().cost
    assert neighbours[3].cost == p.below().cost
