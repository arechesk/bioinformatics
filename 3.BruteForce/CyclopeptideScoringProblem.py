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

def score(peptid,exSpectrum):

    def cyclospectrum(peptide):

        mass = lambda x: sum([table[i] for i in x])
        n = len(peptide)
        peptide2 = peptide + peptide[0:-1]
        return list(map(int,
                    (sorted(
                        [0, mass(peptide2[0:n])] + [mass(k) for k in [peptide2[j:j + i]
                                                                    for i in range(1, n)
                                                                    for j in range(0, n)]]))))
    teorSpectrum=cyclospectrum(peptid)
    score = 0
    i = 0
    j = 0
    while (i < len(teorSpectrum) and j < len(exSpectrum)):
        if (teorSpectrum[i] == exSpectrum[j]):
            i += 1
            j += 1
            score += 1
        else:
            if (teorSpectrum[i] < exSpectrum[j]):
                i += 1
            else:
                j += 1
    return score

if __name__ == "__main__":
    peptid=input()
    experimentalSpectrum=list(map(int, input().split(" ")))
    print(score(peptid,experimentalSpectrum))