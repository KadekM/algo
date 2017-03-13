# Unlimited coins. How many ways to get it?
#https://www.hackerrank.com/challenges/coin-change


def solve(coins, n):
    m = len(coins)
    dp = [[0 for _ in range(n+1)] for _ in range(m)]
    for i in range(m): dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(len(coins)):
            jval = coins[j]
            lefter = dp[j][i-jval] if i-jval >= 0 else 0
            dp[j][i] = dp[j-1][i] + lefter

    #print(dp)
    return dp[m-1][n]


print(solve([2,5,3,6], 10))
