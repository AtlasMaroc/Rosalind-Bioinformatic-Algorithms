from suffix_tree import Tree
import re

'''
the following algorithm finds the shortest common subtring 
using a suffix tree 
'''
def input_file(file):

    open_file = open(file, 'r')
    arr_line = [item.strip() for item in open_file]
    return arr_line

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

def main():
    load_file = input_file("rosalind_lcsm.txt")
    load_dictionary = dictionnary(load_file)

    tree = Tree(load_dictionary)
    for k, length, path in tree.common_substrings():
       print(k, length, path)

main()

