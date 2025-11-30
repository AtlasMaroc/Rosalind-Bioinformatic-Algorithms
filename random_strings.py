import numpy as np 
from collections import Counter

class String:
    def __init__(self, s, A):
        self.s = s
        self.A = np.array(A)
        self.count = dict(Counter(self.s))
        self.B = self.array_B()
    
    def array_B(self) -> np.ndarray:
        
        B = []
        for i in self.A: 
            probability = (self.count['A'] + self.count['T']) * np.log10((1-i)/2) + np.log10((i)/2) * (self.count['C']+self.count['G'])
            B.append(probability)
        return np.array(B)