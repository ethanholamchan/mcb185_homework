import sys
import mcb185

aalength = int(sys.argv[2])

for dl, seq in mcb185.read_fasta(sys.argv[1]):
	counter = 0
	words = dl.split()
	for frame in range(3)
		translation = mcb185.translate(seq, frame=frame)
		aaseqs = translation.split('*')
		for s in aaseqs:
			if len(s) >= aalength and s[0] == 'M':
				print('>', words[0], '-prot-', str(counter))
				print(s + '*')
				counter += 1
	seq = mcb185.antiseq(seq)
	for frame in range(3)
		translation = mcb185.translate(seq, frame=frame)
		aaseqs = translation.split('*')
		for s in aaseqs:
			if len(s) >= aalength and s[0] == 'M':
				print('>', words[0], '-prot-', str(counter))
				print(s + '*')
				counter += 1
