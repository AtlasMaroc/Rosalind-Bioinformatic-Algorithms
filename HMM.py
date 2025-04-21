import numpy as np
import pandas as pd

def input_file(file):
    open_file = open(file, 'r')
    read_file = [item.strip() for item in open_file.readlines()]
    strand = ''.join(read_file)
    return strand

def matrix(strand):
    null_matrix = np.zeros(shape=(4, len(strand)), dtype='int16')
    null_trans = pd.DataFrame(null_matrix, index=['A+', 'C+', 'G+', 'T+', 'A', 'C', 'G', 'T'])
    return null_trans
def forward(E, A, pi, observation): #E for emission matrix, A for transition matrix, pi for initial probability matrix, observation for different values Sigma
    L = len(observation)
    H = pi.shape(0)

    '''
    we will set the inital state
    '''
    alpha = np.zeros((H,L))

    alpha[0, :] = pi*E[observation[0], :]

    for i in range(1, L):
        for t in range(1, H):
            alpha[i, t] = observation[t]*sum(alpha[i-1,s]*A[s,t] for s in range(t))

    return np.sum(alpha[:, L-1])

E = {
    "A+": 0.3,  # Probability of methylated Adenine in CpG
    "A": 0.45,  # Probability of unmethylated Adenine in CpG
    "C+": 0.4,  # Probability of methylated Cytosine in CpG
    "C": 0.25,  # Probability of unmethylated Cytosine in CpG
    "G+": 0.35, # Probability of methylated Guanine in CpG
    "G": 0.3,   # Probability of unmethylated Guanine in CpG
    "T+": 0.2,  # Probability of methylated Thymine in CpG
    "T": 0.35   # Probability of unmethylated Thymine in CpG
}


