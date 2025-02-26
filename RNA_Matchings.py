"""
this algorithm is used to find the perfect matching for a given RNA string
"""

#something's I need to look up
#1: how to implement a graph in python
#2: how to design a recursive function
#3: perfect matching in a complete graph
#4: bonding graph, adjacency list
#5: define the variables I will be working with such as Kn and Pn
#6: undirected cyclic graph

class Graph:
    #object node with the label and the corresponding edges
    class node(object):
          def __init__(self, label):
              self.lab = label
              self.adjacent = {}
              self.basepair = {}

    def __init__(self, string):
        self.string = string

        for s in string:
