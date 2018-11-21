pattern = input()
d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
print("".join([d[i] for i in pattern][::-1]))
