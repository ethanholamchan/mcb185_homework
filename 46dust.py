import sys
import mcb185
import math

def findent(counts, total):
	h = 0
	for n in counts:
		if n != 0: h -= n/total * math.log2(n/total)
	return h

fastafile = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

for dl, seq in mcb185.read_fasta(sys.argv[1]):
	seq = seq[:120]		# only first 120 nts
	mask = list(seq)
	for i in range(len(seq) - w + 1):
		count = [0, 0, 0, 0]
		for j in range(i, i + w):
			if   seq[j] == 'A': count[0] += 1
			elif seq[j] == 'C': count[1] += 1
			elif seq[j] == 'G': count[2] += 1
			else:		    count[3] += 1
		entropy = findent(count, w)
		if entropy < threshold:
			for j in range(i, i + w):
				mask[j] = 'N'
	print(''.join(mask))
	

