def bsearch_min(xs, e, l=0, r=None):
    if r is None: r = len(xs)-1
    while l <= r:
        mid = (l + r + 1) // 2
        if e <= xs[mid]: r = mid-1
        elif e > xs[mid]: l = mid+1

    return l

def bsearch_max(xs, e, l=0, r=None):
    if r is None: r = len(xs)-1
    while l <= r:
        mid = (l + r + 1) // 2
        if e < xs[mid]: r = mid-1
        elif e >= xs[mid]: l = mid+1

    return r

def cnt_amount(xs, e):
    l = bsearch_min(xs, e)
    r = bsearch_max(xs, e)
    return (l, r, r-l+1)


xs = [1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6]

print(cnt_amount(xs, 1))
print(cnt_amount(xs, 2))
print(cnt_amount(xs, 3))
print(cnt_amount(xs, 4))
print(cnt_amount(xs, 5))
print(cnt_amount(xs, 6))

