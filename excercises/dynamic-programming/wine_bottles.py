# There are wine bottles with prices, i.e. [1 3 2 4 5 2 3 6 3]
# Each year, their price double
# Each year, we sell either leftmost or rightmost
# What is maximum profit we can make?

mem = [[-1 for x in range(10)] for y in range(10)]

# got memoization. Two arguments are varying l & r. That's how
# it's possible to observe that that can be memoized
def solve_rec(xs, l=0, r=None):
    if r is None: r = len(xs)-1
    #print "calcing", l, r

    year = len(xs)-r+l
    if mem[l][r] != -1:
        print "from cache", l, r
        return mem[l][r]

    if l == r: return year * xs[l]

    left_calc = year * xs[l] + solve_rec(xs, l+1, r)
    right_calc = year * xs[r] + solve_rec(xs, l, r-1)
    maxx = max(left_calc, right_calc)
    mem[l][r] = maxx

    return maxx


def solve(xs):
    dp = range(1, len(xs)+1)
    for i in dp:
        dp[0] = 1

    print dp
    
print solve_rec([1, 4, 2, 3])
print mem
print solve([1, 4, 2, 3])
