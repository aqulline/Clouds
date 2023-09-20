import numpy

a = numpy.array([1, 2, 3,4])

print(a[[False, True, False, False]])

d = {x : x*x for x in range(1, 100)}

s = [1, 2, 3] * 3