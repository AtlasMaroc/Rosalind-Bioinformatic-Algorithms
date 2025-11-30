import re
from graphviz import Digraph
def input_file(file):

    open_file = open(file, 'r')
    arr_line = [item.strip() for item in open_file]
    return arr_line

def dictionnary(lines):

    id_seq = {}
    dna_strand = ""
    current_id= None

    for line in lines:
        match = re.match(r"^>(Rosalind_[0-9]{1})$", line)
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

class SuffixTrie(object):

    def __init__(self, dictionary):

        for key,value in dictionary.items():
            value += f"${key}"
            dictionary[key] = value

        self.root = {}

        for value in dictionary.values():
           for i in range(len(value)):
              cur = self.root

              for c in value[i:]:
                if c not in cur:
                   cur[c] = {}

                cur = cur[c]
    def coalesce(self, node):

        for c in node:
            if len(node[c]) != 1:
                self.coalesce(node[c])
            if len(node[c]) == 1:
                child_key = c
                child_node = node[c]
                merge_label_child = f'{c}{next(iter(child_node))}'
                node[merge_label_child] = node.pop(child_key)

    def FollowPath(self, substring):

        cur = self.root
        for c in substring:
            if c not in cur:
                return None
            cur = cur[c]
        return cur

    def display(self):
        """Utility to display the trie for debugging."""
        import pprint
        pprint.pprint(self.root)

def main():
    load_file = input_file("rosalind_splc.txt")
    load_dict = dictionnary(load_file)

    sequence = SuffixTrie(load_dict)
    sequence.display()
main()












