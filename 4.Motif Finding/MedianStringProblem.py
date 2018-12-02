def hamming_distance(pattern, motif):
    return sum([1 for i in range(len(motif)) if pattern[i] != motif[i]])


def k_mer_patterns(k):
    patterns = ["A", "C", "G", "T"]
    while len(patterns[0]) < k:
        patterns = [patterns[l] + j for j in ["A", "C", "G", "T"] for l in range(0, len(patterns))]
    return patterns


def min_distance(pattern, text):
    k = len(pattern)
    return min([hamming_distance(pattern, text[i:i + k]) for i in range(len(text) - k + 1)])


def distance_between_pattern_and_dna(pattern, DNA):
    return sum([min_distance(pattern, DNA_string) for DNA_string in DNA])


def median_string(k, DNA):
    patterns = k_mer_patterns(k)
    median = {distance_between_pattern_and_dna(pattern, DNA): pattern for pattern in patterns}
    return median[min(median.keys())]


if __name__ == "__main__":
    k = int(input())
    DNA = [input() for i in range(10)]
    print(median_string(k, DNA))
