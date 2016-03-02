# Each Bytelandian gold coin has an integer number written on it.
# A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4.
# But these numbers are all rounded down (the banks have to make a profit).

# You can also sell Bytelandian coins for American dollars.
# The exchange rate is 1:1. But you can not buy Bytelandian coins.

# You have one gold coin. What is the maximum
# amount of American dollars you can get for it?


def solve(n):
    dp = range(0, n+1)
    # 1,2,3 cases are covered by range
    for i in range(4, n+1):
        dp[i] = max(dp[i], dp[i//2]+dp[i//3]+dp[i//4])


    print dp
    return dp[n]

print solve(12) # 12
print solve(2) # 2
