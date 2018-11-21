def pattern_count(sample, genome):
    return sum([1 for i in range(0, len(genome) - len(sample)) if genome[i:i + len(sample)] == sample])


text = input()
k = int(input())
d = {i: {} for i in range(len(text))}
for i in range(0, len(text) - k):
    d[pattern_count(text[i:i + k], text)][text[i:i + k]] = None
d = {k: v for k, v in d.items() if v != {}}
print(" ".join(d[max(d.keys())].keys()))
