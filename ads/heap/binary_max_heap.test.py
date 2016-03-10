from ads.heap.binary_max_heap import *

hp = []
insert(hp, 5)
insert(hp, 7)
insert(hp, 10)
print(hp)

insert(hp, 4)
insert(hp, 8)
insert(hp, 12)
print(hp)

print(delete_max(hp))
print(hp)

print(delete_max(hp))
print(hp)
increase_key(hp, 2, 5)
print(hp)
increase_key(hp, 0, -6)
print(hp)
