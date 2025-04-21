import re as re

def input_file(file):

    read_file = open(file, 'r')
    line_strip = [items.strip() for items in read_file.readlines()]
    return line_strip

def sequence(line_strip):

    dna_strand = ''

    for line in line_strip:
        match = re.match(r"^>(Rosalind_[0-9]{4})$", line)
        if match:
            continue
        else:
            dna_strand += line

    return dna_strand

def reverse(dna_strand):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_complement = ''.join(complement[base] for base in reversed(dna_strand))
    return reversed_complement
def dna_to_rna(dna_strand, reverse):
    rna_seq = []

    codon = {'A':'A', 'T':'U', 'G':'G', 'C':'C'}
    for x in range(0,3):
        seq = ''
        for i in range(x, len(dna_strand)):
            tri = dna_strand[i]
            trans = codon[tri]
            seq += trans
        rna_seq.append(seq)
    for x in range(0, 3):
        seq = ''
        for i in range(x, len(reverse)):
            tri = reverse[i]
            trans = codon[tri]
            seq += trans
        rna_seq.append(seq)
    return rna_seq
def orf(rna_seq):

    orf = []
    codon_to_amino_acid = {
        'UUU': 'F', 'UUC': 'F',  # Phenylalanine
        'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',  # Leucine
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',  # Isoleucine
        'AUG': 'M',  # Methionine (Start codon)
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',  # Valine
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',  # Serine
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
        'UAU': 'Y', 'UAC': 'Y',  # Tyrosine
        'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop',  # Stop codons
        'CAU': 'H', 'CAC': 'H',  # Histidine
        'CAA': 'Q', 'CAG': 'Q',  # Glutamine
        'AAU': 'N', 'AAC': 'N',  # Asparagine
        'AAA': 'K', 'AAG': 'K',  # Lysine
        'GAU': 'D', 'GAC': 'D',  # Aspartic Acid
        'GAA': 'E', 'GAG': 'E',  # Glutamic Acid
        'UGU': 'C', 'UGC': 'C',  # Cysteine
        'UGG': 'W',  # Tryptophan
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',  # Arginine
        'AGU': 'S', 'AGC': 'S',  # Serine
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',  # Glycine
    }


    for temp_seq in rna_seq:  # Iterate over each RNA sequence
      for start in range(0,len(temp_seq)-2, 3):
        codon = temp_seq[start:start + 3]
        if codon == 'AUG':  # Found a start codon
            aa_seq = ''  # Temporary sequence for current ORF
            for i in range(start, len(temp_seq) - 2, 3):
                codon = temp_seq[i:i + 3]
                amino_acid = codon_to_amino_acid[codon]

                if amino_acid == 'Stop':
                    break
                elif amino_acid:
                    aa_seq += amino_acid

            # Append this ORF if a valid sequence was built

            orf.append(aa_seq)
    unique =  list(dict.fromkeys(orf))
    return unique
def main():
    load_file = input_file('rosalind_orf.txt')
    load_sequence = sequence(load_file)
    load_reverse = reverse(load_sequence)
    load_rna = dna_to_rna(load_sequence, load_reverse)
    load_orf = orf(load_rna)
    for seq in load_orf:
        print(seq)

main()






