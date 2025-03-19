"""
this algorithm is used to find the perfect matching for a given RNA string
"""
import timeit
from math import factorial
class Graph:
    #object node with the label and the corresponding edges
    class node(object):
          def __init__(self, label):
              self.label = label
              self.adjacent = []
              self.basepair = set()
    def __init__(self, string):
        self.string = string
        self.graph = self.create_nodes(string)
        self.AdjacentEdges(string)
        self.BasepairEdges(string)
    def create_nodes(self, string):
        return [self.node(char) for char in string]
    def AdjacentEdges(self, string):
    #self.graph list will have nodes linked to edges

        for i,node in enumerate(self.graph):

            if i > 0:
                node.adjacent.append(self.graph[i-1])
            if i < len(string)-1:
                node.adjacent.append(self.graph[i+1])

    def BasepairEdges(self, string):

        bs_pair = { 'A': 'U', 'G': 'C', 'C':'G', 'U': 'A'}
        #iterate over node object in the self.graph list
        for i, base in enumerate(self.graph):
            #iterate over the string i to check for any base pair matching
            #if base pair matching is found create an basepair edge

            for index in range(i+1, len(string)):
                if bs_pair[base.label] == string[index]:
                    base.basepair.add(index)

    def perfect_matching(self):

            AU_count = 0
            GC_count = 0
            au_found = False
            gc_found = False

            for node in self.graph:
                if not au_found and node.label in ('A', 'U'):
                    AU_count += len(node.basepair)
                    au_found = True  # Stop counting after first A/U
                elif not gc_found and node.label in ('G', 'C'):
                    GC_count += len(node.basepair)
                    gc_found = True  # Stop counting after first G/C

                # Early exit if both found
                if au_found and gc_found:
                    break

            return factorial(GC_count)*factorial(AU_count)



def main(value):

     inst_graph = Graph(value)
     inst_graph.AdjacentEdges(value)
     inst_graph.BasepairEdges(value)
     num_poss = inst_graph.perfect_matching()
     print(num_poss)
     print(timeit.timeit())

main('AAAGCCUGCAGGGGGUCCUUGUCGCCUAAGCCUUCAAUACAAUGAGUGGCCCGUAAGUACCAUGUUCUGA')