amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def expand(peptides):
    new_peptides = []
    if len(peptides) == 0:
        new_peptides = [[i] for i in list(amino_acid_masses)]
    else:
        for i in peptides:
            for j in amino_acid_masses:
                new_peptides.append(i + [j])
    return new_peptides


def is_consistend(peptide, spectrum):
    for p in lenearspectrum(peptide):
        if p not in spectrum:
            return False
    return True


def lenearspectrum(peptide):
    n = len(peptide)
    return list(map(int,
                    (sorted(
                        [0, sum(peptide[0:n])] + [sum(k) for k in [peptide[j:j + i]
                                                                   for i in range(1, n)
                                                                   for j in range(0, n)]]))))



def cyclospectrum(peptide):
    n = len(peptide)
    peptide2 = peptide + peptide[0:-1]
    return list(map(int,
                    (sorted(
                        [0, sum(peptide2[0:n])] + [sum(k) for k in [peptide2[j:j + i]
                                                                    for i in range(1, n)
                                                                    for j in range(0, n)]]))))
def Trim(n, Leaderboard, spectrum):
    return [j[1] for j in sorted([(LinearScore(i,spectrum),i) for i in Leaderboard ],key= lambda x: x[0])[0:n]]


def LinearScore(peptid,exSpectrum):

    teorSpectrum=lenearspectrum(peptid)
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

def leaderboard_cyclopeptide_sequencing(n,spectrum):
    def mass(peptide):
        return sum(peptide)

    def parent_mass(spectrum):
        return spectrum[-1]

    Leaderboard = expand([])
    while len(Leaderboard):
        if len(Leaderboard) != 18: Leaderboard = expand(Leaderboard)
        Leaderboard = list(filter(lambda x: is_consistend(x, spectrum), Leaderboard))
        LeaderPeptid = []
        t = Leaderboard[:]
        for peptide in t:
            if mass(peptide) == parent_mass(spectrum):
                if LinearScore(peptide, spectrum) > LinearScore(LeaderPeptid, spectrum):
                    LeaderPeptid =peptide

                Leaderboard.remove(peptide)
            elif mass(peptide) > parent_mass(spectrum):
                Leaderboard.remove(peptide)
        Leaderboard = Trim(n, Leaderboard, spectrum)

    return LeaderPeptid


if __name__ == "__main__":
    def peptides_to_string(peptide): return "-".join([str(j) for j in peptide])
    n=int(input())
    spectrum = list(map(int, input().split(" ")))
    print(peptides_to_string(leaderboard_cyclopeptide_sequencing(n,spectrum)))

