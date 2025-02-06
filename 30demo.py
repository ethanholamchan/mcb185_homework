# Unit 3 Demo

import math
import sys

# Strings

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

# Method Syntax

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# String Formatting

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

# Indexes

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)): print(i, seq[i])

# Slices

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
# Tuples
	
tax = ('Homo', 'sapiens', 9606)
print(tax)

# s[0] = 'C'
# tax[0] = 'human'

print(tax[0])
print(tax[::-1])

# enumerate() and zip()

nts = 'ACGT'
for i in range(len(nts)): print(i, nts[i])

for i, nt in enumerate(nts): print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)): print(nts[i], names[i])

for nt, name in zip(nts, names): print(nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day         to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

# Practice Problems

def find_min(l):
	l.sort()
	return l[0]
print(find_min([1, 2, 3]))
print(find_min(['b', 'c', 'a']))

def find_minmax(l):
	l.sort()
	return [l[0], l[len(l) - 1]]
print(find_minmax([1, 2, 3]))
print(find_minmax(['b', 'c', 'a']))

def mean(l):
	total = 0
	for i in (l): total += i
	return total / len(l)
print(mean([4, 5, 6]))
print(mean([90, 25, 65]))

def entropy(l):
	h = 0
	for i in l: h -= i * math.log2(i)
	return h
print(entropy([.1, .5, .7, .3]))

def kl_distance(l1, l2):
	d = 0
	for p, q in zip(l1, l2): d += p * math.log2(p/q)
	return -d
list1 = [.5, .6, .2, .8]
list2 = [.6, .8, .8, .9]
print(kl_distance(list1, list2))

# Command Line Data

print(sys.argv)

i = int('42')
x = float('0.61803')
print(i * x)

# x = float('hello')

# Pairwise Comparison

# for i in range(0, len(list))
# 	for j in range(X, len(list)):
# X = 0: all combinatiosn
# X = i: half matrix with diagonal
# X = i + 1: half matrix without diagonal

