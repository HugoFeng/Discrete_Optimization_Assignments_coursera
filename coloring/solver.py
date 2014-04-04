#!/usr/bin/python
# -*- coding: utf-8 -*-

import color

class Node(object):
    def __init__(self):
        self.color = -1
        self.toNode = []
    def edgeNum(self):
        return len(self.toNode)

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    nodes = {i:Node() for i in range(node_count)}

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    #Build graph
    for e in edges:
        nodeA, nodeB = e 
        nodes[nodeA].toNode.append(nodeB)
        nodes[nodeB].toNode.append(nodeA)
    
    #for index in range(node_count):
    #    print 'Node', index, ': ', nodes[index].toNode 
    

    # build a trivial solution
    # every node has its own color
    #solution = range(0, node_count)

    #My solution:
    solution , colorNum= color.color(nodes)

    # prepare the solution in the specified output format
    output_data = str(colorNum) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

