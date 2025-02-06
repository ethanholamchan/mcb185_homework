# Spinner

import random
import time

count = 0
while True:
	time.sleep(0.1)
	count += 1
	if   count % 4 == 0: print('|', end='\r')
	elif count % 4 == 1: print('/', end='\r')
	elif count % 4 == 2: print('-', end='\r')
	else               : print('\\', end='\r')
	
