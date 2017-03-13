#http://www.programming-challenges.com/pg.php?page=downloadproblem&format=html&probid=110103

def trun(x):
    return (x * 100) //100

def solve(xs):
    n = len(xs)
    avg = float(sum(xs))/n
    #print "average is %f" % avg

    change = 0.0
    for x in xs:
        if x < avg:
            change += avg-x #TODO truncate here to cents
            #print "%f must handle %f" % (x, avg-x)

    return change


print solve([10.0, 20.0, 30.0]) # 11.99
print solve([15.0, 15.01, 3.0, 3.01]) # 10.00
print solve([9999.10, 9999.10, 9999.00, 9999.10]) #0.07
print solve([1.01, 0.99, 0.99]) #0.01
