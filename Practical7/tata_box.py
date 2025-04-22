import re

infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('tata_genes.fa', 'w')

current_header = ''
current_sequence = ''
    
for line in infile:
    line = line.strip()
    if line.startswith('>'):
        if current_header and re.search(r'TATA[AT]A[AT]', current_sequence):
                gene_name = re.findall(r'gene:([^\s]+)', current_header)
                outfile.write('>{}\n{}\n'.format(gene_name[0], current_sequence))
        current_header = line
        current_sequence = ''
    else:
        current_sequence += line
    
if current_header and re.search(r'TATA[AT]A[AT]', current_sequence):
    gene_name = re.findall(r'gene:([^\s]+)', current_header)
    outfile.write('>{}\n{}\n'.format(gene_name[0], current_sequence))
infile.close()
outfile.close()