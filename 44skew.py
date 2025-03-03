import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))

s = seq[0:w]
print(0, sequence.gc_comp(s), sequence.gc_skew(s))
for i in range(1, len(seq) -w +1):
	s = s.replace(seq[i-1], '', 1) + seq[i+w-1]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))
	
