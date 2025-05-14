# human SOD2 length:222     subcellular localisation:mitochondria matrix
# range:83.3%-100%   

import blosum as bl

def blosum():
    matrix = bl.BLOSUM(62)
    return matrix
# alignment.py
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def calculate_alignment_score(seq1, seq2, blosum62):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62[aa1][aa2]
    return score

def calculate_percentage_identity(seq1, seq2):
    identical = sum(1 for aa1, aa2 in zip(seq1, seq2) if aa1 == aa2)
    return (identical / len(seq1)) * 100

# Set file paths
human_fasta = 'P04179.fasta.txt'
mouse_fasta = 'P09671.fasta.txt'

# Read sequences
human_seq = read_fasta(human_fasta)
mouse_seq = read_fasta(mouse_fasta)
random_seq = "SKCWCDAQSCCGSMHDRGQTLVIQYQTYDVHNRKIEEYAEFYGNHNPWVPFREPLCCIWLLNKGFLGGGTFTAASIFGSDQRQELLIMGCTACRECIYGFWKAVWIAVNERHHLPTPASKDVFDFGDNCQRQLHIRWSVKTCDRIGNWCEPRNADWMQCMITENGKMFTCGGLPRIIDCPLAWPNRQSTHRCDPYNDWRLFFTLCMFCWISEIFVTLHDPDL"

blosum62 = blosum()

# Calculate scores and percentage identities
human_mouse_score = calculate_alignment_score(human_seq, mouse_seq, blosum62)
human_mouse_identity = calculate_percentage_identity(human_seq, mouse_seq)

human_random_score = calculate_alignment_score(human_seq, random_seq, blosum62)
human_random_identity = calculate_percentage_identity(human_seq, random_seq)

mouse_random_score = calculate_alignment_score(mouse_seq, random_seq, blosum62)
mouse_random_identity = calculate_percentage_identity(mouse_seq, random_seq)

# Print results
print("Human vs. Mouse:")
print(f"Alignment Score: {human_mouse_score}")
print(f"Percentage Identity: {human_mouse_identity}%\n")

print("Human vs. Random:")
print(f"Alignment Score: {human_random_score}")
print(f"Percentage Identity: {human_random_identity}%\n")

print("Mouse vs. Random:")
print(f"Alignment Score: {mouse_random_score}")
print(f"Percentage Identity: {mouse_random_identity}%")

#human-mouse  score:1097 percentage:90.1%
#human-random score:-245 percentage:5.4%
#mouse-random score:-237 percentage:5.4%
#more similar: human and mouse
#This high conservation may stem from the key function of SOD2 in eliminating superoxide anion radicals in mitochondria, and the stability of its sequence is crucial for maintaining the structure and function of proteins. This study verified the expected hypotheses through simple sequence alignment, laying the foundation for the subsequent in-depth analysis of protein functional evolution.