# How many encodings are if A-1 B-2 ... Z-26

def amount(char2):
    if len(char2)==1: return 1
    if char2[0] == '0' or char2[1] == '0': return 1
    i = int(char2)
    if i <= 26: return 2
    return 1

def solve(xs):
    dp = [1] * len(xs)
    dp[0] = 1
    dp[1] = amount(xs[0] + xs[1])

    for i in range(1, len(xs)):
        word = xs[i-1] + xs[i]
        #print "word", word, amount(word)
        if amount(word) == 2:
            dp[i] = dp[i-1]+dp[i-2]
        else:
            dp[i] = dp[i-1]

    print dp
    return dp[len(xs)-1]

print solve("25114") # 6
print solve("101") # 1
print solve("1111111111") # 89
print solve("3333333333") # 1