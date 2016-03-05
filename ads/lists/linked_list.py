# mutable impl
# None represents head of list is empty... could be special type
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


# O(n)
def display(xs):
    if xs.value is None : print("empty list");return
    x = xs
    while x is not None:
        print(x.value)
        x = x.next


# O(n)
def append(xs, v):
    if xs.value is None: xs.value = v; return;

    x = xs
    while x.next is not None:
        x = x.next

    x.next = Node(v, None)

# O(1)
def prepend(xs, v):
    return Node(v, xs)

# O(n)
def delete(xs, v):
    x = xs

    if x.value == v:
        if xs.next is None:
            xs.value = None
            return

        xs.value = xs.next.value
        xs.next = xs.next.next
        return


    while x.next is not None and x.next.value != v:
        x = x.next

    if x.next is not None:
        x.next = x.next.next

    return


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
print(find(xs, 5))
print(find(xs, 6).value)

xs2 = prepend(xs, 99)
delete(xs2, 5)
delete(xs2, 99)
delete(xs2, 6)
delete(xs2, 2)
print("---")
display(xs2)
print("---")
delete(xs2, 4)
delete(xs2, 3)
display(xs2)
append(xs2, 5)
display(xs2)
