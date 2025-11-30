from hmmlearn import hmm
import numpy as np
import pandas as pd
def input_file(file):


    open_file = open(file, 'r')
    lines = [items.strip() for items in open_file.readlines()]
    dna_strand = ''.join(lines)
    return dna_strand
# Number of states (eight as per requirement)
n_states = 8
# Number of possible emissions (nucleotides A, T, C, G)
n_observations = 4  # Assume A, T, C, G are encoded as 0, 1, 2, 3

model = hmm.CategoricalHMM(n_components=8,  n_iter=100, tol=1e-4, random_state=42, init_params='')
model.startprob_ = np.full(n_states, 1 / n_states)  # Initial state probabilities
model.transmat_ = np.full((n_states, n_states), 1 / n_states)  # Transition probabilities
model.emissionprob_ = np.random.dirichlet(np.ones(n_observations), n_states)  # Emission probabilities

# Define the nucleotide encoding
nucleotide_map = {'A': 0, 'T': 1, 'C': 2, 'G': 3}

dna_strand = input_file('rosalind_orf.txt')
# Encode the sequence
encoded_sequence = np.array([nucleotide_map[nuc] for nuc in dna_strand]).reshape(-1, 1)

model.fit(encoded_sequence, len(encoded_sequence))

state_names = {0: "A", 1: "T", 2: "C", 3: "G", 4: "A+", 5: "T+", 6: "C+", 7: "G+"}

# Convert the transition matrix to a DataFrame for easy viewing with named rows/columns
transition_df = pd.DataFrame(model.transmat_, index=[state_names[i] for i in range(n_states)],
                             columns=[state_names[i] for i in range(n_states)])
print("Transition matrix with nucleotide names:\n", transition_df)

# Convert the emission matrix to a DataFrame for easy viewing
emission_df = pd.DataFrame(model.emissionprob_, index=[state_names[i] for i in range(n_states)],
                           columns=["A", "T", "C", "G"])
print("Emission matrix with nucleotide names:\n", emission_df)