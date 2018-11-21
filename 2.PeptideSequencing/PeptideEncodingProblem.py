complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
table = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R',
         'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H',
         'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R',
         'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
         'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
         'GUC': 'V', 'GUG': 'V',
         'GUU': 'V', 'UAA': '', 'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
         'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F',
         }
translate = lambda pattern: "".join([table[pattern[i:i + 3]] for i in range(0, len(pattern), 3)])
revers = lambda substring: "".join([complement[i] for i in substring][::-1])
DNA = input()
acid = input()
len_peptid = len(acid) * 3
print(' '.join([substring for substring in [DNA[i:i + len_peptid] for i in range(0, len(DNA) - len_peptid + 1)]
                if translate(substring.replace('T', 'U')) == acid or translate(
        revers(substring).replace('T', 'U')) == acid]))
