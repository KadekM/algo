def rec(price, n):
    if n == 0: return 0
    q = -99999999
    for i in range(n):
        q = max(q, price[i] + rec(price, n-i-1))

    return q



n = 10
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
dp = [0] * n
dp[0] = 1

print rec(prices, 10)

