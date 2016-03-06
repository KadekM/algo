class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

# finds the node
def find(bt, v):
    if bt.v == v: return bt
    elif bt.v > v and bt.l is not None: return find(bt.l, v)
    elif bt.v < v and bt.r is not None: return find(bt.r, v)
    else: return None

# finds node which should have the value, or parent
def findClosest(bt, v):
    if bt.v == v: return bt
    elif bt.v > v:
        if bt.l is None: return bt
        else: return findClosest(bt.l, v)
    elif bt.v < v:
        if bt.r is None: return bt
        else: return findClosest(bt.r, v)

# returns parent of node
def parent(bt, v, prev=None):
    if bt == None or bt.v == v: return prev
    elif bt.v > v: return parent(bt.l, v, bt)
    else: return parent(bt.r, v, bt)


def insert(bt, v):
    closest = findClosest(bt, v)
    if closest.v == v: return False
    elif closest.v > v:
        closest.l = Node(v)
        return True
    else:
        closest.r = Node(v)
        return True

def depth(bt):
    if bt is None: return 0
    return 1+max(depth(bt.l), depth(bt.r))

def btmin(bt):
    if bt.l is None: return bt
    else: return btmin(bt.l)


def btmax(bt):
    if bt.r is None: return bt
    else: return btmax(bt.r)

#TODO
def delete(bt, v):
    return


def prefix(bt):
    if bt is None: return []
    return [bt.v] + prefix(bt.l) + prefix(bt.r)

def infix(bt):
    if bt is None: return []
    return infix(bt.l) + [bt.v] + infix(bt.r)

def postfix(bt):
    if bt is None: return []
    return postfix(bt.l) + postfix(bt.r) + [bt.v]



bt = Node(34, Node(12), Node(54))

print(find(bt, 84))
print(findClosest(bt, 84).v)
print(insert(bt, 12))
print(insert(bt, 7))
print(insert(bt, 32))
print(infix(bt))
print(depth(bt))
print(btmin(bt).v)
print(btmax(bt).v)
print(parent(bt, 12).v)
