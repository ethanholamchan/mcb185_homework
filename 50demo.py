import random
import time
import itertools

# Sets

s = {'A', 'C', 'G'}
print(s)
s.add('T')
print(s)
s.add('A')
print(s)
'''
def random_names(n, k):
	klist = list()
	kset = set()
	for _ in range(n):
		kmer = ''.join(random.choices('ACGT', k=k))
		klist.append(kmer)
		kset.add(kmer)
	return klist, kset

for size in range(1000, 10000, 1000):
	list1, set1 = random_names(size, 10)
	list2, set2 = random_names(size, 10)
	
	t0 = time.time()
	for name1 in list1:
		if name1 in list2: pass
	t1 = time.time()
	list_time = t1 - t0
	
	t0 = time.time()
	for name1 in list1:
		if name1 in set2: pass
	t1 = time.time()
	set_time = t1 - t0
	
	print(list_time, set_time, list_time/set_time)
	
# Dictionaries

d = {}
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])
d['pig'] = 'oink'
print(d)
d['cat'] = 'mew'
print(d)
del d['cat']
print(d)

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))

# Lookup Tables

kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)
'''
# Kmers
for nts in itertools.product('ACGT', repeat = 2):
	print(nts)
