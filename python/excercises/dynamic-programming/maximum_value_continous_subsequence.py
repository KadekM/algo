# Given a sequence of n real numbers A(1) ... A(n), determine a contiguous subsequence
# A(i) ... A(j) for which the sum of elements in the subsequence is maximized.

# kadane algorithm, O(n) runtime
def solve_kadane(xs):
    maxx = current = xs[0]
    for x in xs[1:]:
        current = max(x, current+x)
        maxx = max(maxx, current)
    return maxx


# dynamic programming solution
def solve_dp(xs):
    dp = [0] * len(xs)
    i = 0
    while i < len(xs):
        dp[i] = max(dp[i-1]+xs[i], xs[i])
        i += 1

    print dp
    return max(dp)


xs = [3, -4, 2, -1, 3, -9, 3]
#            ^   ^  ^ = 4

print solve_kadane(xs)
print solve_dp(xs)
