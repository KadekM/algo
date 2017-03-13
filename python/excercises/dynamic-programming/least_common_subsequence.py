#https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

def solve(a, b):
    dp = [[0] * (len(a)+1) for x in range(len(b)+1)]
    jj = 1

    for j in b:
        ii = 1
        for i in a:
            if i == j: dp[jj][ii] = dp[jj-1][ii-1]+1
            else: dp[jj][ii] = max(dp[jj-1][ii], dp[jj][ii-1])
            ii += 1
        jj += 1

    print dp
    return dp[len(b)][len(a)]


print solve("srjm", "tsrm")
