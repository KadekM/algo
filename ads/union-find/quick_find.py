# Quick find (eager approach)
class Union_find:
    def __init__(self, amount_of_elems):
        # each starts with its own group
        # value is group id
        self.ids = range(amount_of_elems)

    # O(1)
    def find(self, x):
        return self.ids[x]

    # O(1)
    def connected(self, x, y):
        return self.find(x) == self.find(y)

    # O(n), convention: assign all from groupY to groupX
    def union(self, x, y):
        groupX = self.find(x)
        groupY = self.find(y)
        for key, group in enumerate(self.ids):
            if group == groupY: self.ids[key] = groupX


uf = Union_find(10)

print uf.connected(1, 2)
uf.union(1, 2)
uf.union(1, 3)
uf.union(3, 4)
uf.union(6, 7)
print uf.connected(1, 2)
print uf.connected(1, 4)
print uf.connected(1, 6)


