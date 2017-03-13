# You are given n types of coin denominations of values v(1) < v(2) < ... < v(n)
# (all integers). Assume v(1) = 1, so you can always make change for any amount
# of money C. Give an algorithm which makes change for an amount of money C with
# as few coins as possible.




coins = [1, 2, 3, 5]

print solve_dp(coins, 10)