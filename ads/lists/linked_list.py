# mutable
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


# O(n)
def display(xs):
    x = xs
    while x is not None:
        print x.value
        x = x.next


# O(n)
def append(xs, v):
    x = xs
    while x.next is not None:
        x = x.next

    x.next = Node(v, None)


# O(n)
def find(xs, v):
    x = xs
    while x.value != v and x.next is not None:
        x = x.next

    if x.value == v: return x
    else: return None


xs = Node(3,Node(2,Node(4)))
append(xs, 6)
display(xs)
print find(xs, 5)
print find(xs, 6).value
