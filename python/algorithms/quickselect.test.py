from algorithms.quickselect import *
from random import shuffle

xs = [31, 6, 2, 4, 11, 32, 7]
shuffle(xs)

print(quickselect(xs, 3))
