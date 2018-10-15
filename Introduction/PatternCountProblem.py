sample=input()
genome=input()
print( sum([1 for i in range(0,len(genome)-len(sample)) if genome[i:i+len(sample)]==sample]))

