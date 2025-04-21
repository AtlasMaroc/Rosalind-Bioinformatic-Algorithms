import re

def read_file(file, motif):
    index_list = []
    with open(file, "r", newline=None) as fhandle:
        dna_motif = r'(?=(GACTAGGGA))'
        for line in fhandle:
            line_strip = line.strip()
            for match in re.finditer(dna_motif, line_strip):
                start_index = match.start() + 1  # +1 because positions are 1-indexed
                index_list.append(start_index)
    result = ' '.join(map(float, index_list))
    return result
print(read_file("rosalind_subs (2).txt"))