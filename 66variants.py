import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()
print('variations between', arg.gff, arg.vcf)

variants = []
gene_functions = []

with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		words = line.split()
		variants.append([int(words[1]), words[0]])

with gzip.open(arg.gff, 'rt') as fp:
	for line in fp:
		words = line.split()
		if line[0] == 'I' or line[0] == 'V'or line[0] == 'X':
			num = words[0]
			function = words[2]
			beg = int(words[3])
			end = int(words[4])
			gene_functions.append([function, beg, end, num])

for var in variants:
	functions = []
	for gf in gene_functions:
		if var[0] > gf[1] and var[0] < gf[2] and var[1] == gf[3]:
			if gf[0] not in functions: functions.append(gf[0])
	print(f"{var[1]:<8}", f'{var[0]:<8}', f"{','.join(functions):<8}")

