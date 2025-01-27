# Death Saves
# Must take race argument all lowercase

import random

def death_saves(race):
	fails = 0
	succs = 0
	
	while True:
		roll = random.randint(1, 20)
		if race == 'halfling':
			roll2 = random.randint(1, 20)
			if roll 2 > roll: roll = roll2
		if   roll == 1 : fails += 2
		elif roll == 20: 
			return 'You have gained 1 health and have revived!'
			break
		elif roll >= 10: succs += 1
		else:	         fails += 1
		
		if fails >= 3 or succs == 3: 
			if fails >= 3: return 'You died:('
			else:          return 'You are stable, but unconscious...'
			break
print(death_saves(''))
		
