def bsearch(xs, x, l=0, r=None):
    if r is None: r = len(xs)-1
    res = None
    while l <= r:
        mid = (l+r+1)//2
        if x < xs[mid]:
            r = mid - 1
        elif x > xs[mid]:
            l = mid + 1
        else: return mid
    return res


def col(M, i):
    return [row[i] for row in M]

def bsearch_mat(M, x):
    cols = len(M)
    rows = len(M[0])
    for i in range(rows):
        if x <= M[i][cols-1]:
            return i, bsearch(M[i], x)

    return None


A = [[-4, -1,  4,  5],
    [ -3,  0,  6, 10],
    [  1,  8, 11, 15],
    [ 17, 19, 22, 30]]

#print bsearch([-4, -1, 4, 5], 3), 2
#print bsearch([-4, -1, 4, 5], 2), 2
#print bsearch([-4, -1, 4, 5], -2), 0
#print bsearch([-4, -1, 4, 5], 6), 3

print bsearch_mat(A, 5)
print bsearch_mat(A, -5)
print bsearch_mat(A, 21)
print bsearch_mat(A, 19)
print bsearch_mat(A, 33)
