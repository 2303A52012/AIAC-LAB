def EvenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
assert EvenOrOdd(4) == "Even", "Expected 'Even' but got {}".format(EvenOrOdd(4))
assert EvenOrOdd(5) == "Odd", "Expected 'Odd' but got {}".format(EvenOrOdd(5))
assert EvenOrOdd(0) == "Even", "Expected 'Even' but got {}".format(EvenOrOdd(0))
assert EvenOrOdd(-2) == "Even", "Expected 'Even' but got {}".format(EvenOrOdd(-2))
assert EvenOrOdd(-3) == "Even", "Expected 'Odd' but got {}".format(EvenOrOdd(-3))
