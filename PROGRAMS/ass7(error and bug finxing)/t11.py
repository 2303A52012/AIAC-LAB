def add_values(a, b):
    return int(a) + int(b)  # Bug: TypeError due to string conversion; fixed by converting string to integer
print(add_values(5, "10"))
print(add_values("3", "7"))
print(add_values("4", 6))
print(add_values(2, 8))
'''
we were trying to add an integer (5)
to a string ("10"), which is not allowed in Python. By converting the string "10" 
to an integer using int("10"), we can successfully perform the addition without any errors.
'''