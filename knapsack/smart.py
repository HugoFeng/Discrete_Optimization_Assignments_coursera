from Queue import PriorityQueue
from collections import namedtuple
Node = namedtuple("Node", ['subItems', 'capacityLeft', 'valueTaken', 'taken', 'evaluation'])

from heapq import heappush, heappop, heapify

class MyPriorityQueue(object):
    def __init__(self, maxSize=0, descend=True):
        self._maxSize = maxSize
        self._list = []
        if descend:
            self._reverseSign = -1
        else:
            self._reverseSign = 1
    
    def push(self, priority, item):
        self._list.append((priority*self._reverseSign, item))
        heapify(self._list)
        if self._maxSize == 0:
            return
        elif len(self._list)>self._maxSize:
            del self._list[-1]
            
    def pop(self):
        tmp = self._list[0]
        del self._list[0]
        return tmp[1]
    def empty(self):
        return len(self._list)==0
    def size(self):
        return len(self._list)


def smartChoice(items, capacity):
    global toDo, solution
    #Change maxSize of toDo to change the range of searching space
    toDo = MyPriorityQueue(maxSize=2000)
    solution = MyPriorityQueue(maxSize=5)
    value = 0
    taken = [0]*len(items)
    items=sorted(items, key=lambda item:item.value*1.0/item.weight, reverse=True)
    startNode = Node(items[:], capacity, 0.0, taken[:], getEvaluation(items, capacity, 0.0))
    toDo.push(startNode.evaluation, startNode)
    while toDo.empty()!=True:
        bestFirstSearch(toDo.pop())
    if solution.empty():
        return (0, [0,0])
    else:
        best = solution.pop()
    return (int(best.valueTaken), best.taken)

def getEvaluation(subItems, capacityLeft, valueTaken):
    sumValue = valueTaken
    for item in subItems:
        if item.weight > capacityLeft:
            sumValue += capacityLeft*1.0/item.weight*item.value
            return sumValue
        else:
            capacityLeft -= item.weight
            sumValue += item.value
    return sumValue

def bestFirstSearch(node):
    global toDo, solution
    subItems, capacityLeft, valueTaken, taken = node.subItems, node.capacityLeft, node.valueTaken, node.taken
    if subItems  == []:
        solution.push(node.valueTaken, node)
    else:
        if subItems[0].weight <= capacityLeft:
            dontPick=getEvaluation(subItems[1:], capacityLeft, valueTaken)
            pick = getEvaluation(subItems[1:], capacityLeft-subItems[0].weight, valueTaken+subItems[0].value)
            
            toDo.push(dontPick, Node(subItems[1:], capacityLeft, valueTaken, taken[:], dontPick))
            taken[subItems[0].index] = 1
            toDo.push(pick, Node(subItems[1:], capacityLeft-subItems[0].weight, valueTaken+subItems[0].value, taken[:], pick))
        else:
            dontPick=getEvaluation(subItems[1:], capacityLeft, valueTaken)
            toDo.push(dontPick, Node(subItems[1:], capacityLeft, valueTaken, taken[:], dontPick))
