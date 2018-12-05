from functools import reduce


def prob(profile, pattern):
    return reduce(lambda x, y: x * y, [profile[pattern[i]][i] for i in range(len(pattern))])


def profile_most_probable(dna, k, profile):
    k_mers = sorted([(prob(profile, dna[i:i + k]), dna[i:i + k]) for i in range(len(dna) - k + 1)],
                    key=lambda x: x[0],
                    reverse=True)
    return k_mers[0][1]


def get_profile(motifs):
    n = 4
    m = len(motifs[0])
    nucleotides = ["A", "C", "G", "T"]
    profile = {nucleotides[i]: [0] * m for i in range(n)}
    for i in range(len(motifs)):
        for j in range(len(motifs[i])):
            profile[motifs[i][j]][j] += 1
    for i in nucleotides:
        for j in range(m):
            profile[i][j] = profile[i][j] / len(motifs)
    return profile


def score(motifs):
    score = 0
    for j in range(len(motifs[0])):
        count = 0
        counts = {i: 0 for i in ["A", "C", "G", "T"]}
        for i in range(len(motifs)):
            counts[motifs[i][j]] += 1
            count += 1
        score += count - max(counts.values())
    return score


def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][0:k])

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]

        for j in range(1, t):
            profile = get_profile(motifs)
            motifs.append(profile_most_probable(dna[j], k, profile))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs.copy()
    return best_motifs


if __name__ == "__main__":
    k, t = tuple(map(int, input().split(" ")))
    dna = [input() for i in range(5)]
    print("\n".join(greedy_motif_search(dna, k, t)))
