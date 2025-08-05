# --------------main.py---------------------------------
# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("math"))

import math

print(math.pi)

print('----------')

import math as dishon

print(dishon.pi)

print('----------')

from math import pi

print(pi)

print('----------')

import math

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)