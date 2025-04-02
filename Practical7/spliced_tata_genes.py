import re

user_input = input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAG): ").upper()

output_filename = f"{user_input}_spliced_genes.fa"
donor = user_input[:2]
acceptor = user_input[2:]

with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as infile, \
     open(output_filename, 'w') as outfile:

    current_header = ''
    current_sequence = ''

    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            if current_header and re.search(fr'({donor}.+?{acceptor})', current_sequence):
                introns = re.findall(fr'({donor}.+?{acceptor})', current_sequence)
                intron_str = " ".join(introns)  
                tata_matches = re.findall(r'TATA[AT]A[AT]', intron_str)
                
                if tata_matches:
                    gene_name = re.findall(r'gene:([^\s]+)', current_header)
                    if gene_name:
                        tata_count = len(tata_matches)
                        outfile.write(f'>{gene_name[0]} {tata_count}\n{current_sequence}\n')

            current_header = line
            current_sequence = ''
        else:
            current_sequence += line
    
    # Process the last sequence
    if current_header and re.search(fr'({donor}.+?{acceptor})', current_sequence):
        introns = re.findall(fr'({donor}.+?{acceptor})', current_sequence)
        intron_str = " ".join(introns)
        tata_matches = re.findall(r'TATA[AT]A[AT]', intron_str)

        if tata_matches:
            gene_name = re.findall(r'gene:([^\s]+)', current_header)
            if gene_name:
                tata_count = len(tata_matches)
                outfile.write(f'>{gene_name[0]} {tata_count}\n{current_sequence}\n')
