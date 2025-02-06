# Stats

import sys
import math

prob = []

for arg in sys.argv[1:]: prob.append(float(arg))   # making list

prob.sort()	# finding max and min
maximum = prob[len(prob) - 1]
minimum = prob[0]

total = 0	# finding mean and sd
for num in prob: total += num
mean = total / len(prob)
sdsquare = 0
for num in prob: sdsquare += (mean - num)**2 / len(prob)
sd = math.sqrt(sdsquare)

med = 0		#finding median
if len(prob) % 2 == 1: med = prob[int(len(prob)/2 - .5)]
else:		       med = (prob[len(prob)/2 - 1] + prob[len(prob)/2]) / 2

print('You listed ', len(prob), 'values')
print('max: ', maximum, ' min: ', minimum)
print('mean: ', mean, ' sd: ', f'{sd:.4}')
print('median: ', med)
