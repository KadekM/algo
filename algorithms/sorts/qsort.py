from random import *

# Not in memory. Only conceptual impl
# Quick sort is by definition in memory sort!

def qsort_rec(xs):
    if len(xs) <= 1: return xs
    pivot = 0
    left = list(filter(lambda x: x < xs[pivot], xs[1:]))
    right = list(filter(lambda x: x >= xs[pivot], xs[1:]))
    return qsort_rec(left) + [xs[pivot]] + qsort_rec(right)


# In memory qsort
def qsort(xs, l=0, r=None):
    if r is None: r = len(xs)-1
    if l >= r: return

    i, j = l, r
    pivot = xs[randint(i, j)]
    while i <= j:
        while xs[i] < pivot: i += 1
        while xs[j] > pivot: j -= 1
        if i <= j:
            xs[i], xs[j] = xs[j], xs[i]
            i, j = i+1, j-1

    qsort(xs, l, j)
    qsort(xs, i, r)
