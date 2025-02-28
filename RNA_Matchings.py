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
              self.label = label
              self.adjacent = []
              self.basepair = []

    def __init__(self, string):
        self.string = string
        self.graph = []
    def AdjacentEdges(self, string):
    #self.graph dict will have keys as nodes and value as edges

        for i in range(len(string)+1):
            cur = self.node(string[i])
            if i == 0:
                cur.adjacent.append(string[i+1])
            else:
                cur.adjacent.append(string[i+1])
                cur.adjacent.append(string[i-1])

        return self.graph
    def BasepairEdges(self, string):

        bs_pair = { 'A': 'U', 'G': 'C', 'C':'G', 'U': 'A'}

        for base in self.graph:


