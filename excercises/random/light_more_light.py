#http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110701&format=html
from math import sqrt

def solve(n):
    ison = True
    for i in range(2, (n+1)//2 + 1):
        if n % i == 0: ison = not ison
    ison = not ison # last walk, since we go only to //2
    return ison


def solve2(n):
    x = sqrt(n)
    if x*x == n: return True
    else: return False


print(solve(3), solve2(3))
print(solve(9), solve2(9))
print(solve(6241), solve2(6241))
print(solve(8191), solve2(8191))
