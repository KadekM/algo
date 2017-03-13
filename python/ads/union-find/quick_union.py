# Quick union (lazy approach)
class Union_find:
    def __init__(self, number_of_elements):
        self.ids = range(number_of_elements)

    def load(self, xs):
        self.ids = xs

    # O(n) traverse the tree up
    def find(self, x):
        while x != self.ids[x]: x = self.ids[x]
        return x

    # O(n) traverse to roots on both elements and see if it match
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # O(n)
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        self.ids[i] = j


uf = Union_find(10)

uf.load([0,1,9,4,9,6,6,7,8,9])
print uf.find(3) # should be 9
print uf.find(2) # should be 9
print uf.find(7) # should be 7
print uf.connected(1, 9) # should be False
print uf.connected(2, 4) # should be True

uf.union(1,9)
print uf.connected(1, 9) # should be True

