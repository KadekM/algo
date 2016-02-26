# Weighted quick union (lazy approach)
class Union_find:
    def __init__(self, number_of_elements):
        self.ids = range(number_of_elements)
        self.cnt = [1] * number_of_elements

    def load(self, xs):
        self.ids = xs
        self.cnt = [1] * len(xs)

    # O(log n) traverse the tree up
    def find(self, x):
        path = []
        while x != self.ids[x]:
            path.append(x) # collect path as we go
            x = self.ids[x]

        # compress:
        for i in path:
            self.ids[i] = x
            self.cnt[i] = 0
        self.cnt[x] += len(path)

        return x

    # O(log n) traverse to roots on both elements and see if it match
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # O(log n)
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)

        # Join smaller subtree to larger
        if self.cnt[i] <= self.cnt[j]:
            self.ids[i] = j
            self.cnt[j] += self.cnt[i]
            self.cnt[i] = 0
        else:
            self.ids[j] = i
            self.cnt[i] += self.cnt[j]
            self.cnt[j] = 0


uf = Union_find(10)

uf.load([0,1,9,4,9,6,6,7,8,9])
print uf.find(3) # should be 9
print uf.find(2) # should be 9
print uf.find(7) # should be 7
print uf.connected(1, 9) # should be False
print uf.connected(2, 4) # should be True

uf.union(1,9)
print uf.connected(1, 9) # should be True
print uf.connected(2, 8) # should be False

