table = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186,
}
peptide = input()
mass = lambda x: sum([table[i] for i in x])
n = len(peptide)
peptide += peptide[0:-1]
print(
    " ".join(
        map(str,
            (sorted(
                [0, mass(peptide[0:n])] + [mass(k) for k in [peptide[j:j + i]
                                                             for i in range(1, n)
                                                             for j in range(0, n)]]))))
)
