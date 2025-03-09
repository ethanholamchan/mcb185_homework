import sys
import gzip
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

minimum = 10000
mincolor = ''

with open(colorfile, 'rt') as fp:
	for line in fp:
		words = line.split()
		rgb = words[2].split(',')
		total = math.sqrt((R-int(rgb[0]))**2 + (G-int(rgb[1]))**2 + (B-int(rgb[2]))**2)
		if total < minimum:
			minimum = total
			mincolor = words[0]
print(mincolor)
