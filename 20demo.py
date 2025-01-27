# Ethan Chan Unit 2 Demo MCB185

import math
import random
'''
# Tuples

t = 1, 2
print (t)
print (type(t))

person = 'Steve', 21, 57891.50
print (person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2)/ 2
	return x, y
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
print(m[0], m[1])
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

# Iteration

#while True:
#	print('hello')

i = 0
while i < 3:
	i = i + 1
	print('hey', i)

i = 0
while i < 10:
	print(i)
	i += 3
print('final value of i is ', i)

for i in range(1, 10, 3): print(i)
for i in range(1, 5): print(i)
for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
for i in range(len(basket)):
	print(basket[i])

# Nesting

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:	       print(i, 'is odd')

# Practice Problems

def triangular_num(n):
	total = 0
	for i in range(n): total+=i
	return total
print(triangular_num(4))

def factorial(n):
	total = 1
	for i in range(1, n + 1): total = total * i
	return total
print(factorial(4))

def poisson(k, n):
	for i in range (1, k): print('n:', n, ' k: ', i, 'Poisson: ', (n**i * math.e**(-n)) / factorial(i))
print(poisson(4, 2))

def n_choose_k(n, k) : return factorial(n) / (factorial(k) * (factorial(n-k)))
print(n_choose_k(4, 2))

def euler(n): 
	total = 0
	for i in range(1, n + 1): total += (1 / factorial(i))
	return total
print(euler(4))
print(euler(10))

def is_prime(n):
	for i in range(2, n // 2):
		if n % i == 0: return True
	return False
print(is_prime(45))
print(is_prime(23))

def pi(n):
	pi = 3
	for i in range(1, n + 1):
		if (i % 2 == 0): pi -= 4/(2 * i * (2 * i + 1) * (2 * i + 2))
		else           : pi += 4/(2 * i * (2 * i + 1) * (2 * i + 2))
	return pi
print(pi(4))
print(pi(10))

# Random Numbers

for i in range(5): print(random.random())

for i in range(3): print(random.randint(1, 6))

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# More Practice

def monte_carlo_pi():
	inside = 0
	total  = 0
	while True:
		x      = random.random()
		y      = random.random()
		dist   = math.sqrt(x**2 + y**2)
		total+=1
		if dist < 1: inside+=1
		print(inside / total * 4)

def dnd_stats(rules):
	total = 0
	if   rules == '3D6':
		for i in range(3): 
			total += random.randint(1, 6) 
	elif rules == '3D6r1':
		for i in range(3):
			roll = random.randint(1, 6)
			if roll != 1: total += roll
	elif rules == '3D6x2':
		for i in range(3):
			roll1 = random.randint(1, 6)
			roll2 = random.randint(1, 6)
			if   roll1 > roll2: total += roll1
			elif roll1 < roll2: total += roll2
			else: 		    total += roll1
	elif rules == '4D6d1':
		rolls = [0, 0, 0, 0]
		for i in range(4): 
			rolls[i] = random.randint(1, 6)
		minimum = rolls[0]
		for i in range(1, 4):
			if rolls[i] < rolls[i-1]: minimum = rolls[i]
		for i in range(4): total += rolls[i]
		total -= minimum
	return total / 3
print('3D6', dnd_stats('3D6'))
print('3D6r1', dnd_stats('3D6r1'))
print('3D6x2', dnd_stats('3D6x2'))
print('4D6d1', dnd_stats('4D6d1'))
'''
# Assessment Examples

# 4a. change line 1.. to while i < n where n is the n where n is the number of interations
# 4b. add an if statement after line 176 using the isclose() function or doing pi % math.pi == any tiny number e-10 or something
def gl_pi():
	i  = 0
	j  = 0
	pi = 0
	while True:
		i += 1
		if i % 2 == 1:
			j += 1
			if j % 2 == 1: pi += (1 / i)
			else:          pi -= (1 / i)
			print(pi * 4)


		
		
			
