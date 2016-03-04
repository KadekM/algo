
# A sequence of numbers is called a zig-zag sequence if the differences
# between successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or negative.
# A sequence with fewer than two elements is trivially a zig-zag sequence.

# For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences
# (6,-3,5,-7,3) are alternately positive and negative.
# In contrast, 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences,
# the first because its first two differences are positive and the
# second because its last difference is zero.

# Given a sequence of integers, sequence, return the length
# of the longest subsequence of sequence that is a zig-zag sequence.
# A subsequence is obtained by deleting some number of elements (possibly zero)
# from the original sequence, leaving the remaining elements
# in their original order.


def solve(xs):
    n = len(xs)
    dp = [1] * n
    truh = [0] * n
    for i in xrange(1, n):
        truh[i] = xs[i]-xs[i-1]

    for i in xrange(1, n):
        v = 1
        for j in xrange(i-1, -1, -1):
            if truh[i] > 0 and truh[j] < 0:
                v = dp[j]
                break
            if truh[i] < 0 and truh[j] > 0:
                v = dp[j]
                break
        dp[i] = v + 1

    return dp[n-1]
    print dp
    print truh


# can be even done better by remembering maximum... or even greedy

# should be 7
print solve([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])

# should be 36
print solve([373, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244])