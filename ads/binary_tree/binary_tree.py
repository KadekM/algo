import collections

# without pointer to parent
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

def has_children(bt):
    return bt.l is not None or bt.r is not None

# utility for deletion
def find_with_parent(bt, v, parent = None):
    if bt.v == v: return bt, parent
    elif bt.v > v and bt.l is not None: return find_with_parent(bt.l, v, bt)
    elif bt.v < v and bt.r is not None: return find_with_parent(bt.r, v, bt)
    else: return None, None

# utility for deletion
def find_min_with_parent(bt, parent = None):
    if bt.l is None: return bt, parent
    else: return find_min_with_parent(bt.l, bt)

def find_max_with_parent(bt, parent = None):
    if bt.r is None: return bt, parent
    else: return find_max_with_parent(bt.r, bt)

#TODO
def delete(bt, v):
    # deleted only node
    if bt.v == v and bt.l is None and bt.r is None:
        # you'd end up with empty tree, which is fine, but we'd need
        # a special class that represents it and handle it on each method
        # so it's ignored here for simplicity
        return False

    node, node_parent = find_with_parent(bt, v)
    if node is None: return False

    # no children, just unlink from parent
    if not has_children(node):
        if node == node_parent.l: node_parent.l = None
        else : node_parent.r = None
        return True
    # thus it has at least one child

    # node deleted has only one child
    if node.l is None: # must be right
        if node_parent.l == node: node_parent.l = node.r
        else: node_parent.r = node.r
        return True
    elif node.r is None: # must be left
        if node_parent.l == node: node_parent.l = node.l
        else: node_parent.r = node.l
        return True

    # thus it has both children, move min from right
    # work with value only (less linking nodes)
    min_from_right, min_from_right_parent = find_min_with_parent(node.r, node)
    node.v = min_from_right.v

    if min_from_right_parent is not None:
        min_from_right_parent.r = None # it's a min, so it must be on left

    return True


def prefix(bt):
    if bt is None: return []
    return [bt.v] + prefix(bt.l) + prefix(bt.r)

def infix(bt):
    if bt is None: return []
    return infix(bt.l) + [bt.v] + infix(bt.r)

def postfix(bt):
    if bt is None: return []
    return postfix(bt.l) + postfix(bt.r) + [bt.v]

def bfs_info(bt):
    res = []
    queue = collections.deque([bt])
    depths = {bt.v: 0}
    fromm = {bt.v: None}

    while len(queue) != 0:
        current = queue.popleft()

        if current.l is not None:
            queue.append(current.l)
            depths[current.l.v] = depths[current.v] + 1
            fromm[current.l.v] = (current.v, "L")
        if current.r is not None:
            queue.append(current.r)
            depths[current.r.v] = depths[current.v] + 1
            fromm[current.r.v] = (current.v, "R")

        res.append((current.v, depths[current.v], fromm[current.v]))

    return res


bt = Node(34, Node(12), Node(54))

print(find(bt, 83))
print(findClosest(bt, 84).v)
print(insert(bt, 12))
print(insert(bt, 7))
print(insert(bt, 32))
print(infix(bt))
print(depth(bt))
print(btmin(bt).v)
print(btmax(bt).v)
print(parent(bt, 12).v)
print(find_with_parent(bt, 7)[1].v)

print("-------")
bt2 = Node(100, Node(50, Node(25), Node(75)), Node(150, None, Node(200, None, Node(300))))
print(bfs_info(bt2))
print(delete(bt2, 359)) # delete non existing
print(delete(bt2, 200)) # delete with one child
print(delete(bt2, 300)) # delete without kids
print(bfs_info(bt2))
print(delete(bt2, 100)) # delete without parent
print(bfs_info(bt2))
print(delete(bt2, 50))
print(bfs_info(bt2))
print(delete(bt2, 75))
print(bfs_info(bt2))
print(delete(bt2, 25))
print(bfs_info(bt2))
print(delete(bt2, 150))
print(bfs_info(bt2))
