import re
def find_restriction_sites(dna_sequence, enzyme_sequence):
    dna_sequence = dna_sequence.upper()
    enzyme_sequence = enzyme_sequence.upper()
    
    if bool(re.search(r'[^ATCG]', dna_sequence.upper())) == True or bool(re.search(r'[^ATCG]', enzyme_sequence.upper())) == True:
        return "Error: Sequences must contain only A, C, G, T."
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i + len(enzyme_sequence)] == enzyme_sequence:
            positions=i
            return positions

# Example call
print("Cut sites:", find_restriction_sites("AAGCTTCGAATTC", "GAATTC"))