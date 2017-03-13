from ads.heap.binary_max_heap import *

# heapsort should be in memory though
def heapsort(xs):
    hp = []
    for x in xs: insert(hp, x)

    while len(hp) != 0:
        yield delete_max(hp)


import random
arr = random.sample(range(20), 15)
print(arr)
print(list(heapsort(arr)))
