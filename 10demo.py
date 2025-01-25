# 10demo.py by Ethan Chan

import math

print ('hello, again') # greeting

print (1.5e-2)
print (5 % (1 + 2))
print (3 + 4)
print (3**3)
print (math.pow(3, 3))
print (math.sqrt(4))
print (math.log10(1000))

print (0.1 * 1)
print (0.1 * 3)

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

def ftoc(f): return (f - 32) * 5 / 9
def ctof(c): return (c * 9 / 5) + 32
def mph_to_kph(mph): return mph * 1.60934
def kph_to_mph(kph): return kph / 1.60934
def compute_dna_concentration(od260) : return od260 * 50
