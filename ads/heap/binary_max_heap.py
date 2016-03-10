def find_max(xs): return xs[0]

def delete_max(xs):
    max = xs[0]
    if len(xs) == 1: xs.pop()
    else:
        xs[0] = xs.pop() # change first and last, and remove 0 len
        shift_down(xs, 0)
    return max

def heap_swap(xs, i, j):
    tmp = xs[i]
    xs[i] = xs[j]
    xs[j] = tmp

def shift_up(xs, i):
    if i <= 0: return

    parent = (i-1)//2
    if xs[i] > xs[parent]:
        heap_swap(xs, i, parent)
        shift_up(xs, parent)


def shift_down(xs, i):
    child = i * 2 + 1

    if child >= len(xs): return

    if child + 1 < len(xs) and xs[child] < xs[child+1]:
        child += 1

    if xs[child] > xs[i]:
        heap_swap(xs, i, child)
        shift_down(xs, child)


def insert(xs, x):
    xs.append(x)
    shift_up(xs, len(xs)-1)


def increase_key(xs, i, dx):
    xs[i] += dx
    if dx > 0: shift_up(xs, i)
    elif dx < 0: shift_down(xs, i)

def merge(): pass
