import sequence
import sys
import mcb185

seq = ''
for dl, s in mcb185.read_fasta(sys.argv[1]):
	 seq = s

w = int(sys.argv[2])

s = seq[0:w]
print(0, sequence.gc_comp(s), sequence.gc_skew(s))
for i in range(1, len(seq) -w +1):
	s = s.replace(seq[i-1], '', 1) + seq[i+w-1]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))	
