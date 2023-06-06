import random

def generate_dna_sequence(length):
    nucleotides = ['A', 'T', 'C', 'G']
    sequence = ''

    for _ in range(length):
        nucleotide = random.choice(nucleotides)
        sequence += nucleotide

    return sequence

def generate_subsequences(sequence, k):
    subsequences = []
    for i in range(len(sequence) - k + 1):
        subsequence = sequence[i:i+k]
        subsequences.append(subsequence)
    return subsequences

dna_sequence = generate_dna_sequence(700)
subsequences = generate_subsequences(dna_sequence, 7)

print(dna_sequence)
print(subsequences)

# for subsequence in subsequences:
#     print(subsequence)
