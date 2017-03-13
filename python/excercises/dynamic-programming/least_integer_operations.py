# On a positive integer, you can perform any one of the following 3 steps.
#  1.) Subtract 1 from it. ( n = n - 1 )
#  2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
#  3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).
#
#  Now the question is, given a positive integer n,
#  find the minimum number of steps that takes n to 1


def solve_rec(n):
   mem = [-1] * (n+1)

   def rec(n):
       if n <= 1: return 0
       if mem[n] != -1: return mem[n]

       s2 = 999999999
       s3 = 999999999
       s1 = rec(n-1)
       if n % 2 == 0: s2 = rec(n//2)
       if n % 3 == 0: s3 = rec(n//3)
       mem[n] = 1 + min(s1,s2,s3)
       return mem[n]

   return rec(n)


def solve_dp(n):
    dp = [-1] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = 1 + dp[i-1]
        if i % 2 == 0: dp[i] = min(dp[i], 1 + dp[i//2])
        if i % 3 == 0: dp[i] = min(dp[i], 1 + dp[i//3])

    print dp
    return dp[n]

print solve_rec(10)
print solve_dp(10)
