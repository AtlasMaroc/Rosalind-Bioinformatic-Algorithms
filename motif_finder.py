# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Use Biopython to parse sequence and factorial makes this problem straightforward ( O(n) ).

from Bio import SeqIO
from math import factorial

with open("rosalind_pmch (1).txt", "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        rna = str(record.seq)
print(factorial(rna.count('A'))*factorial(rna.count('C')))



