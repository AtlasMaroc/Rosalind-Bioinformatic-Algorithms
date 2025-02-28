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
    #self.graph list will have nodes linked to edges

        for i in range(len(string)):
            cur = self.node(string[i])
            self.graph.append(cur)
            if i == 0:
                cur.adjacent.append(string[i+1])
            else:
                cur.adjacent.append(string[i+1])
                cur.adjacent.append(string[i-1])


    def BasepairEdges(self, string):

        bs_pair = { 'A': 'U', 'G': 'C', 'C':'G', 'U': 'A'}
        #iterate over node object in the self.graph list
        for base in self.graph:
            #iterate over the string i to check for any base pair matching
            #if base pair matching is found create an basepair edge

            for i in range(len(string)):
                if bs_pair[base.label] == string[i]:
                    base.basepair.append(i)






