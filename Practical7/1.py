import re
da=input("Enter splice donor/acceptor combination (GTAG, GCAG, ATAG): ")
file=open(da+"_spliced_genes.fa", "w")
genes=open('tata_genes.fa', 'r')
name=""
a=""
intron=""
for line in genes:
    lin = line.rstrip()
    if '>' in lin:
#create a viable called name to contain gene' name
        name=lin
    else:
         #cut intron with given donor and acceptor
        intron =re.findall(fr'({da[0:2]}.+?{da[2:4]})',lin)
        instance=0
        for i in range(len(intron)):
        #calculate the instance number
            if re.search('TATAAAA',intron[i]) or re.search('TATAAAT',intron[i]) or re.search('TATATAA',intron[i]) or re.search('TATATAT',intron[i]):
                instance+=1
        file.write(f'{name} instance number:{instance}\n{lin}\n')
file.close()
genes.close()