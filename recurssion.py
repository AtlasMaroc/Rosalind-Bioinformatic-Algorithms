from io import StringIO
from Bio import SeqIO
import requests
import re
import sys

if len(sys.argv) < 1 :
    sys.exit(1)


def input_file(file):

    open_file = open(file, 'r')
    lines = [items.strip() for items in open_file.readlines()]
    return lines
def extra_id(lines):

    seq_id = {}
    for i in  range(0, len(lines)):
        split = lines[i].split('_')
        seq_id[split[0]] = lines[i]
    return seq_id

def load_sequence(seq_id):

     dictionary = { ids: '' for ids in seq_id}

     general_url = "http://www.uniprot.org/uniprot/"

     for i in range(0,len(seq_id)):

         current_url = general_url+seq_id[i]+'.fasta'
         response = requests.get(current_url)
         cData = ''.join(response.text)
         Seq = StringIO(cData)
         record = "".join(list(SeqIO.read(Seq, 'fasta')))
         dictionary[seq_id[i]] = record
     return dictionary


def motif(dictionary):

    match = {key: [] for key in dictionary}
    protein_motif = rf'{sys.argv[2]}'
    id_list = [key for key in dictionary.keys()]
    for key in id_list:
        for ids in re.finditer(protein_motif, dictionary[key]):
            start_index = ids.start() + 1
            match[key].append(start_index)

    return match

def main():
    file = sys.argv[1]
    load_file = input_file(file)
    id_seq = extra_id(load_file)
    truncated_ids = list(id_seq.keys())
    original_ids = list(id_seq.values())
    sequence = load_sequence(truncated_ids)
    preliminary_result = motif(sequence)
    result = {}

    for truncated, original in id_seq.items():
        if truncated in preliminary_result.keys():
            result[original] = preliminary_result[truncated]

    for key, value in result.items():
        if value:  # This checks if 'value' (the list) is not empty
            print(key)
            print(" ".join(map(str, value)))
main()

