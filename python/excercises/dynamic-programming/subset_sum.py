# find minimal subset that adds to `num`

def solve(xs, num):
    dp = [0] * (num+1)
    dp[0] = 1
    sol = [-1] * (num+1)
    rev = sorted(xs, reverse=True)

    for i in range(1, num+1):
        for x in rev:
            before = i-x
            if before >= (i+1)//2:
                break
            elif before < 0: continue
            elif before == 0:
                dp[i] = 1
                sol[i] = max(sol[i], x)
            else:
                dp[i] = max(dp[i], dp[before])
                sol[i] = max(sol[i], x)


    #print dp
    #print sol
    if dp[num] == 1:
        print "found for %s and amount %s, solution:" % (xs, num)
        nm = num
        s = sol[nm]
        while nm > 0:
            print s
            nm -= s
            s = sol[nm]

        print "-----"
    else:
        print "not found for %s and amount %s" % (xs, num)



solve([2,3,7], 4)
solve([2,3,7], 12)
solve([2,3,7], 13)
solve([2,3,7,11,25,32], 45)
solve([2,3,7,11,25,32], 34)
solve([2,3,7,11,25,32], 35)
