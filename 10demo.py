# 10demo.py by Ethan Chan

import math
'''
print ('hello, again') # greeting

# Basic arithmetic

print (1.5e-2)
print (5 % (1 + 2))
print (3 + 4)
print (3**3)
print (math.pow(3, 3))
print (math.sqrt(4))
print (math.log10(1000))

print (0.1 * 1)
print (0.1 * 3)

# Variables

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print (c)

print (type(a), type (b), type(c))
print (type(a), type (b), type(c), sep= ', ', end= '!\n')

def pythagoras(a, b): return math.sqrt (a**2 + b**2)
print(pythagoras(3, 4))

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2

# Practice Functions

def ftoc(f): return (f - 32) * 5 / 9
def ctof(c): return (c * 9 / 5) + 32
def mph_to_kph(mph): return mph * 1.60934
def kph_to_mph(kph): return kph / 1.60934
def compute_dna_concentration(od260) : return od260 * 50
def arithmetic_mean_3nums(a, b, c) : (a + b + c) / 3
def geometric_mean_3nums(a, b, c) : (a * b * c)**(1/3)
def harmonics_mean_3nums(a, b, c) : 3/(1/a + 1/b + 1/c)
def distance(ax, ay, bx, by) : math.sqrt((ax-bx)**2 + (ay-by)**2)

# Strings

s = 'hello world'
print (s, type(s))

# Conditionals

a = 2
b = 2
if a ==b:
	print ('a equals b')
print (a, b)

def is_even(x):
	if x % 2 == 0 : return True
	return False
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print (type(c))

if   a < b: print('a < b')
elif a > b: print('a > b')
else:  	    print('a = b')

if   a < b:  print('a < b')
elif a >= b: print('a >= b')
elif a == b: print('this will never print')

if a < b or a > b: print('all things being equal, and and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:  	    print('a = b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')
if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
#if a < s: print ('a < s')

# None Type

def silly(m, x, b): y = m * x + b
print(silly(2, 3, 4))

# More Practice

def is_integer(i):
	if i % 0.5 == 0: return True
	else:            return False
print(is_integer(3))
print(is_integer(3.1))

def is_valid_prob(x):
	if x >= 0 and x <= 1: return True
	else:                 return False
print(is_valid_prob(3))
print(is_valid_prob(0.75))

def dna_letter_weight(nt):
	if nt == 'A' or nt == 'T' or nt == 'C' or nt == 'G': return (nt + ' weighs about 330 kDa')
print(dna_letter_weight('T'))
print(dna_letter_weight('G'))
print(dna_letter_weight('B'))

def dna_complement(nt):
	if   nt =='A': return 'T'
	elif nt =='T': return 'A'
	elif nt =='C': return 'G'
	elif nt =='G': return 'C'
	return
print(dna_complement('A'))
print(dna_complement('C'))
print(dna_complement('H'))

print('expected: T, F, F, T, T weighs about 330 kDa, G weighs about 330 kDa, none, T, G, none')
'''
# Even More Practice

def max_3nums(a, b, c):
	max = 0
	if a > b: max = a
	else:     max = b
	if max > c: return max
	else:       return c
print(max_3nums(1, 2, 3))
print(max_3nums(3, 2, 1))
print(max_3nums(2, 3, 2))

def sens(tp, tn, fp, fn): return tp / (tp + fn)
def spec(tp, tn, fp, fn): return tn / (tn + fp)
def f1(tp, tn, fp, fn): return tp / (tp + 1/2 * (fp + fn))

print(sens(30, 5, 20, 95))
print(spec(30, 5, 20, 95))
print(f1(30, 5, 20, 95))

def shannon_entropy(a_count, c_count, g_count, t_count):
	total  = a_count + c_count + g_count + t_count
	a_prob = a_count/total
	c_prob = c_count/total
	g_prob = g_count/total
	t_prob = t_count/total
	return -(a_prob * math.log2(a_prob) + c_prob * math.log2(c_prob) + g_prob * math.log2(g_prob) + t_prob * math.log2(t_prob))

print(shannon_entropy(30, 75, 40, 110))
	
