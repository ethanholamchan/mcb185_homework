# Saving Throws
# Must take dc argument as integer up to 20 and adv argument as string all lowercase

import random

def saving_throws(dc, adv):
	roll = random.randint(1, 20)
	if adv == 'advantage':
		roll2 = random.randint(1, 20)
		if roll < roll2: roll = roll2
	elif adv == 'disadvantage':
		roll2 = random.randint(1, 20)
		if roll > roll2: roll = roll2
	if roll >= dc: return 'Success'
	else         : return 'Fail'
print(saving_throws(5, ''))
print(saving_throws(10, 'advantage'))
print(saving_throws(15, 'disadvantage'))

	
		
	
