import numpy as np
import math

class PartialPermutation:
    def __init__(self, n, k):
        self.n = n
        self.k = k 
        self.permutations = PartialPermutation.perm(n, k)
        self.modulu = self.remainder()

    @staticmethod
    def perm(n, k):
        if k == 0:
            return 1
        return math.perm(n, k)
    
    def remainder(self):
        return self.permutations % 1000000
    
    def __repr__(self):
        return f"PartialPermutation({self.n}, {self.k}, {self.permutations}, {self.modulu})"

test = PartialPermutation(94, 10)
test