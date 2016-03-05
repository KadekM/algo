import random




# Initializes skipped list
def skip_list(xs):
    res = [zip(xs, range(len(xs)))]

    row = 0
    while True:
        next = []
        for k, x in enumerate(res[row]):
            if random.randint(0, 1) == 1:
                next.append((x[0], k))


        if len(next) != 0:
            res.append(next)
            row += 1

        if len(next) == 1: break


    res.reverse()
    return res

#TODO
def find(skipped, x):
    return None

#TODO
def insert(skipped, x):
    return None

sl = skip_list([1,2,3,4,5,6,7,8,9,10])
print(sl)
print(find(sl, 5))


