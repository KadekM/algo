from random import *

from algorithms.sorts.qsort import *

arr = sample(range(20), 15)
print(arr)
print(qsort_rec(arr))

qsort(arr)
print(arr)
