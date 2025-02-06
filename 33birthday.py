# Birthday

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

count = 0

for i in range(trials):
	bday = []
	for i in range(people): 
		birthday = random.randint(1, days)
		if birthday in bday:
			count += 1
			break
		bday.append(birthday)
			
print(count/trials)
	
