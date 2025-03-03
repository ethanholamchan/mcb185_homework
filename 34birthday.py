# Birthday

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

count = 0

for i in range(trials):
	calendar = [0] * days
	for i in range(people):
		bday = random.randint(0, days-1)
		calendar[bday] += 1
		if calendar[bday] == 2: 
			count += 1
			break

print(count / trials)
