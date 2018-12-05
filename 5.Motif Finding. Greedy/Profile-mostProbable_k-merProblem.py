from functools import reduce


def pr(pattern, profile):
    return reduce(lambda x, y: x * y, [profile[pattern[i]][i] for i in range(len(pattern))])


def most_probable_k_mer(dna, k, profile):
    k_mers = {pr(dna[i:i + k], profile): dna[i:i + k] for i in range(len(dna) - k + 1)}
    return k_mers[max(k_mers.keys())]

if __name__ == "__main__":
    dna = input()
    k = int(input())
    profile = {i: list(map(float, input().split(" "))) for i in ["A", "C", "G", "T"]}
    print(most_probable_k_mer(dna, k, profile))
