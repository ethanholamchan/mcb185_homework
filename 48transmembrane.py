import sys
import mcb185

kd_chart = {'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5, 'M': 1.9, 'A': 1.8, 
	    'G': -.4, 'T': -.7, 'S': -.8, 'W': -.9, 'Y': -1.3, 'P': -1.6, 
	    'H': -3.2, 'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9,
	    'R': -4.5
	   }

def find_kd(seq):
	total = 0
	for aa in seq:
		if aa in kd_chart: total += kd_chart[aa]
	return total/len(seq)

def has_signal_peptide(seq):
	for i in range(23):
		if 'P' not in seq[i:i+8] and find_kd(seq[i:i+8]) >= 2.5:
			return True
	return False
	
def has_hydrophobic_region(seq):
	for i in range(30, len(seq) -10):
		if 'P' not in seq[i:i+11] and find_kd(seq[i:i+11]) >= 2.0:
			return True
	return False

for dl, seq in mcb185.read_fasta(sys.argv[1]):
	if len(seq) < 30: continue
	if has_signal_peptide(seq) and has_hydrophobic_region(seq):
		print(dl)
