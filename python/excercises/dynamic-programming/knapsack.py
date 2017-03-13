# Knapsack with item repetition


def solve_nonrepeating(v, w, limit):
    return -1

def solve_repeating(v, w, limit):
    wl = len(w)

    dp = [[-1 for x in xrange(limit)] for x in xrange(wl)]


    for i in xrange(wl):
        for j in xrange(1,limit):
            if i == 0: above = -1
            else: above = dp[i-1][j]


            if j - w[i] < 0:
                dp[i][j] = max(0, above)
                continue

            if j - w[i] == 0:
                dp[i][j] = v[i]
                continue


            leftie = v[i] + dp[i][j - w[i]]
            dp[i][j] = max(above, leftie)

    print dp


v = [1,3,2,5]
w = [2,3,1,4]
limit = 6


print solve_nonrepeating(v, w, limit)
print solve_repeating(v, w, limit)
