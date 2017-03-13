
def solve(a):
    n = len(a)
    r = a[n//2::-1]
    l = a[::-1]
    print a+r
    print l+a


solve("moth")
solve("bbba")