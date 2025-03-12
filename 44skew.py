import sequence
import sys
import mcb185

w = int(sys.argv[2])
for dl, s in mcb185.read_fasta(sys.argv[1]):
	seq = s[0:w]
	c_count = seq.count('C')
	g_count = seq.count('G')
	
	for i in range(len(seq)-w-1):
		gc_skew = (g_count - c_count)/(g_count + c_count)
		print(gc_skew)
		
		if   s[i] == 'C': c_count -= 1
		elif s[i] == 'G': g_count -= 1
		
		if   s[i+w+1] == 'C': c_count += 1
		elif s[i+w+1] == 'G': g_count += 1
		
		

