class Graph:
    class node(object):
          def __init__(self, label):
              self.lab = label
              self.adjacent = {}
              self.basepair = {}

    def __init__(self, string):
        self.string = string

        for s in string:
