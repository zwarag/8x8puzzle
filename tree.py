# https://stackoverflow.com/questions/65909225/recursive-class-typing-in-python
from __future__ import annotations
from typing import Union
from dataclasses import dataclass
import numpy as np
import numpy.typing as npt


@dataclass
class Node():
    """
    A Node can have up to 4 Children.
    Children: "Right", "Above", "Left", "Below"
    """
    value: int = 0
    parent: Node = None
    childs = np.empty(4, dtype=object)

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


if __name__ == '__main__':
    # Only for testing purposes
    p = Node(value=0)
    right = Node(value=1, parent=p)
    above = Node(value=2, parent=p)
    left = Node(value=3, parent=p)
    below = Node(value=4, parent=p)
    p.childs[0] = right
    p.childs[1] = above
    p.childs[2] = left
    p.childs[3] = below
    assert p.childs[0].parent.value == p.value
    assert p.childs[1].parent.value == p.value
    assert p.childs[2].parent.value == p.value
    assert p.childs[3].parent.value == p.value
    assert p.childs[0] == right
    assert p.childs[1] == above
    assert p.childs[2] == left
    assert p.childs[3] == below
    p.value += 1
    assert p.childs[0].parent.value == 1
    assert p.childs[1].parent.value == 1
    assert p.childs[2].parent.value == 1
    assert p.childs[3].parent.value == 1
    p.childs[0].value += 1
    p.childs[1].value += 1
    p.childs[2].value += 1
    p.childs[3].value += 1
    right.value = 2
    above.value = 3
    left.value = 4
    below.value = 5
    assert p.right().value == p.childs[0].value
    assert p.above().value == p.childs[1].value
    assert p.left().value == p.childs[2].value
    assert p.below().value == p.childs[3].value
    neighbours = p.getChildren()
    assert neighbours[0].value == p.right().value
    assert neighbours[1].value == p.above().value
    assert neighbours[2].value == p.left().value
    assert neighbours[3].value == p.below().value
