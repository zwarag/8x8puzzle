import numpy as np
from tree import Node


def buildPositionMatrix(matrix):
    n, m = np.shape(matrix)
    nn = n*n
    posMatrix = np.empty(nn, dtype=int)
    posMatrix[matrix.reshape(nn)] = np.arange(nn)
    return posMatrix


def printTree(node: Node) -> str:
    s = ""
    for d in range(node.depth):
        s += "\t"
    print(f"{s}{node.name}({node.cost})")
    for child in node.childs:
        if child is not None:
            printTree(child)
