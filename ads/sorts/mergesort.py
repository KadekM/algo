def merge_sort(xs):
    if len(xs) <= 1: return xs

    def split(xs):
        n = len(xs)//2
        return xs[:n], xs[n:]

    def merge(xs, ys):
        m, n = len(xs), len(ys)
        i = j = k = 0
        res = [None] * (m + n)
        while i < m and j < n:
            if xs[i] <= ys[j]:
                res[k] = xs[i]
                i += 1
            elif xs[i] > ys[j]:
                res[k] = ys[j]
                j += 1
            k += 1

        while i < m:
            res[k] = xs[i]
            i += 1
            k += 1
        while j < n:
            res[k] = ys[j]
            j += 1
            k += 1
        return res

    ls, rs = split(xs)
    return merge(merge_sort(ls), merge_sort(rs))

import random
arr = random.sample(range(20), 15)
print arr

print merge_sort(arr)
