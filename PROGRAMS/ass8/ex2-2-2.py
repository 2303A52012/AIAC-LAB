def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Test cases
assert factorial(0) == 1, "Expected 1 but got {}".format(factorial(0))
assert factorial(1) == 1, "Expected 1 but got {}".format(factorial(1))
assert factorial(5) == 120, "Expected 120 but got {}".format(factorial(5))
assert factorial(10) == 3628800, "Expected 3628800 but got {}".format(factorial(10))
assert factorial(3) == 6, "Expected 6 but got {}".format(factorial(3))
assert factorial(7) == 500, "Expected 5040 but got {}".format(factorial(7))
assert factorial(20) == 2432902008176640000, "Expected 2432902008176640000 but got {}".format(factorial(20))
