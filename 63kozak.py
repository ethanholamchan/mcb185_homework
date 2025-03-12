import sys
import gzip
import re
import mcb185

input_file = sys.argv[1]
origin_found = False
cds = {}
seqs = []

rows, cols = 14, 4
counts = []
for _ in range(rows):
	counts.append([0] * cols)

def get_cds_coord(words):
	strand = '+'
	if 'complement' in words[0]: strand = '-'
	coords = re.sub(r"[a-zA-Z]", "", words[0]).split('..')
	if strand == '-': return int(coords[len(coords)-1].rstrip(')')), strand
	else:             return int(coords[0].lstrip('(')), strand
		
def find_cds_region(coord, strand, genome):
	if strand == '+': return genome[coord-10:coord+4]
	else:		  return mcb185.anti_seq(genome[coord-5:coord+9])

with gzip.open(input_file, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[0] == 'CDS': 
			coord, strand = get_cds_coord(words[1:])
			cds[coord] = strand
		if 'ORIGIN' in words: origin_found = True
		if origin_found:
			seqs.append(''.join(words[1:])) 
			
genome = ''.join(seqs)

for coord, strand in cds.items():
	cds_region = find_cds_region(coord, strand, genome)
	for i in range(rows):
		if   cds_region[i] == 'a': counts[i][0] += 1
		elif cds_region[i] == 'c': counts[i][1] += 1
		elif cds_region[i] == 'g': counts[i][2] += 1
		else:                      counts[i][3] += 1

print("AC IMTSU001\nXX\nID ECKOZ\nXX\nDE I made this shit up")
print(f"{'PO':<9}{'A':<9}{'C':<9}{'G':<9}{'T':<9}")
for i in range(rows):
	print(f'{i+1:<8}', f'{counts[i][0]:<8}', f'{counts[i][1]:<8}', 
	f'{counts[i][2]:<8}', f'{counts[i][3]:<8}')
