import argparse
import mcb185
import math

def findent(counts, total):
	h = 0
	for n in counts:
		if n != 0: h -= n/total * math.log2(n/total)
	return h
	
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, 
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

for dl, seq in mcb185.read_fasta(arg.file):
	seq = seq[:120]		# only first 120 nts
	mask = list(seq)
	for i in range(len(seq) - arg.size + 1):
		count = [0, 0, 0, 0]
		for j in range(i, i + arg.size):
			if   seq[j] == 'A': count[0] += 1
			elif seq[j] == 'C': count[1] += 1
			elif seq[j] == 'G': count[2] += 1
			else:		    count[3] += 1
		entropy = findent(count, arg.size)
		if entropy < arg.entropy:
			for j in range(i, i + arg.size):
				if arg.lower: mask[j] = mask[j].lower()
				else:         mask[j] = 'N'
	print(''.join(mask))
