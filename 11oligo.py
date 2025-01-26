import math

def tm(a, c, g, t):
	total = a + c + g + t
	if total <= 13: return (a + t) * 2 + (g + c) * 4
	else:		return 64.9 + 41 * (g + c - 16.4) / (a + c + g + t)
print(tm(5, 7, 3, 4))
