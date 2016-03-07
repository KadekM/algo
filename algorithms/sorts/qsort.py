# Not in memory. Only conceptual impl
# Quick sort is by definition in memory sort!

def qsort_rec(xs):
    if len(xs) <= 1: return xs
    pivot = 0
    left = list(filter(lambda x: x < xs[pivot], xs[1:]))
    right = list(filter(lambda x: x >= xs[pivot], xs[1:]))
    return qsort_rec(left) + [xs[pivot]] + qsort_rec(right)


# Correct qsort
def qsort(xs): pass


import random
arr = random.sample(range(20), 15)
print(arr)
print(qsort_rec(arr))
