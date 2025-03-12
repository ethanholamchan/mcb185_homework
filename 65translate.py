import argparse
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100, 
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_false', 
	help='also examine the anti-parallel strand')
arg = parser.parse_args()
print('translating', arg.file, arg.min, arg.anti)

for dl, seq in mcb185.read_fasta(arg.file):
	aa_seq = mcb185.translate(seq).split('*')
	for aas in aa_seq:
		if len(aas) >= arg.min:
			print(dl)
			print(aas[aas.find('M'):])
