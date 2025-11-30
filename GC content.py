import re
from Bio.Seq import Seq

class File:

    def __init__(self, filename):
        self.filename = filename

    def input_file(self):
        read_file = open(self.filename, 'r')
        line_strip = [items.strip() for items in read_file.readlines()]
        return line_strip

    def dictionary(self, line_strip):

       id_seq = {}
       dna_strand = ""
       current_id= None

       for line in line_strip:
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

class LCR:
    def __init__(self, id_seq):
        self.id_seq = id_seq
        self.rev_dic = {}

    def extract(self):

      loc_len = {}   #dictionary corresponding to localisation and length
      comp_seq = "".join(list(self.id_seq.values())[0])
      dna_len = len(comp_seq)

      for x in range(4, 13):
        for i in range(dna_len-x+1):
            forward_sub = comp_seq[i: i + x]
            # Compute reverse complement of this substring
            rev_comp_sub = str(Seq(forward_sub).reverse_complement())

            if forward_sub == rev_comp_sub:
                loc_len[i + 1] = x

      return loc_len


def main():
    file = File('rosalind_revp.txt')
    arr = file.input_file()
    dicti = file.dictionary(arr)
    lcr = LCR(dicti)
    extr = lcr.extract()
    for key in sorted(extr):
        print(f"{key}\t{extr[key]}")


main()


# open a while loop and check if they are under 6 unique concatenated items in the list
# iterate over the indeces  and pop the current index and assign to the last index
# concatenate the newly formed list and assign it to the principal list








