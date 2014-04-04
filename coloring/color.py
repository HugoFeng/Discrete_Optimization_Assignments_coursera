def color(nodes):
    return orderColoring(nodes)

def simpleSolver(nodes):
    return [i for i in range(len(nodes))]


def orderColoring(nodes):
    nodesIndexInOrder = sorted(nodes, key=lambda i: nodes[i].edgeNum())
    colorList = [0]
    for index in nodesIndexInOrder:
        node = nodes[index]
        for c in colorList:
            if canUseColor(nodes, node, c):
                node.color = c
                break
        if node.color == -1:
            colorList.append(len(colorList))
            node.color = colorList[-1]
    return ([nodes[i].color for i in nodes], len(colorList))


def canUseColor(nodes, n, c):
    for toNodeIndex in n.toNode:
        if nodes[toNodeIndex].color == c:
            return False
    return True

