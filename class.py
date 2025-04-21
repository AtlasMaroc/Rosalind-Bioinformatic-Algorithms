import re


class File:

    def __init__(self, filename):
        self.filename = filename

    def input_file(self):
        read_file = open(self.filename, 'r')
        line_strip = [items.strip() for items in read_file.readlines()]
        return line_strip

    @staticmethod
    def dictionary(line_strip):

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

def extract_kmers(id_seq):

    '''
    a function for extracting kmers of half the length of the sequence

    parameters: a dictionary where the keys are ids and values are the corresponding DNA sequence

    output: a dictionary mapping the different ids to a list of kmers
    '''

    list_dna = []
    list_kmer = []
    k_len = len(next(iter(id_seq.values()))) // 2
    lis_dic = {}

    for key, value in id_seq.items():
            kmer_p = [value[i:i+k_len] for i in range(k_len+1)]
            lis_dic[value] = kmer_p

    for key, value in lis_dic.items():
        list_dna.append(key)
        list_kmer.append(value)

    return list_dna, list_kmer

def collapse(list_kmer, list_dna):

    stri = ''
    current_stri = False

    for i in range(len(list_kmer)):
        if current_stri is False:
            current_kmer = list_kmer[i]
            if i < len(list_kmer)-1:
                next_kmer = list_kmer[i+1]
                for kmer in current_kmer:
                   if kmer in next_kmer:
                     curr_dna = list_dna[i]
                     next_dna = list_dna[i + 1]
                     if next_dna.startswith(kmer):
                        stri += curr_dna + next_dna[next_kmer.index(kmer) + len(kmer):]
                     if next_dna.endswith(kmer):
                         stri += next_dna + curr_dna[current_kmer.index(kmer) + len(kmer):]
                     if current_kmer.startends(kmer):

                     current_stri = True

                     break




    return stri

def main():
    file = File('rosalind_splc.txt')
    arr = file.input_file()
    dicti = file.dictionary(arr)
    list_dna, list_kmer = extract_kmers(dicti)
    col_string = collapse(list_kmer, list_dna)
    print(col_string)


main()

#else:
#for kmer in list_kmer[i]:
 #   curr_dna = ''.join(list_dna[i])
  #  if kmer in stri:
   #     match_index = list_kmer[i].index(kmer)
    #   stri += curr_dna[match_index + len(kmer):]

#ATTAGTTAGATAGACAGACCGACCTACCTGCTGCCGGCCGGCCGGACGGAA
#ATTAGACCTGCCGGAATAC
#ATTAGACCTGCCGGAATAC
#CCTGCCGGAACG
#['ATTAGACCTG', 'CCTGCCGGAA', 'AGACCTGCCG', 'GCCGGAATAC']

#if kmer in next_kmer:
 #   match_index = next_kmer.index(kmer)
  #  curr_dna = list_dna[i]
   # next_dna = list_dna[i + 1]
    #stri += curr_dna + next_dna[next_kmer.index(kmer) + len(kmer):]

    #current_stri = True

    #break