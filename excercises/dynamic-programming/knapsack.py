# Knapsack with item repetition


def solve_nonrepeating(v, w, limit):
    return -1

def solve_repeating(v, w, limit):
    vl = len(v)
    wl = len(w)

    dp = [-1 for x in xrange(5)] *
    print dp


n = 7
v = [1,3,2,5,7,2,3]
w = [2,3,1,4,5,3,1]
limit = 10


print solve_nonrepeating(v, w, limit)
print solve_repeating(v, w, limit)
