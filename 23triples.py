# Triples

import math

def triples():
	for i in range(1, 101):
		for j in range(1, 101):
			hyp = math.sqrt(i**2 + j**2)
			if hyp % 1 == 0: print(i, j, hyp)
triples()
