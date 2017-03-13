# Count number of inversions in array
def count_inv(xs):
    if len(xs) <= 1: return 0

    def merge_and_count(xs):
        if len(xs) <= 1: return xs, 0

        def split(xs):
            n = len(xs)//2
            return xs[:n], xs[n:]

        def merge(xs, ys):
            m, n = len(xs), len(ys)
            res = [None] * (m+n)
            i = j = k = inv = 0
            while i < m and j < n:
                if xs[i] <= ys[j]:
                    res[k] = xs[i]
                    i += 1
                else:
                    res[k] = ys[j]
                    inv += m-i
                    j += 1
                k += 1

            while i < m:
                res[k] = xs[i]
                i += 1
                k += 1

            while j < n:
                res[k] = ys[j]
                j += 1
                k += 1

            return res, inv

        left, right = split(xs)
        leftm, lcnt = merge_and_count(left)
        rightm, rcnt = merge_and_count(right)
        merged, cnt = merge(leftm, rightm)

        return merged, cnt + lcnt + rcnt

    sorted, count = merge_and_count(xs)
    return count


print(count_inv([5,1,2,4,9,3]), 6)
print(count_inv([1,5,4,3]), 2+1)
print(count_inv([3,5,3,2,1]), 3+3+2+1)
