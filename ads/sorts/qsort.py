def qsort_rec(xs):
    if len(xs) <= 1: return xs
    pivot = 0
    left = filter(lambda x: x < xs[pivot], xs[1:])
    right = filter(lambda x: x >= xs[pivot], xs[1:])
    return qsort_rec(left) + [xs[pivot]] + qsort_rec(right)


import random
arr = random.sample(range(20), 15)
print arr
print qsort_rec(arr)
