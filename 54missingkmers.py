import sys
import mcb185
import itertools

def find_missing_kmers(seq):
	k = 1
	while True:
		seen_kmers = set()
		total_kmers = set()
		
		for nts in itertools.product('ACGT', repeat=k):
	       		total_kmers.add(''.join(nts))
			       		
		for i in range(len(seq) - k + 1):
			seen_kmers.add(seq[i:i+k])
			if seen_kmers == total_kmers: break
			
		if seen_kmers != total_kmers:	
			rev_seq = mcb185.anti_seq(seq)
			for i in range(len(rev_seq) - k + 1):
				seen_kmers.add(rev_seq[i:i+k])
				if seen_kmers == total_kmers: break
		
		missing_kmers = total_kmers - seen_kmers
		if missing_kmers: return k, missing_kmers
		
		k += 1


for dl, seq in mcb185.read_fasta(sys.argv[1]):
	k, missing_kmers = find_missing_kmers(seq)
	print(k, len(missing_kmers))

