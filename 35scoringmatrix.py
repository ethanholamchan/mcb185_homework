# Scoring System

import sys

seq      = sys.argv[1]
match    = sys.argv[2]
mismatch = sys.argv[3]

matrix = [[0 for _ in range(len(seq) + 1)] for _ in range(len(seq) + 1)]

matrix[0][0] = None

for i in range(len(seq)): matrix[i+1][0] = seq[i]
for j in range(len(seq)): matrix[0][j+1] = seq[j]

for i in range(len(seq)):
	for j in range(len(seq)):
		if seq[i] == seq[j]: matrix[i+1][j+1] = match
		else:                matrix[i+1][j+1] = mismatch

for i in range(len(seq) + 1): print(str(matrix[i]))

