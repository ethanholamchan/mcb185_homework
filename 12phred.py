import math

def char_to_prob(s): return 1 / (10**(ord('s')/10))
def prob_to_char(x): return -10 * math.log10(x)

print(char_to_prob('A'))
print(prob_to_char(0.001))
