def gcd(p, q):
    if q == 0: return p
    else: return gcd(q, p%q)


print gcd(7, 3)
print gcd(20, 4)
print gcd(4, 1)
print gcd(35, 15)
