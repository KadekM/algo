# https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

c = 0
def solve(xs):
    global c
    # we dont need whole E, basically we would need len(xs) x 2 matrix (end=n or n-1)
    # but nevermind
    mem = [[-1 for _ in xrange(len(xs))] for _ in xrange(len(xs))]

    def solve_rec(xs, s, e):
        if s > e: return 0

        if mem[s][e] != -1: return mem[s][e]
        global c; c += 1 #counting calls

        right = xs[s+1] + solve_rec(xs, s+3, e)
        if s+1 > e: right = 0

        calc = max(xs[s] + solve_rec(xs, s+2, e), right)
        mem[s][e] = calc
        return calc

    xxs = xs[:]
    xxs.extend([0])

    res = max(solve_rec(xxs, 0, len(xs)-2), solve_rec(xxs, 1, len(xs)-1))

    print "called %d times" % c
    c = 0
    return res


#10
print solve([1,5,1,5])
#10
print solve([1,5,1,1,5])
#11
print solve([1,5,1,1,0,5])
#19
print solve([10, 3, 2, 5, 7, 8])

#15
print solve([11, 15])
#21
print solve([7, 7, 7, 7, 7, 7, 7])
#16
print solve([0, 2, 3, 4, 5, 1, 2, 3, 4, 5])
#2926
print solve([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
             5, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
             52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72])

