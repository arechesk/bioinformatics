mass = int(input())
amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
counts = [1]+[0]*mass
for i in range(57, mass+1):
    for j in amino_acid_masses:
            counts[i] += counts[i-j]
print(counts[mass])
