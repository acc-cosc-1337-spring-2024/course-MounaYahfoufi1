#
def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA strands must be of equal length")
    
    distance = sum(1 for x, y in zip(dna1, dna2) if x != y)
    return distance

def get_dna_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    dna_complement = ''.join(complement[base] for base in dna)
    return dna_complement
