from functools import reduce


def hamming_distance(pattern, motif):
    return sum([1 for i in range(len(motif)) if pattern[i]!=motif[i]])


def is_pattern_with_at_most_d_mistakes_in_string(pattern, DNA_string, d):
    k = len(pattern)
    return reduce(lambda x,y: x | y, [hamming_distance(pattern, DNA_string[i:i + k]) <= d for i in range(len(DNA_string) - k + 1)])


def is_pattern_with_at_most_d__mistakes_in_DNA(pattern, DNA, d):
    return reduce(lambda x,y: x & y, [is_pattern_with_at_most_d_mistakes_in_string(pattern, DNA[i], d) for i in range(len(DNA))])


def mutations(pattern):
    k = len(pattern)
    return list({pattern[:i] + j + pattern[i+1:k] for i in range(0, k) for j in ["A", "C", "G", "T"]})


def motif_enumeration(k, d, DNA):
    patterns = []
    for DNA_string in DNA:
        for i in range(len(DNA[0]) - k + 1):
            pattern_curr = DNA_string[i:i+k]
            mutations_list = mutations(pattern_curr)
            for mutation in mutations_list:
                if is_pattern_with_at_most_d__mistakes_in_DNA(mutation, DNA, d):
                    patterns.append(mutation)
    return " ".join(list(set(patterns)))


if __name__ == "__main__":
    k,d = tuple(map(int,input().split(" ")))
    DNA = [input() for i in range(4)]
    print(motif_enumeration(k, d, DNA))