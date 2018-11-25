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


def cyclopeptide_sequencing(spectrum):
    def mass(peptide):
        return sum(peptide)

    def parent_mass(spectrum):
        return spectrum[-1]

    result = []
    peptides = expand([])
    while len(peptides):
        if len(result) > 1: break
        if len(peptides) != 18: peptides = expand(peptides)
        peptides = list(filter(lambda x: is_consistend(x, spectrum), peptides))
        t = peptides[:]
        for peptide in t:
            if mass(peptide) == parent_mass(spectrum):
                if cyclospectrum(peptide) == spectrum:
                    result += [peptide]
                peptides.remove(peptide)
            elif mass(peptide) > parent_mass(spectrum):
                peptides.remove(peptide)

    return result


if __name__ == "__main__":
    def peptides_to_string(peptides): return " ".join(sorted(["-".join([str(j) for j in i]) for i in peptides]))
    spectrum = list(map(int, input().split(" ")))
    print(peptides_to_string(cyclopeptide_sequencing(spectrum)))

