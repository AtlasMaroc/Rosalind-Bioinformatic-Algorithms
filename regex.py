import re

def input_file(file):

    open_file = open(file, 'r')
    lines = [items.strip() for items in open_file.readlines()]
    return lines

def dictionnary(lines):

    id_seq = {}
    dna_strand = ""
    current_id= None

    for line in lines:
        match = re.match(r"^>(Rosalind_[0-9]{4})$", line)
        if match:
            if current_id:
                id_seq[current_id] = dna_strand
                dna_strand = ""

            current_id = match.group(1)
        else:
            dna_strand += line
    if current_id:
        id_seq[current_id] = dna_strand
    return id_seq

def adjacent_matrix(id_seq, k):

    id_seq1 = id_seq
    adjacent_strand = { key: [] for key in id_seq1}

    id_list = list(adjacent_strand.keys())

    for i in range(0, len(id_list)):
        for j in  range(i+1, len(id_list)):
            seq_id1 = id_list[i]
            seq_id2 = id_list[j]
            seq_1 = id_seq1[seq_id1]
            seq_2 = id_seq1[seq_id2]

            if(seq_1[-k:] == seq_2[:k]):
               adjacent_strand[seq_id1].append(seq_id2)
            if seq_1[:k] == seq_2[-k:]:
              adjacent_strand[seq_id2].append(seq_id1)

    return adjacent_strand

def main():
    file_name = 'rosalind_grph (10).txt'  # replace with your file name
    k = 3  # replace with your k value

    lines = input_file(file_name)
    id_seq = dictionnary(lines)
    adjacent_strand = adjacent_matrix(id_seq, k)

    for key, value in adjacent_strand.items():
        for pair in value:
            print(f"{key} {pair}")

main()