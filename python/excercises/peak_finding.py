def find_peak(xs):
    l = 0
    r = len(xs)-1
    while l < r:
        mid = (l + r + 1) // 2
        if xs[mid-1] > xs[mid]:
            r = mid - 1
        elif xs[mid+1] > xs[mid]:
            l = mid + 1
        else:
            return mid

# todo: does not handle peaks such as 1 2 3 4<- or ->4 3 2 1
# todo: 2D peaks

print find_peak([1,3,4,5,3,1])
print find_peak([1,3,4,2])
print find_peak([1,6,1,0])
