import sys
import mcb185
import random

min_length = int(sys.argv[2])
stop_codons = {'TAA', 'TAG', 'TGA'}

def find_orfs(seq, strand, offset):
	orfs = []
	start = -1
	
	for i in range(offset, len(seq)-2, 3):
		codon = seq[i:i+3]
		if codon == 'ATG' and start == -1: 
			start = i
		elif codon in stop_codons and start != -1:
			length = i + 3 - start
			if length >= min_length:
				if strand == '+': orfs.append((start + 1, i + 3, '+'))
				else:		  orfs.append((len(seq)-i, len(seq)-start, "-"))
			start = -1
	return orfs

for dl, seq in mcb185.read_fasta(sys.argv[1]):
	rev_seq = mcb185.anti_seq(seq)
	orfs = []
	for frame in range(3): 
		orfs += find_orfs(seq, "+", frame)
	for frame in range(3): orfs += find_orfs(rev_seq, '-', frame)
	orfs.sort()
	for start, end, strand in orfs: 
		print(f"{dl}\tgene_finder\tCDS\t{start}\t{end}\t{strand}")


rand_genome = ''.join(random.choices('ACGT', k=1000000))

rev_rand = mcb185.anti_seq(rand_genome)

orfs = []
for frame in range(3): orfs += find_orfs(rand_genome, "+", frame)
for frame in range(3): orfs += find_orfs(rev_rand, '-', frame)
print(len(orfs))

