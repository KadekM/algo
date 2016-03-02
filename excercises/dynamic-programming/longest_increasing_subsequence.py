# Given a sequence of n real numbers A(1) ... A(n),
# determine a subsequence (not necessarily contiguous)
# of maximum length in which the values in the subsequence
# form a strictly increasing sequence.


# O(n^2)
def longest(xs):
    dp = [0] * len(xs)
    for i, x in enumerate(xs):
        seq = filter(lambda m: m[1] < x,zip(dp[:i], xs[:i]))
        if len(seq) == 0: maxx = 1
        else: maxx = max(seq)[0]+1
        dp[i] = maxx

    print dp
    return max(dp)


print longest([1,3,1,2,3]) # should be 3 - 1,2,3
print longest([1,0,1,2,3]) # should be 4 - 0,1,2,3
print longest([1,2,3,4,5]) # should be 5 - ...

# 1 2 5 9 0 1 2 3 4 5 0 1 10
# 1 2 3 4 1 2 3 4 5 6 0 2 7
print longest([1,2,3,1,2,3,4,5,1,2,3,6]) # should be 6 - 1,2,3,4,5,6

print longest([1,2,5,9,0,1,2,3,4,5,0,10]) # should be 7 - 0,1,2,3,4,5,10

print longest([1,2,3,0,1,4,0,1,7,0,2,3,0,5,1,2,6]) # should be 6 - 1,2,3,4,5,6


