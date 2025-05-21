import matplotlib.pyplot as plt

def plot_amino_acid_frequency(mrna_sequence):
    # Define the codon to amino acid translation table
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    amino_acids = []
    # Iterate through each codon in steps of 3, starting from the beginning of the sequence
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3].upper()  # Ensure codon is uppercase
        if len(codon) != 3:
            continue  # Skip incomplete codons
        aa = codon_table.get(codon, 'X')  # Default to 'X' for unknown codons
        if aa == 'STOP':
            break  # Stop translation at the first stop codon
        amino_acids.append(aa)
    
    # Count the frequency of each amino acid
    frequency = {}
    for aa in amino_acids:
        frequency[aa] = frequency.get(aa, 0) + 1
    
    # Generate the bar plot
    plt.figure(figsize=(12, 6))
    colors = plt.cm.tab20(range(len(frequency)))  # Use a colormap for varied colors
    plt.bar(frequency.keys(), frequency.values(), color=colors)
    
    plt.xlabel('Amino Acid', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.title('Amino Acid Frequency Distribution', fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()
print(plot_amino_acid_frequency("AUGCGCUUACCAU"))