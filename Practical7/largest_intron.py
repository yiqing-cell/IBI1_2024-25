import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

# find all GT...AG
matches = re.findall(r'(?=(GT.+?AG))', seq)

max_length = 0
for match in matches:
    intron_length = len(match) 
    if intron_length > max_length:
        max_length = intron_length

print(f"The length of the largest intron is: {max_length}")
