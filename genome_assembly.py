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
       return list(id_seq.values())

def overlap(a, b, min_length):
    """
    Return the length of the maximum overlap between the suffix of 'a' and the prefix of 'b'
    if that overlap is at least 'min_length'. Otherwise, return 0.
    """
    start = 0  # start all the way at the beginning of a
    best = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            break
        # Check if b matches a's suffix starting at this index
        if b.startswith(a[start:]):
            overlap_length = len(a) - start
            if overlap_length > best:
                best = overlap_length
        start += 1
    return best


def greedy_superstring(reads):
    """
    Given a list of reads (DNA strings), repeatedly merge the pair with the maximal
    overlap (which must be more than half the length of a read) until one string remains.
    """
    # We assume that all reads are of equal length (or approximately equal) and
    # that the required overlap is > len(read) // 2.
    min_length = len(reads[0]) // 2 + 1

    while len(reads) > 1:
        max_overlap = 0
        best_pair = None
        best_merged = ""

        # Try all ordered pairs of reads
        for i in range(len(reads)):
            for j in range(len(reads)):
                if i == j:
                    continue
                a, b = reads[i], reads[j]
                ov = overlap(a, b, min_length)
                if ov > max_overlap:
                    max_overlap = ov
                    best_pair = (i, j)
                    best_merged = a + b[ov:]

        if max_overlap == 0:
            # No pair found with sufficient overlap (should not happen given the problem guarantee)
            break

        # Merge the best pair
        i, j = best_pair
        # Remove the reads in reverse order so the indices remain valid.
        reads.pop(max(i, j))
        reads.pop(min(i, j))
        reads.append(best_merged)

    return reads[0]

def main():
    file = File('rosalind_splc.txt')
    arr = file.input_file()
    dicti = file.dictionary(arr)
    col_string = greedy_superstring(dicti)
    print(col_string)

main()