def binary_search(xs, x):
    l = 0
    r = len(xs)-1
    while l <= r:
        mid = (l+r+1)//2
        if xs[mid] > x: r = mid - 1
        elif xs[mid] < x: l = mid + 1
        else: return mid

    return -1


def binary_search_rec(xs, x):
    def _impl(l, r):
        if (l <= r):
            mid = (l+r+1)//2
            if xs[mid] > x: return _impl(l, r-1)
            elif xs[mid] < x:  return _impl(l-1, r)
            else: return mid
        else: return -1

    return _impl(0, len(xs)-1)

import random
arr = random.sample(range(20), 15)
arr.sort()
print(arr)

print(binary_search(arr, 1), binary_search_rec(arr, 1))
print(binary_search(arr, 2), binary_search_rec(arr, 2))
print(binary_search(arr, 3), binary_search_rec(arr, 3))
print(binary_search(arr, 4), binary_search_rec(arr, 4))
print(binary_search(arr, 5), binary_search_rec(arr, 5))
