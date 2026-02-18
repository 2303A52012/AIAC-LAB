def sub(a,b):
    return a - b
assert sub(5, 3) == 2 
assert sub(10, 4) == 6
assert sub(-5, -3) == -4 , "Expected -4 but got {}".format(sub(-5, -3))
assert sub(0, 0) == 0