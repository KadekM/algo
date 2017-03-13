# O(n^2)
def insertion_sort(xs):
    n = len(xs)
    for i, x in enumerate(xs):
        j = i-1
        while j >= 0 and xs[j] > x:
            xs[j+1] = xs[j]
            j -= 1
        xs[j+1] = x



import random
arr = random.sample(range(20), 15)

print(arr)
insertion_sort(arr)
print(arr)
