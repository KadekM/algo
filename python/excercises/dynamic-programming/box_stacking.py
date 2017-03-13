# You are given a set of n types of rectangular 3-D boxes,
# where the i^th box has height h(i), width w(i) and depth
# d(i) (all real numbers). You want to create a stack of
# boxes which is as tall as possible, but you can only stack
# a box on top of another box if the dimensions of the 2-D
# base of the lower box are each strictly larger than those
# of the 2-D base of the higher box. Of course, you can rotate
# a box so that any side functions as its base. It is also allowable
# to use multiple instances of the same type of box.

# O(n^2)


def solve(hs, ws, ds):
    n = len(hs)
    # rotate all 3 sides (since we have infinite boxes, its fine)
    for i in range(n):
        a, b, c = hs[i], ws[i], ds[i]
        hs.append(b); ws.append(c); ds.append(a)
        hs.append(c); ws.append(a); ds.append(b)

    n *= 3 # now we have thrice the cubes

    # sort them by their base
    els = sorted(map(lambda x: (x[0]*x[1], x[0], x[1], x[2]), zip(ws, ds, hs)), reverse=True)

    dp = [0] * n
    for i in range(n):
        elss = filter(lambda x: x[1] < els[i][1] and x[2] < els[i][2], els[i:])
        if elss == []:
            dp[i] = els[i][3]
            continue

        maxH = max(elss, key=lambda x:x[3])
        dp[i] = maxH[3] + els[i][3]

    print dp
    return max(dp)

hs = [5,3,1,7,5,4]
ws = [4,2,4,3,1,7]
ds = [5,3,1,6,3,2]
print solve(hs, ws, ds)

hs = [1]
ws = [2]
ds = [2]
print solve(hs, ws, ds) # should be 2 -> rotate the box
