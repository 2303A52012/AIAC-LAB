def calculate_area(length, breadth):
    if length < 0 or breadth < 0:
        return "Length and breadth must be non-negative"
    return length * breadth
print(calculate_area(5, 10))
print(calculate_area(7, 3))
print(calculate_area(0, 5))
print(calculate_area(-2, 4))