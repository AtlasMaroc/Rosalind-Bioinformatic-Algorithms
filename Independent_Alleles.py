'''
the algorithm solution is for independent allele problem, it takes two input
an integer K <= 7 representing the number of generation, and N representing
the number of people with the genotype after k generation. the output is the
probability of N people having the genotype from a pool of 2^k.
'''



from scipy.stats import binom
class Allele:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.pr = 0.25
        self.N = 2 ** (k)


    def pro(self, n, k):
        res = 0
        for i in range(0, n):
            res += binom.pmf(i, self.N, 0.25)

        return print(1 - res)


inst = Allele(32,7)

inst.pro(32,7)
