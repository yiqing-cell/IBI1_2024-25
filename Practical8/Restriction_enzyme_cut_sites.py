def find_restriction_sites(dna_sequence, enzyme_sequence):
    dna_sequence = dna_sequence.upper()
    enzyme_sequence = enzyme_sequence.upper()
    
    if not all(base in "ACGT" for base in dna_sequence) or not all(base in "ACGT" for base in enzyme_sequence):
        return "Error: Sequences must contain only A, C, G, T."
    for i in range(len(dna_sequence) - len(enzyme_sequence) + 1):
        if dna_sequence[i:i + len(enzyme_sequence)] == enzyme_sequence:
            positions=i
            return positions

# Example call
print("Cut sites:", find_restriction_sites("AAGCTTCGAATTC", "GAATTC"))