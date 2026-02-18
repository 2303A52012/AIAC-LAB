# write a py function that returns febanacci series of n terms and test with assert statements

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = [0, 1]
        for i in range(2, n):
            next_term = series[i-1] + series[i-2]
            series.append(next_term)
        return series
# Test cases
assert fibonacci(0) == [], "Expected [] but got {}".format(fibonacci(0))
assert fibonacci(1) == [0], "Expected [0] but got {}".format(fibonacci(1))
assert fibonacci(2) == [0, 1], "Expected [0, 1] but got {}".format(fibonacci(2))
assert fibonacci(5) == [0, 1, 1, 2, 3], "Expected [0, 1, 1, 2, 3] but got {}".format(fibonacci(5))
assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Expected [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] but got {}".format(fibonacci(10))
assert fibonacci(3) == [0, 1, 1], "Expected [0, 1, 1] but got {}".format(fibonacci(3))
assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8], "Expected [0, 1, 1, 2, 3, 5, 8] but got {}".format(fibonacci(7))